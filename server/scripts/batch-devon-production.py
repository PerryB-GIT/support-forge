#!/usr/bin/env python3
"""
Batch Devon Video Production
=============================
Processes all AI Launchpad Academy video scripts and generates
avatar videos using HeyGen API with Devon (August + Archer).

Usage:
    python batch-devon-production.py --list              # List all scripts
    python batch-devon-production.py --start             # Start production
    python batch-devon-production.py --start --priority 1  # Only priority 1 scripts
    python batch-devon-production.py --status            # Check status
    python batch-devon-production.py --resume            # Resume incomplete videos
"""

import os
import sys
import re
import json
import time
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict
from enum import Enum

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# ============================================================================
# Configuration
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
SCRIPTS_DIR = SCRIPT_DIR.parent.parent / "docs" / "academy-content" / "video-scripts"
OUTPUT_DIR = SCRIPT_DIR / "output" / "devon-videos"
STATE_FILE = SCRIPT_DIR / "devon-production-state.json"
LOG_FILE = SCRIPT_DIR / "devon-production.log"

# Devon avatar configuration
DEVON_CONFIG = {
    "avatar_id": "August_Casual_Front2_public",
    "voice_id": "453c20e1525a429080e2ad9e4b26f2cd",
    "avatar_name": "Devon",
    "voice_name": "Archer",
    "dimension": {"width": 1280, "height": 720}  # 720p due to plan limits
}

# HeyGen API
HEYGEN_API_BASE = "https://api.heygen.com/v2"

# Priority 1 scripts (core foundation)
PRIORITY_1_SCRIPTS = [
    "script-0.1", "script-0.2", "script-0.3",  # Module 0
    "script-1.1", "script-1.2", "script-1.3",  # Module 1
    "script-2.1", "script-2.2",                 # Module 2 (core)
    "script-3.1", "script-3.2",                 # Module 3 (core)
    "5.1-automation",                           # Module 5 foundation
    "7.1-credential",                           # Security essential
    "8.1-capstone", "8.2-building", "8.4-certification"  # Capstone
]

# HeyGen plan limits - 180 seconds max
# At ~130 wpm for avatar speech, 180s = ~390 words max
MAX_VIDEO_WORDS = 360  # Conservative limit for avatar pacing

# ============================================================================
# Data Classes
# ============================================================================

class VideoStatus(Enum):
    PENDING = "pending"
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class VideoScript:
    script_id: str
    title: str
    file_path: str
    raw_content: str
    spoken_text: str
    word_count: int
    estimated_duration: float  # minutes
    priority: int
    part: int = 1  # Part number for split scripts
    total_parts: int = 1  # Total parts if split

@dataclass
class VideoJob:
    script_id: str
    heygen_video_id: Optional[str] = None
    status: str = "pending"
    video_url: Optional[str] = None
    output_path: Optional[str] = None
    error: Optional[str] = None
    created_at: Optional[str] = None
    completed_at: Optional[str] = None
    duration: Optional[float] = None

# ============================================================================
# Script Parser
# ============================================================================

def extract_spoken_text(content: str) -> str:
    """
    Extract only the spoken dialogue from a video script.
    Removes screen directions, pause markers, headers, etc.
    """
    lines = content.split('\n')
    spoken_lines = []

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Skip markdown headers
        if line.startswith('#'):
            continue

        # Skip metadata lines
        if line.startswith('**') and ':' in line:
            continue
        if line.startswith('*') and ('word' in line.lower() or 'runtime' in line.lower()):
            continue

        # Skip horizontal rules
        if line == '---':
            continue

        # Skip screen directions [SCREEN: ...]
        if line.startswith('[SCREEN:') or line.startswith('[Screen:'):
            continue

        # Remove inline [SCREEN: ...] and [PAUSE] markers
        line = re.sub(r'\[SCREEN:[^\]]+\]', '', line)
        line = re.sub(r'\[PAUSE\]', '', line)
        line = re.sub(r'\[pause\]', '', line)

        # Skip production notes sections
        if 'PRODUCTION NOTES' in line.upper():
            break
        if 'KEY TERMS FOR PRONUNCIATION' in line.upper():
            break
        if 'POST-VIDEO RESOURCES' in line.upper():
            break

        # Clean up the line
        line = line.strip()

        # Skip bullet points that are just labels
        if line.startswith('- ') and ':' in line and len(line) < 50:
            continue

        if line:
            spoken_lines.append(line)

    # Join and clean up
    text = ' '.join(spoken_lines)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove markdown formatting
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Italic

    return text.strip()

def get_script_priority(filename: str) -> int:
    """Determine priority based on filename."""
    for p1_prefix in PRIORITY_1_SCRIPTS:
        if p1_prefix in filename.lower():
            return 1
    return 2

def split_text_into_chunks(text: str, max_words: int = MAX_VIDEO_WORDS) -> List[str]:
    """Split text into chunks respecting sentence boundaries."""
    words = text.split()
    if len(words) <= max_words:
        return [text]

    chunks = []
    current_chunk = []
    current_count = 0

    sentences = re.split(r'(?<=[.!?])\s+', text)

    for sentence in sentences:
        sentence_words = sentence.split()
        sentence_count = len(sentence_words)

        # If adding this sentence exceeds limit and we have content
        if current_count + sentence_count > max_words and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_count = 0

        current_chunk.append(sentence)
        current_count += sentence_count

    # Don't forget the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def load_all_scripts() -> List[VideoScript]:
    """Load and parse all video scripts, splitting long ones into parts."""
    scripts = []

    if not SCRIPTS_DIR.exists():
        logger.error(f"Scripts directory not found: {SCRIPTS_DIR}")
        return scripts

    for md_file in sorted(SCRIPTS_DIR.glob("*.md")):
        try:
            content = md_file.read_text(encoding='utf-8')
            spoken_text = extract_spoken_text(content)

            # Extract title from content or filename
            title_match = re.search(r'^#\s+(.+?)(?:\n|$)', content, re.MULTILINE)
            title = title_match.group(1) if title_match else md_file.stem

            # Clean up title
            title = re.sub(r'^Script\s+\d+\.\d+:\s*', '', title)
            title = re.sub(r'^Module\s+\d+\.\d+:\s*', '', title)

            priority = get_script_priority(md_file.stem)

            # Split into chunks if too long
            chunks = split_text_into_chunks(spoken_text)
            total_parts = len(chunks)

            for part_num, chunk_text in enumerate(chunks, 1):
                word_count = len(chunk_text.split())
                estimated_duration = word_count / 150  # ~150 words per minute

                # Create unique ID for parts
                if total_parts > 1:
                    script_id = f"{md_file.stem}-part{part_num}"
                    part_title = f"{title} (Part {part_num}/{total_parts})"
                else:
                    script_id = md_file.stem
                    part_title = title

                scripts.append(VideoScript(
                    script_id=script_id,
                    title=part_title,
                    file_path=str(md_file),
                    raw_content=content,
                    spoken_text=chunk_text,
                    word_count=word_count,
                    estimated_duration=round(estimated_duration, 1),
                    priority=priority,
                    part=part_num,
                    total_parts=total_parts
                ))

        except Exception as e:
            logger.error(f"Failed to parse {md_file.name}: {e}")

    return scripts

# ============================================================================
# State Management
# ============================================================================

class ProductionState:
    """Manages production state persistence."""

    def __init__(self, state_file: Path = STATE_FILE):
        self.state_file = state_file
        self.jobs: Dict[str, VideoJob] = {}
        self.load()

    def load(self):
        """Load state from file."""
        if self.state_file.exists():
            try:
                data = json.loads(self.state_file.read_text())
                for script_id, job_data in data.get("jobs", {}).items():
                    self.jobs[script_id] = VideoJob(**job_data)
            except Exception as e:
                logger.warning(f"Failed to load state: {e}")

    def save(self):
        """Save state to file."""
        data = {
            "jobs": {k: asdict(v) for k, v in self.jobs.items()},
            "updated_at": datetime.now().isoformat()
        }
        self.state_file.write_text(json.dumps(data, indent=2))

    def get_job(self, script_id: str) -> Optional[VideoJob]:
        return self.jobs.get(script_id)

    def update_job(self, job: VideoJob):
        self.jobs[job.script_id] = job
        self.save()

    def get_stats(self) -> Dict[str, int]:
        stats = {"total": len(self.jobs)}
        for status in VideoStatus:
            stats[status.value] = len([j for j in self.jobs.values() if j.status == status.value])
        return stats

# ============================================================================
# HeyGen Client
# ============================================================================

class HeyGenClient:
    """HeyGen API client."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'X-Api-Key': api_key,
            'Content-Type': 'application/json'
        })

    def generate_video(self, script: VideoScript, test_mode: bool = False) -> Dict[str, Any]:
        """Submit video generation request."""
        # Truncate if over 5000 chars
        text = script.spoken_text[:4900] if len(script.spoken_text) > 5000 else script.spoken_text

        payload = {
            "video_inputs": [{
                "character": {
                    "type": "avatar",
                    "avatar_id": DEVON_CONFIG["avatar_id"],
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": text,
                    "voice_id": DEVON_CONFIG["voice_id"]
                }
            }],
            "dimension": DEVON_CONFIG["dimension"],
            "title": f"Devon - {script.title}",
            "test": test_mode
        }

        try:
            response = self.session.post(
                f"{HEYGEN_API_BASE}/video/generate",
                json=payload,
                timeout=60
            )

            if response.ok:
                data = response.json()
                return {
                    "success": True,
                    "video_id": data.get("data", {}).get("video_id")
                }
            else:
                return {
                    "success": False,
                    "error": f"API error {response.status_code}: {response.text}"
                }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def check_status(self, video_id: str) -> Dict[str, Any]:
        """Check video generation status."""
        try:
            # Status endpoint is v1, not v2
            response = self.session.get(
                "https://api.heygen.com/v1/video_status.get",
                params={"video_id": video_id},
                timeout=30
            )

            if response.ok:
                data = response.json().get("data", {})
                return {
                    "success": True,
                    "status": data.get("status"),
                    "video_url": data.get("video_url"),
                    "duration": data.get("duration"),
                    "error": data.get("error")
                }
            else:
                return {"success": False, "error": f"API error {response.status_code}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def download_video(self, url: str, output_path: Path) -> bool:
        """Download completed video."""
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            response = requests.get(url, stream=True, timeout=300)
            response.raise_for_status()

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except Exception as e:
            logger.error(f"Download failed: {e}")
            return False

# ============================================================================
# Production Manager
# ============================================================================

class ProductionManager:
    """Manages the batch video production process."""

    def __init__(self, api_key: str):
        self.client = HeyGenClient(api_key)
        self.state = ProductionState()
        self.scripts = load_all_scripts()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def list_scripts(self, priority: Optional[int] = None):
        """List all scripts with their status."""
        print("\n" + "=" * 80)
        print("  AI LAUNCHPAD ACADEMY - DEVON VIDEO PRODUCTION")
        print("=" * 80 + "\n")

        scripts = self.scripts
        if priority:
            scripts = [s for s in scripts if s.priority == priority]

        print(f"Total Scripts: {len(scripts)}")
        print(f"Total Words: {sum(s.word_count for s in scripts):,}")
        print(f"Est. Runtime: {sum(s.estimated_duration for s in scripts):.0f} minutes")
        print()

        p1 = [s for s in scripts if s.priority == 1]
        p2 = [s for s in scripts if s.priority == 2]

        print(f"Priority 1 (Core): {len(p1)} scripts")
        print(f"Priority 2 (Extended): {len(p2)} scripts")
        print()

        print("-" * 80)
        print(f"{'ID':<40} {'Words':>6} {'Min':>5} {'Pri':>3} {'Status':<12}")
        print("-" * 80)

        for script in sorted(scripts, key=lambda s: (s.priority, s.script_id)):
            job = self.state.get_job(script.script_id)
            status = job.status if job else "pending"

            status_icon = {
                "pending": "[ ]",
                "queued": "[Q]",
                "processing": "[..]",
                "completed": "[OK]",
                "failed": "[!!]"
            }.get(status, "[??]")

            print(f"{script.script_id:<40} {script.word_count:>6} {script.estimated_duration:>5.1f} {script.priority:>3} {status_icon} {status}")

        print("-" * 80)

        stats = self.state.get_stats()
        print(f"\nProduction Status: {stats.get('completed', 0)}/{stats.get('total', 0)} completed")
        if stats.get('processing', 0):
            print(f"  In Progress: {stats['processing']}")
        if stats.get('failed', 0):
            print(f"  Failed: {stats['failed']}")

    def start_production(self, priority: Optional[int] = None, max_concurrent: int = 3, test_mode: bool = False):
        """Start batch video production."""
        scripts = self.scripts
        if priority:
            scripts = [s for s in scripts if s.priority == priority]

        # Filter out completed
        pending = []
        for script in scripts:
            job = self.state.get_job(script.script_id)
            if not job or job.status in ["pending", "failed"]:
                pending.append(script)

        if not pending:
            print("No pending scripts to process!")
            return

        print(f"\nStarting production of {len(pending)} videos...")
        print(f"Avatar: {DEVON_CONFIG['avatar_name']} ({DEVON_CONFIG['avatar_id']})")
        print(f"Voice: {DEVON_CONFIG['voice_name']} ({DEVON_CONFIG['voice_id']})")
        print(f"Resolution: {DEVON_CONFIG['dimension']['width']}x{DEVON_CONFIG['dimension']['height']}")
        if test_mode:
            print("MODE: TEST (lower quality, faster)")
        print()

        queued_jobs = []

        # Submit videos up to max_concurrent
        for i, script in enumerate(pending[:max_concurrent]):
            print(f"[{i+1}/{len(pending)}] Submitting: {script.title}")

            result = self.client.generate_video(script, test_mode=test_mode)

            job = VideoJob(
                script_id=script.script_id,
                created_at=datetime.now().isoformat()
            )

            if result["success"]:
                job.heygen_video_id = result["video_id"]
                job.status = "processing"
                print(f"    Video ID: {result['video_id']}")
                queued_jobs.append(job)
            else:
                job.status = "failed"
                job.error = result["error"]
                print(f"    FAILED: {result['error']}")

            self.state.update_job(job)
            time.sleep(1)  # Rate limit

        if queued_jobs:
            print(f"\nSubmitted {len(queued_jobs)} videos for processing.")
            print("Use --status to check progress, or --resume to continue after completion.")

    def check_status(self):
        """Check status of all processing videos."""
        processing = [j for j in self.state.jobs.values() if j.status == "processing"]

        if not processing:
            print("No videos currently processing.")
            stats = self.state.get_stats()
            print(f"\nOverall: {stats.get('completed', 0)} completed, {stats.get('failed', 0)} failed")
            return

        print(f"\nChecking {len(processing)} processing videos...\n")

        for job in processing:
            if not job.heygen_video_id:
                continue

            result = self.client.check_status(job.heygen_video_id)

            if result["success"]:
                status = result["status"]
                print(f"{job.script_id}: {status}")

                if status == "completed":
                    job.status = "completed"
                    job.video_url = result["video_url"]
                    job.duration = result.get("duration")
                    job.completed_at = datetime.now().isoformat()

                    # Download video
                    output_path = OUTPUT_DIR / f"{job.script_id}.mp4"
                    print(f"  Downloading to {output_path}...")

                    if self.client.download_video(result["video_url"], output_path):
                        job.output_path = str(output_path)
                        print(f"  Downloaded! Duration: {job.duration}s")

                elif status == "failed":
                    job.status = "failed"
                    job.error = result.get("error", "Unknown error")
                    print(f"  FAILED: {job.error}")

                self.state.update_job(job)
            else:
                print(f"{job.script_id}: Error checking status - {result.get('error')}")

            time.sleep(0.5)

        stats = self.state.get_stats()
        print(f"\nStatus: {stats.get('completed', 0)} completed, {stats.get('processing', 0)} processing, {stats.get('failed', 0)} failed")

    def resume_production(self, priority: Optional[int] = None, max_concurrent: int = 3):
        """Resume production, submitting more videos if slots available."""
        # First check current processing videos
        self.check_status()

        processing_count = len([j for j in self.state.jobs.values() if j.status == "processing"])
        available_slots = max_concurrent - processing_count

        if available_slots <= 0:
            print(f"\nMax concurrent ({max_concurrent}) videos already processing. Wait for completion.")
            return

        # Find pending scripts
        scripts = self.scripts
        if priority:
            scripts = [s for s in scripts if s.priority == priority]

        pending = []
        for script in scripts:
            job = self.state.get_job(script.script_id)
            if not job or job.status == "pending":
                pending.append(script)

        if not pending:
            print("\nAll scripts have been submitted!")
            return

        print(f"\n{available_slots} slots available. Submitting more videos...")

        for script in pending[:available_slots]:
            print(f"Submitting: {script.title}")

            result = self.client.generate_video(script)

            job = VideoJob(
                script_id=script.script_id,
                created_at=datetime.now().isoformat()
            )

            if result["success"]:
                job.heygen_video_id = result["video_id"]
                job.status = "processing"
                print(f"  Video ID: {result['video_id']}")
            else:
                job.status = "failed"
                job.error = result["error"]
                print(f"  FAILED: {result['error']}")

            self.state.update_job(job)
            time.sleep(1)

# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Devon Video Production Manager")

    parser.add_argument('--list', action='store_true', help='List all scripts')
    parser.add_argument('--start', action='store_true', help='Start production')
    parser.add_argument('--status', action='store_true', help='Check status')
    parser.add_argument('--resume', action='store_true', help='Resume production')
    parser.add_argument('--priority', type=int, choices=[1, 2], help='Filter by priority')
    parser.add_argument('--max-concurrent', type=int, default=3, help='Max concurrent videos')
    parser.add_argument('--test', action='store_true', help='Test mode (faster, lower quality)')

    args = parser.parse_args()

    # Get API key
    api_key = os.getenv('HEYGEN_API_KEY')

    # Try loading from .env.video if not set
    if not api_key:
        env_file = SCRIPT_DIR / ".env.video"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith('HEYGEN_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    break

    if not api_key and not args.list:
        print("Error: HEYGEN_API_KEY not found in environment or .env.video")
        sys.exit(1)

    manager = ProductionManager(api_key or "")

    if args.list:
        manager.list_scripts(args.priority)
    elif args.start:
        manager.start_production(args.priority, args.max_concurrent, args.test)
    elif args.status:
        manager.check_status()
    elif args.resume:
        manager.resume_production(args.priority, args.max_concurrent)
    else:
        manager.list_scripts()

if __name__ == "__main__":
    main()
