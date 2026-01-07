#!/usr/bin/env python3
"""
Video Production Orchestrator
=============================
Master script for orchestrating video production workflow.
Manages video generation queue, routes to appropriate generators,
and tracks production status.

Usage:
    python video-orchestrator.py status                    # Show production status
    python video-orchestrator.py generate <script_id>      # Generate specific video
    python video-orchestrator.py batch --type avatar       # Batch generate avatar videos
    python video-orchestrator.py export                    # Export status report
    python video-orchestrator.py init                      # Initialize config and state files
"""

import argparse
import json
import logging
import os
import re
import sys
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Optional

import requests

# ============================================================================
# Constants and Configuration
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
DEFAULT_CONFIG_PATH = SCRIPT_DIR / "config.json"
DEFAULT_STATE_PATH = SCRIPT_DIR / "video-state.json"
DEFAULT_QUEUE_PATH = SCRIPT_DIR / "video-queue.md"
DEFAULT_LOG_PATH = SCRIPT_DIR / "video-orchestrator.log"

# ============================================================================
# Enums
# ============================================================================

class VideoType(Enum):
    AVATAR = "avatar"
    SCREEN_CAPTURE = "screen_capture"
    HYBRID = "hybrid"
    UNKNOWN = "unknown"


class VideoStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    MANUAL_REQUIRED = "manual_required"
    SKIPPED = "skipped"


# ============================================================================
# Logging Setup
# ============================================================================

def setup_logging(log_path: Path, verbose: bool = False) -> logging.Logger:
    """Configure logging with file and console handlers."""
    logger = logging.getLogger("video-orchestrator")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_formatter = logging.Formatter("%(levelname)-8s | %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# ============================================================================
# Configuration Management
# ============================================================================

class Config:
    """Configuration manager for the orchestrator."""

    DEFAULT_CONFIG = {
        "heygen": {
            "api_key": "",
            "api_base": "https://api.heygen.com/v2",
            "default_avatar_id": "",
            "default_voice_id": "",
            "video_dimensions": {"width": 1920, "height": 1080}
        },
        "paths": {
            "queue_file": str(DEFAULT_QUEUE_PATH),
            "state_file": str(DEFAULT_STATE_PATH),
            "output_dir": str(SCRIPT_DIR / "output"),
            "assets_dir": str(SCRIPT_DIR / "assets")
        },
        "settings": {
            "dry_run": False,
            "auto_retry": True,
            "max_retries": 3,
            "retry_delay_seconds": 60,
            "polling_interval_seconds": 30
        },
        "notifications": {
            "enabled": False,
            "webhook_url": ""
        }
    }

    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.data = self._load_config()

    def _load_config(self) -> dict:
        """Load configuration from file or create default."""
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                # Merge with defaults to ensure all keys exist
                return self._deep_merge(self.DEFAULT_CONFIG.copy(), loaded)
        return self.DEFAULT_CONFIG.copy()

    def _deep_merge(self, base: dict, override: dict) -> dict:
        """Deep merge two dictionaries."""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result

    def save(self) -> None:
        """Save current configuration to file."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def get(self, *keys: str, default: Any = None) -> Any:
        """Get nested configuration value."""
        value = self.data
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value


# ============================================================================
# State Management
# ============================================================================

class StateManager:
    """Manages production state tracking."""

    def __init__(self, state_path: Path):
        self.state_path = state_path
        self.state = self._load_state()

    def _load_state(self) -> dict:
        """Load state from file or create empty state."""
        if self.state_path.exists():
            with open(self.state_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "videos": {},
            "last_updated": None,
            "statistics": {
                "total_generated": 0,
                "total_failed": 0,
                "total_manual": 0
            }
        }

    def save(self) -> None:
        """Save state to file."""
        self.state["last_updated"] = datetime.now().isoformat()
        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, default=str)

    def get_video(self, script_id: str) -> Optional[dict]:
        """Get video state by script ID."""
        return self.state["videos"].get(script_id)

    def update_video(self, script_id: str, updates: dict) -> None:
        """Update video state."""
        if script_id not in self.state["videos"]:
            self.state["videos"][script_id] = {
                "script_id": script_id,
                "created_at": datetime.now().isoformat(),
                "status": VideoStatus.PENDING.value,
                "attempts": 0
            }

        self.state["videos"][script_id].update(updates)
        self.state["videos"][script_id]["updated_at"] = datetime.now().isoformat()
        self.save()

    def get_all_videos(self) -> dict:
        """Get all video states."""
        return self.state["videos"]

    def get_videos_by_status(self, status: VideoStatus) -> list:
        """Get videos filtered by status."""
        return [
            v for v in self.state["videos"].values()
            if v.get("status") == status.value
        ]

    def get_videos_by_type(self, video_type: VideoType) -> list:
        """Get videos filtered by type."""
        return [
            v for v in self.state["videos"].values()
            if v.get("video_type") == video_type.value
        ]

    def update_statistics(self, stat_key: str, increment: int = 1) -> None:
        """Update statistics counter."""
        if stat_key in self.state["statistics"]:
            self.state["statistics"][stat_key] += increment
            self.save()


# ============================================================================
# Queue Parser
# ============================================================================

class QueueParser:
    """Parse video production queue from markdown file."""

    def __init__(self, queue_path: Path):
        self.queue_path = queue_path

    def parse(self) -> list:
        """Parse the queue file and return list of video scripts."""
        if not self.queue_path.exists():
            return []

        with open(self.queue_path, "r", encoding="utf-8") as f:
            content = f.read()

        scripts = []
        current_script = None

        # Pattern to match script headers like "## Script: intro-001" or "### [avatar] Welcome Video"
        header_pattern = re.compile(
            r'^#{2,3}\s+(?:\[(\w+)\]\s+)?(?:Script:\s*)?(.+?)(?:\s*\((\w+)\))?$',
            re.MULTILINE
        )

        # Split content by headers
        parts = header_pattern.split(content)

        # Process parts (groups of 4: pre-match, type, title, inline-type, content)
        i = 1  # Skip first part (content before first header)
        while i < len(parts):
            if i + 3 < len(parts):
                video_type = parts[i] or parts[i + 2] or "unknown"
                title = parts[i + 1].strip()

                # Generate script ID from title
                script_id = self._generate_id(title)

                # Get content until next header
                content_end = i + 4
                script_content = parts[i + 3] if i + 3 < len(parts) else ""

                scripts.append({
                    "script_id": script_id,
                    "title": title,
                    "video_type": self._parse_video_type(video_type),
                    "content": script_content.strip(),
                    "raw_type": video_type
                })

            i += 4

        # Fallback: simple parsing if complex parsing returns nothing
        if not scripts:
            scripts = self._simple_parse(content)

        return scripts

    def _simple_parse(self, content: str) -> list:
        """Simple fallback parser for basic markdown structure."""
        scripts = []
        lines = content.split("\n")
        current_script = None
        current_content = []

        for line in lines:
            # Check for header
            if line.startswith("## ") or line.startswith("### "):
                # Save previous script
                if current_script:
                    current_script["content"] = "\n".join(current_content).strip()
                    scripts.append(current_script)

                # Parse new header
                header = line.lstrip("#").strip()
                video_type = "unknown"

                # Check for type markers
                if "[avatar]" in header.lower():
                    video_type = "avatar"
                    header = header.replace("[avatar]", "").replace("[Avatar]", "").strip()
                elif "[screen" in header.lower():
                    video_type = "screen_capture"
                    header = re.sub(r'\[screen[^\]]*\]', '', header, flags=re.IGNORECASE).strip()
                elif "[hybrid]" in header.lower():
                    video_type = "hybrid"
                    header = header.replace("[hybrid]", "").replace("[Hybrid]", "").strip()

                current_script = {
                    "script_id": self._generate_id(header),
                    "title": header,
                    "video_type": video_type,
                    "raw_type": video_type
                }
                current_content = []
            elif current_script:
                current_content.append(line)

        # Save last script
        if current_script:
            current_script["content"] = "\n".join(current_content).strip()
            scripts.append(current_script)

        return scripts

    def _generate_id(self, title: str) -> str:
        """Generate a URL-safe ID from title."""
        # Remove special characters and convert to lowercase
        id_str = re.sub(r'[^\w\s-]', '', title.lower())
        # Replace spaces with hyphens
        id_str = re.sub(r'[\s]+', '-', id_str)
        # Remove consecutive hyphens
        id_str = re.sub(r'-+', '-', id_str)
        return id_str.strip('-')

    def _parse_video_type(self, type_str: str) -> str:
        """Parse video type string to enum value."""
        type_lower = type_str.lower()
        if "avatar" in type_lower:
            return VideoType.AVATAR.value
        elif "screen" in type_lower:
            return VideoType.SCREEN_CAPTURE.value
        elif "hybrid" in type_lower:
            return VideoType.HYBRID.value
        return VideoType.UNKNOWN.value


# ============================================================================
# HeyGen Generator
# ============================================================================

class HeyGenGenerator:
    """Generate videos using HeyGen API."""

    def __init__(self, config: Config, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.api_key = config.get("heygen", "api_key")
        self.api_base = config.get("heygen", "api_base")

    def _get_headers(self) -> dict:
        """Get API request headers."""
        return {
            "X-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def create_video(self, script: dict, dry_run: bool = False) -> dict:
        """Create a video from script."""
        if not self.api_key:
            return {
                "success": False,
                "error": "HeyGen API key not configured"
            }

        if dry_run:
            self.logger.info(f"[DRY RUN] Would create video: {script['title']}")
            return {
                "success": True,
                "dry_run": True,
                "video_id": f"dry-run-{script['script_id']}"
            }

        try:
            payload = self._build_payload(script)

            response = requests.post(
                f"{self.api_base}/video/generate",
                headers=self._get_headers(),
                json=payload,
                timeout=60
            )

            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "video_id": data.get("data", {}).get("video_id"),
                    "response": data
                }
            else:
                return {
                    "success": False,
                    "error": f"API error: {response.status_code}",
                    "response": response.text
                }

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": f"Request failed: {str(e)}"
            }

    def _build_payload(self, script: dict) -> dict:
        """Build HeyGen API payload from script."""
        dimensions = self.config.get("heygen", "video_dimensions")

        return {
            "video_inputs": [{
                "character": {
                    "type": "avatar",
                    "avatar_id": self.config.get("heygen", "default_avatar_id"),
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": script.get("content", ""),
                    "voice_id": self.config.get("heygen", "default_voice_id")
                }
            }],
            "dimension": dimensions,
            "title": script.get("title", "Untitled")
        }

    def check_status(self, video_id: str) -> dict:
        """Check video generation status."""
        if not self.api_key:
            return {"success": False, "error": "API key not configured"}

        try:
            response = requests.get(
                f"{self.api_base}/video_status.get",
                headers=self._get_headers(),
                params={"video_id": video_id},
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "status": data.get("data", {}).get("status"),
                    "video_url": data.get("data", {}).get("video_url"),
                    "response": data
                }
            else:
                return {
                    "success": False,
                    "error": f"API error: {response.status_code}"
                }

        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}


# ============================================================================
# Video Orchestrator
# ============================================================================

class VideoOrchestrator:
    """Main orchestrator for video production."""

    def __init__(self, config_path: Path = DEFAULT_CONFIG_PATH, verbose: bool = False):
        self.config = Config(config_path)
        self.logger = setup_logging(
            Path(self.config.get("paths", "log_file", default=str(DEFAULT_LOG_PATH))),
            verbose
        )

        state_path = Path(self.config.get("paths", "state_file", default=str(DEFAULT_STATE_PATH)))
        self.state = StateManager(state_path)

        queue_path = Path(self.config.get("paths", "queue_file", default=str(DEFAULT_QUEUE_PATH)))
        self.queue_parser = QueueParser(queue_path)

        self.heygen = HeyGenGenerator(self.config, self.logger)

        self.dry_run = self.config.get("settings", "dry_run", default=False)

    def sync_queue(self) -> None:
        """Sync queue file with state."""
        scripts = self.queue_parser.parse()

        for script in scripts:
            existing = self.state.get_video(script["script_id"])
            if not existing:
                self.state.update_video(script["script_id"], {
                    "title": script["title"],
                    "video_type": script["video_type"],
                    "status": VideoStatus.PENDING.value
                })
                self.logger.info(f"Added to queue: {script['title']} ({script['video_type']})")

    def determine_video_type(self, script: dict) -> VideoType:
        """Determine the type of video based on script content and metadata."""
        video_type = script.get("video_type", "unknown")

        if video_type == VideoType.AVATAR.value:
            return VideoType.AVATAR
        elif video_type == VideoType.SCREEN_CAPTURE.value:
            return VideoType.SCREEN_CAPTURE
        elif video_type == VideoType.HYBRID.value:
            return VideoType.HYBRID

        # Auto-detect from content
        content = script.get("content", "").lower()
        if "screen" in content or "demo" in content or "walkthrough" in content:
            return VideoType.SCREEN_CAPTURE

        return VideoType.AVATAR

    def generate_video(self, script_id: str, dry_run: Optional[bool] = None) -> dict:
        """Generate a single video by script ID."""
        if dry_run is None:
            dry_run = self.dry_run

        # Get script from queue
        scripts = self.queue_parser.parse()
        script = next((s for s in scripts if s["script_id"] == script_id), None)

        if not script:
            self.logger.error(f"Script not found: {script_id}")
            return {"success": False, "error": "Script not found"}

        video_type = self.determine_video_type(script)
        self.logger.info(f"Processing: {script['title']} (type: {video_type.value})")

        # Update state
        self.state.update_video(script_id, {
            "status": VideoStatus.IN_PROGRESS.value,
            "video_type": video_type.value,
            "attempts": (self.state.get_video(script_id) or {}).get("attempts", 0) + 1
        })

        # Route to appropriate generator
        if video_type == VideoType.AVATAR:
            result = self._generate_avatar_video(script, dry_run)
        elif video_type == VideoType.SCREEN_CAPTURE:
            result = self._flag_for_manual(script, "Screen capture requires manual recording")
        elif video_type == VideoType.HYBRID:
            result = self._flag_for_manual(script, "Hybrid videos require manual composition")
        else:
            result = self._flag_for_manual(script, "Unknown video type")

        # Update state based on result
        if result.get("success"):
            status = VideoStatus.COMPLETED if not result.get("manual_required") else VideoStatus.MANUAL_REQUIRED
            self.state.update_video(script_id, {
                "status": status.value,
                "video_id": result.get("video_id"),
                "video_url": result.get("video_url"),
                "completed_at": datetime.now().isoformat() if status == VideoStatus.COMPLETED else None
            })
            if status == VideoStatus.COMPLETED:
                self.state.update_statistics("total_generated")
            else:
                self.state.update_statistics("total_manual")
        else:
            self.state.update_video(script_id, {
                "status": VideoStatus.FAILED.value,
                "error": result.get("error")
            })
            self.state.update_statistics("total_failed")

        return result

    def _generate_avatar_video(self, script: dict, dry_run: bool) -> dict:
        """Generate avatar video using HeyGen."""
        self.logger.info(f"Generating avatar video: {script['title']}")
        result = self.heygen.create_video(script, dry_run)

        if result.get("success"):
            self.logger.info(f"Video creation initiated: {result.get('video_id')}")
        else:
            self.logger.error(f"Video creation failed: {result.get('error')}")

        return result

    def _flag_for_manual(self, script: dict, reason: str) -> dict:
        """Flag video for manual processing."""
        self.logger.info(f"Flagged for manual: {script['title']} - {reason}")
        return {
            "success": True,
            "manual_required": True,
            "reason": reason,
            "script_id": script["script_id"]
        }

    def batch_generate(self, video_type: Optional[str] = None, dry_run: Optional[bool] = None) -> dict:
        """Batch generate videos by type."""
        self.sync_queue()

        scripts = self.queue_parser.parse()
        results = {"generated": [], "failed": [], "skipped": []}

        for script in scripts:
            # Filter by type if specified
            if video_type:
                script_type = self.determine_video_type(script)
                if script_type.value != video_type:
                    continue

            # Skip if already completed
            existing = self.state.get_video(script["script_id"])
            if existing and existing.get("status") == VideoStatus.COMPLETED.value:
                results["skipped"].append(script["script_id"])
                self.logger.info(f"Skipping completed: {script['title']}")
                continue

            result = self.generate_video(script["script_id"], dry_run)

            if result.get("success"):
                results["generated"].append(script["script_id"])
            else:
                results["failed"].append({
                    "script_id": script["script_id"],
                    "error": result.get("error")
                })

        return results

    def get_status(self) -> dict:
        """Get production status summary."""
        self.sync_queue()

        videos = self.state.get_all_videos()

        summary = {
            "total": len(videos),
            "by_status": {},
            "by_type": {},
            "statistics": self.state.state.get("statistics", {}),
            "last_updated": self.state.state.get("last_updated")
        }

        for status in VideoStatus:
            count = len([v for v in videos.values() if v.get("status") == status.value])
            if count > 0:
                summary["by_status"][status.value] = count

        for vtype in VideoType:
            count = len([v for v in videos.values() if v.get("video_type") == vtype.value])
            if count > 0:
                summary["by_type"][vtype.value] = count

        return summary

    def export_report(self, output_path: Optional[Path] = None) -> str:
        """Export detailed status report."""
        self.sync_queue()

        videos = self.state.get_all_videos()
        status = self.get_status()

        report_lines = [
            "# Video Production Status Report",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            f"- Total Videos: {status['total']}",
            ""
        ]

        # Status breakdown
        report_lines.append("### By Status")
        for stat, count in status.get("by_status", {}).items():
            report_lines.append(f"- {stat}: {count}")

        report_lines.append("")
        report_lines.append("### By Type")
        for vtype, count in status.get("by_type", {}).items():
            report_lines.append(f"- {vtype}: {count}")

        # Detailed list
        report_lines.extend(["", "## Video Details", ""])

        for script_id, video in sorted(videos.items(), key=lambda x: x[1].get("title", "")):
            status_emoji = {
                "completed": "[DONE]",
                "in_progress": "[PROG]",
                "pending": "[PEND]",
                "failed": "[FAIL]",
                "manual_required": "[MANUAL]",
                "skipped": "[SKIP]"
            }.get(video.get("status", ""), "[????]")

            report_lines.append(f"### {status_emoji} {video.get('title', script_id)}")
            report_lines.append(f"- ID: `{script_id}`")
            report_lines.append(f"- Type: {video.get('video_type', 'unknown')}")
            report_lines.append(f"- Status: {video.get('status', 'unknown')}")

            if video.get("video_url"):
                report_lines.append(f"- URL: {video['video_url']}")
            if video.get("error"):
                report_lines.append(f"- Error: {video['error']}")
            if video.get("completed_at"):
                report_lines.append(f"- Completed: {video['completed_at']}")

            report_lines.append("")

        report = "\n".join(report_lines)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)

        return report

    def init_config(self) -> None:
        """Initialize configuration files."""
        # Save default config
        self.config.save()
        self.logger.info(f"Config saved to: {self.config.config_path}")

        # Create directories
        output_dir = Path(self.config.get("paths", "output_dir"))
        assets_dir = Path(self.config.get("paths", "assets_dir"))

        output_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info(f"Created directories: {output_dir}, {assets_dir}")

        # Create sample queue file if it doesn't exist
        queue_path = Path(self.config.get("paths", "queue_file"))
        if not queue_path.exists():
            sample_queue = """# Video Production Queue

## [avatar] Welcome to Support Forge
Welcome to Support Forge! In this video, I'll show you how our platform
helps IT professionals manage support tickets more efficiently.

## [screen_capture] Dashboard Overview
A walkthrough of the main dashboard, showing key features and navigation.

## [hybrid] Getting Started Tutorial
Combines avatar introduction with screen recordings of the setup process.

## [avatar] Feature Spotlight: Ticket Management
Deep dive into our ticket management system with AI-powered categorization.
"""
            with open(queue_path, "w", encoding="utf-8") as f:
                f.write(sample_queue)
            self.logger.info(f"Created sample queue file: {queue_path}")


# ============================================================================
# CLI Interface
# ============================================================================

def create_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Video Production Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s init                          Initialize config and directories
  %(prog)s status                         Show production status
  %(prog)s generate welcome-video         Generate specific video
  %(prog)s batch --type avatar            Generate all avatar videos
  %(prog)s batch --dry-run                Test batch without generating
  %(prog)s export -o report.md            Export status report
        """
    )

    parser.add_argument(
        "-c", "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to config file"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without making API calls"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # init command
    subparsers.add_parser("init", help="Initialize configuration files")

    # status command
    subparsers.add_parser("status", help="Show production status")

    # generate command
    gen_parser = subparsers.add_parser("generate", help="Generate specific video")
    gen_parser.add_argument("script_id", help="Script ID to generate")

    # batch command
    batch_parser = subparsers.add_parser("batch", help="Batch generate videos")
    batch_parser.add_argument(
        "--type",
        choices=["avatar", "screen_capture", "hybrid"],
        help="Filter by video type"
    )

    # export command
    export_parser = subparsers.add_parser("export", help="Export status report")
    export_parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output file path"
    )

    return parser


def format_status(status: dict) -> str:
    """Format status for console output."""
    lines = [
        "\n========================================",
        "    VIDEO PRODUCTION STATUS",
        "========================================\n",
        f"Total Videos: {status['total']}",
        ""
    ]

    if status.get("by_status"):
        lines.append("By Status:")
        for stat, count in status["by_status"].items():
            icon = {
                "completed": "[OK]",
                "in_progress": "[..]",
                "pending": "[  ]",
                "failed": "[!!]",
                "manual_required": "[??]"
            }.get(stat, "    ")
            lines.append(f"  {icon} {stat}: {count}")

    if status.get("by_type"):
        lines.append("\nBy Type:")
        for vtype, count in status["by_type"].items():
            lines.append(f"  - {vtype}: {count}")

    if status.get("statistics"):
        lines.append("\nStatistics:")
        for key, value in status["statistics"].items():
            lines.append(f"  - {key}: {value}")

    if status.get("last_updated"):
        lines.append(f"\nLast Updated: {status['last_updated']}")

    lines.append("\n========================================\n")

    return "\n".join(lines)


def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    # Initialize orchestrator
    orchestrator = VideoOrchestrator(
        config_path=args.config,
        verbose=args.verbose
    )

    if args.dry_run:
        orchestrator.dry_run = True
        orchestrator.logger.info("Running in dry-run mode")

    try:
        if args.command == "init":
            orchestrator.init_config()
            print("Configuration initialized successfully!")
            return 0

        elif args.command == "status":
            status = orchestrator.get_status()
            print(format_status(status))
            return 0

        elif args.command == "generate":
            result = orchestrator.generate_video(args.script_id)
            if result.get("success"):
                print(f"Video generation initiated: {args.script_id}")
                if result.get("manual_required"):
                    print(f"Note: Manual processing required - {result.get('reason')}")
                return 0
            else:
                print(f"Failed: {result.get('error')}")
                return 1

        elif args.command == "batch":
            result = orchestrator.batch_generate(
                video_type=args.type,
                dry_run=args.dry_run
            )
            print(f"\nBatch Generation Results:")
            print(f"  Generated: {len(result['generated'])}")
            print(f"  Failed: {len(result['failed'])}")
            print(f"  Skipped: {len(result['skipped'])}")

            if result['failed']:
                print("\nFailed videos:")
                for fail in result['failed']:
                    print(f"  - {fail['script_id']}: {fail.get('error', 'Unknown error')}")

            return 0 if not result['failed'] else 1

        elif args.command == "export":
            output_path = args.output or SCRIPT_DIR / f"video-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
            report = orchestrator.export_report(output_path)
            print(f"Report exported to: {output_path}")
            return 0

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return 130
    except Exception as e:
        orchestrator.logger.exception("Unexpected error")
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
