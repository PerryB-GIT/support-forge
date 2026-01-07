#!/usr/bin/env python3
"""
Audio-Slides Compositor
=======================
Combines audio tracks with slide images to create final video output.

This compositor combines:
- Audio track (AAC/MP3 from Devon voiceover)
- Slide images (PNGs timed to the script)
- Parsed script JSON (with segment timing)

Output: Final MP4 video with slides synced to audio

Features:
1. Read parsed script JSON to get segment timings
2. For each segment, display the corresponding slide image
3. Use FFmpeg to create video from image sequence with proper durations
4. Support crossfade transitions between slides (0.3s default)
5. Handle cases where audio is longer/shorter than total slide duration
6. Output 1920x1080 @ 30fps

Usage:
    python audio-slides-compositor.py \\
        --audio path/to/audio.aac \\
        --slides path/to/slides/ \\
        --script path/to/parsed-script.json \\
        --output path/to/final.mp4

    python audio-slides-compositor.py --help

Requirements:
    - FFmpeg installed at C:\\ffmpeg\\bin\\ffmpeg.exe (or in PATH)
    - Python 3.8+
"""

import argparse
import json
import logging
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Callable

# ============================================================================
# Constants and Configuration
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "output"
DEFAULT_LOG_PATH = SCRIPT_DIR / "audio-slides-compositor.log"

# FFmpeg paths
FFMPEG_PATH = Path(r"C:\ffmpeg\bin\ffmpeg.exe")
FFPROBE_PATH = Path(r"C:\ffmpeg\bin\ffprobe.exe")

# Output specifications
OUTPUT_WIDTH = 1920
OUTPUT_HEIGHT = 1080
OUTPUT_FPS = 30
BACKGROUND_COLOR = "0x1E1B4B"  # Dark purple (matches video-compositor.py)

# Transition settings
DEFAULT_TRANSITION_DURATION = 0.3  # seconds

# ============================================================================
# Logging Setup
# ============================================================================

def setup_logging(log_path: Path, verbose: bool = False) -> logging.Logger:
    """Configure logging with file and console handlers."""
    logger = logging.getLogger("audio-slides-compositor")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # Clear any existing handlers
    logger.handlers.clear()

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
# Data Classes
# ============================================================================

@dataclass
class SlideSegment:
    """Represents a single slide segment with timing."""
    segment_id: int
    start_time: float
    end_time: float
    duration: float
    slide_path: Optional[Path] = None
    visual_cue: Optional[str] = None

    @property
    def has_slide(self) -> bool:
        """Check if slide file exists."""
        return self.slide_path is not None and self.slide_path.exists()


@dataclass
class CompositorConfig:
    """Configuration for the audio-slides compositor."""
    audio_path: Path
    slides_dir: Path
    script_path: Path
    output_path: Path
    transition_duration: float = DEFAULT_TRANSITION_DURATION
    verbose: bool = False
    temp_dir: Optional[Path] = None
    keep_temp: bool = False


# ============================================================================
# FFmpeg Wrapper
# ============================================================================

class FFmpegWrapper:
    """Wrapper for FFmpeg operations with progress reporting."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.ffmpeg_path = self._find_ffmpeg()
        self.ffprobe_path = self._find_ffprobe()

    def _find_ffmpeg(self) -> str:
        """Find FFmpeg executable."""
        # Check configured path first
        if FFMPEG_PATH.exists():
            return str(FFMPEG_PATH)

        # Check common locations
        common_paths = [
            r"C:\ffmpeg\bin\ffmpeg.exe",
            r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
            r"C:\ProgramData\chocolatey\bin\ffmpeg.exe",
            "ffmpeg.exe",
            "ffmpeg",
            "/usr/bin/ffmpeg",
            "/usr/local/bin/ffmpeg",
        ]

        for path in common_paths:
            if os.path.exists(path) or shutil.which(path):
                return path

        # Try to find via where/which
        try:
            result = subprocess.run(
                ["where", "ffmpeg"] if sys.platform == "win32" else ["which", "ffmpeg"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split('\n')[0]
        except Exception:
            pass

        return "ffmpeg"  # Hope it's in PATH

    def _find_ffprobe(self) -> str:
        """Find FFprobe executable."""
        # Check configured path first
        if FFPROBE_PATH.exists():
            return str(FFPROBE_PATH)

        # Check common locations
        common_paths = [
            r"C:\ffmpeg\bin\ffprobe.exe",
            r"C:\Program Files\ffmpeg\bin\ffprobe.exe",
            "ffprobe.exe",
            "ffprobe",
        ]

        for path in common_paths:
            if os.path.exists(path) or shutil.which(path):
                return path

        # Try deriving from ffmpeg path
        if self.ffmpeg_path and self.ffmpeg_path != "ffmpeg":
            ffprobe = self.ffmpeg_path.replace("ffmpeg", "ffprobe")
            if os.path.exists(ffprobe):
                return ffprobe

        return "ffprobe"

    def check_availability(self) -> tuple[bool, str]:
        """Check if FFmpeg is available and return version."""
        try:
            result = subprocess.run(
                [self.ffmpeg_path, "-version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                self.logger.info(f"FFmpeg found: {version_line}")
                return True, version_line
            return False, "FFmpeg returned error"
        except FileNotFoundError:
            return False, f"FFmpeg not found at {self.ffmpeg_path}"
        except subprocess.TimeoutExpired:
            return False, "FFmpeg check timed out"
        except Exception as e:
            return False, f"Error checking FFmpeg: {e}"

    def get_media_info(self, file_path: Path) -> dict[str, Any]:
        """Get media file information using ffprobe."""
        try:
            result = subprocess.run(
                [
                    self.ffprobe_path,
                    "-v", "quiet",
                    "-print_format", "json",
                    "-show_format",
                    "-show_streams",
                    str(file_path)
                ],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                return json.loads(result.stdout)
            self.logger.error(f"FFprobe error: {result.stderr}")
            return {}
        except Exception as e:
            self.logger.error(f"Error getting media info: {e}")
            return {}

    def get_duration(self, file_path: Path) -> float:
        """Get media file duration in seconds."""
        info = self.get_media_info(file_path)
        if info and "format" in info:
            return float(info["format"].get("duration", 0))
        return 0.0

    def run_ffmpeg(
        self,
        args: list[str],
        progress_callback: Optional[Callable[[str], None]] = None,
        timeout: int = 3600
    ) -> tuple[bool, str]:
        """Run FFmpeg with the given arguments."""
        cmd = [self.ffmpeg_path] + args
        self.logger.debug(f"Running: {' '.join(cmd)}")

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )

            # Capture stderr for progress (FFmpeg outputs progress to stderr)
            stderr_output = []
            for line in process.stderr:
                stderr_output.append(line)
                if progress_callback and "time=" in line:
                    progress_callback(line)
                elif "error" in line.lower() and "errors" not in line.lower():
                    self.logger.warning(line.strip())

            process.wait(timeout=timeout)

            if process.returncode == 0:
                return True, "Success"
            else:
                error_msg = ''.join(stderr_output[-20:])  # Last 20 lines
                return False, error_msg

        except subprocess.TimeoutExpired:
            process.kill()
            return False, "FFmpeg timed out"
        except Exception as e:
            return False, f"FFmpeg error: {e}"


# ============================================================================
# Script Parser
# ============================================================================

class ScriptParser:
    """Parses the parsed script JSON to extract segment timing."""

    def __init__(self, script_path: Path, logger: logging.Logger):
        self.script_path = script_path
        self.logger = logger
        self.segments: list[SlideSegment] = []
        self.total_duration: float = 0
        self.title: str = ""
        self._parse()

    def _parse(self):
        """Parse the script JSON file."""
        if not self.script_path.exists():
            self.logger.error(f"Script file not found: {self.script_path}")
            return

        try:
            with open(self.script_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.title = data.get("title", "Untitled")
            self.total_duration = data.get("total_duration_seconds", 0)

            # Handle segments from video-script-parser.py output format
            segments_data = data.get("segments", [])

            if not segments_data:
                self.logger.warning("No segments found in script JSON")
                return

            for seg in segments_data:
                segment_id = seg.get("segment_id", 0)
                start_time = float(seg.get("start_time", 0))
                end_time = float(seg.get("end_time", 0))
                duration = end_time - start_time

                segment = SlideSegment(
                    segment_id=segment_id,
                    start_time=start_time,
                    end_time=end_time,
                    duration=duration,
                    visual_cue=seg.get("visual_cue", "")
                )

                self.segments.append(segment)

            # Update total duration from segments if not specified
            if not self.total_duration and self.segments:
                self.total_duration = max(seg.end_time for seg in self.segments)

            self.logger.info(f"Parsed {len(self.segments)} segments from script")
            self.logger.info(f"Script duration: {self.total_duration:.2f}s ({self.total_duration/60:.1f} min)")

        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in script file: {e}")
        except Exception as e:
            self.logger.error(f"Error parsing script: {e}")


# ============================================================================
# Slide Manager
# ============================================================================

class SlideManager:
    """Manages slide images and matches them to segments."""

    SUPPORTED_FORMATS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

    def __init__(self, slides_dir: Path, logger: logging.Logger):
        self.slides_dir = slides_dir
        self.logger = logger
        self.slides: dict[int, Path] = {}
        self._scan_slides()

    def _scan_slides(self):
        """Scan slides directory and index files by segment number."""
        if not self.slides_dir.exists():
            self.logger.warning(f"Slides directory not found: {self.slides_dir}")
            return

        for file in self.slides_dir.iterdir():
            if not file.is_file():
                continue

            suffix = file.suffix.lower()
            if suffix not in self.SUPPORTED_FORMATS:
                continue

            # Extract segment number from filename
            # Expected formats: segment_001.png, segment_002.png, etc.
            stem = file.stem.lower()

            segment_num = None

            # Try various patterns
            import re

            # Pattern: segment_NNN or segment_NN or segment_N
            match = re.search(r'segment[_-]?(\d+)', stem)
            if match:
                segment_num = int(match.group(1))
            else:
                # Pattern: slide_NNN
                match = re.search(r'slide[_-]?(\d+)', stem)
                if match:
                    segment_num = int(match.group(1))
                else:
                    # Pattern: just numbers NNN
                    match = re.match(r'^(\d+)$', stem)
                    if match:
                        segment_num = int(match.group(1))

            if segment_num is not None:
                self.slides[segment_num] = file
                self.logger.debug(f"Found slide: segment {segment_num} -> {file.name}")

        self.logger.info(f"Indexed {len(self.slides)} slides from {self.slides_dir}")

    def get_slide(self, segment_id: int) -> Optional[Path]:
        """Get slide for a specific segment ID."""
        return self.slides.get(segment_id)

    def match_slides_to_segments(self, segments: list[SlideSegment]) -> list[SlideSegment]:
        """Match slide files to segments and update segment objects."""
        for segment in segments:
            slide_path = self.get_slide(segment.segment_id)
            if slide_path:
                segment.slide_path = slide_path
            else:
                self.logger.warning(f"No slide found for segment {segment.segment_id}")

        matched = sum(1 for s in segments if s.has_slide)
        self.logger.info(f"Matched {matched}/{len(segments)} segments with slides")

        return segments


# ============================================================================
# Audio-Slides Compositor
# ============================================================================

class AudioSlidesCompositor:
    """Main compositor that combines audio with timed slides."""

    def __init__(self, config: CompositorConfig, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.ffmpeg = FFmpegWrapper(logger)
        self.script_parser = ScriptParser(config.script_path, logger)
        self.slide_manager = SlideManager(config.slides_dir, logger)
        self.temp_dir = config.temp_dir or Path(tempfile.mkdtemp(prefix="audio_slides_"))
        self.audio_duration = 0.0
        self.total_progress = 0.0

    def validate_inputs(self) -> bool:
        """Validate all input files and configuration."""
        errors = []

        # Check FFmpeg
        available, msg = self.ffmpeg.check_availability()
        if not available:
            errors.append(f"FFmpeg: {msg}")

        # Check audio file
        if not self.config.audio_path.exists():
            errors.append(f"Audio file not found: {self.config.audio_path}")
        else:
            self.audio_duration = self.ffmpeg.get_duration(self.config.audio_path)
            if self.audio_duration == 0:
                errors.append("Could not read audio duration")
            else:
                self.logger.info(f"Audio duration: {self.audio_duration:.2f}s ({self.audio_duration/60:.1f} min)")

        # Check slides directory
        if not self.config.slides_dir.exists():
            errors.append(f"Slides directory not found: {self.config.slides_dir}")
        elif not self.slide_manager.slides:
            errors.append("No slide images found in slides directory")

        # Check script JSON
        if not self.config.script_path.exists():
            errors.append(f"Script JSON not found: {self.config.script_path}")
        elif not self.script_parser.segments:
            errors.append("No segments parsed from script JSON")

        # Report errors
        if errors:
            for error in errors:
                self.logger.error(error)
            return False

        return True

    def create_placeholder_image(self, output_path: Path, text: str = "Slide") -> bool:
        """Create a placeholder image with text for missing slides."""
        # Escape special characters for FFmpeg
        safe_text = text.replace("'", "").replace(":", " -").replace("\\", "")[:50]

        try:
            success, msg = self.ffmpeg.run_ffmpeg([
                "-y",
                "-f", "lavfi",
                "-i", f"color=c={BACKGROUND_COLOR}:s={OUTPUT_WIDTH}x{OUTPUT_HEIGHT}:d=1",
                "-vf", f"drawtext=text='{safe_text}':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2",
                "-frames:v", "1",
                str(output_path)
            ])
            return success and output_path.exists()
        except Exception as e:
            self.logger.error(f"Failed to create placeholder: {e}")
            return False

    def prepare_segment_video(self, segment: SlideSegment, index: int) -> Optional[Path]:
        """Create a video clip for a single segment from its slide image."""
        output_path = self.temp_dir / f"segment_{segment.segment_id:03d}.mp4"

        # Get slide path or create placeholder
        slide_path = segment.slide_path
        if not slide_path or not slide_path.exists():
            self.logger.warning(f"Creating placeholder for segment {segment.segment_id}")
            slide_path = self.temp_dir / f"placeholder_{segment.segment_id:03d}.png"
            text = segment.visual_cue[:40] if segment.visual_cue else f"Segment {segment.segment_id}"
            if not self.create_placeholder_image(slide_path, text):
                return None

        # Create video from image with exact duration
        success, msg = self.ffmpeg.run_ffmpeg([
            "-y",
            "-loop", "1",
            "-i", str(slide_path),
            "-t", str(segment.duration),
            "-vf", (
                f"scale={OUTPUT_WIDTH}:{OUTPUT_HEIGHT}:force_original_aspect_ratio=decrease,"
                f"pad={OUTPUT_WIDTH}:{OUTPUT_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color={BACKGROUND_COLOR},"
                f"setsar=1,format=yuv420p"
            ),
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            "-r", str(OUTPUT_FPS),
            "-pix_fmt", "yuv420p",
            str(output_path)
        ])

        if not success:
            self.logger.error(f"Failed to create segment {segment.segment_id} video: {msg}")
            return None

        return output_path

    def concatenate_segments_simple(self, segment_videos: list[Path]) -> Optional[Path]:
        """Concatenate segment videos without transitions (simple concat)."""
        if not segment_videos:
            return None

        if len(segment_videos) == 1:
            return segment_videos[0]

        output_path = self.temp_dir / "slides_concat.mp4"

        # Create concat file list
        concat_list = self.temp_dir / "concat_list.txt"
        with open(concat_list, 'w') as f:
            for video in segment_videos:
                # Use forward slashes for ffmpeg compatibility
                f.write(f"file '{video.as_posix()}'\n")

        success, msg = self.ffmpeg.run_ffmpeg([
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_list),
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            str(output_path)
        ])

        if not success:
            self.logger.error(f"Failed to concatenate segments: {msg}")
            return None

        return output_path

    def concatenate_segments_with_transitions(self, segment_videos: list[Path]) -> Optional[Path]:
        """Concatenate segment videos with crossfade transitions."""
        if not segment_videos:
            return None

        if len(segment_videos) == 1:
            return segment_videos[0]

        # For crossfade, we need to use xfade filter
        # This is complex with many segments, so we'll do it pairwise
        transition_dur = self.config.transition_duration

        self.logger.info(f"Applying {transition_dur}s crossfade transitions between {len(segment_videos)} segments")

        # Build complex filter graph for xfade
        # For n videos, we need n-1 xfade filters
        n = len(segment_videos)

        # Input labels
        inputs = []
        for i, video in enumerate(segment_videos):
            inputs.extend(["-i", str(video)])

        # Calculate offsets for xfade
        # Each xfade needs an offset which is the total duration up to that point minus transition time
        durations = []
        for video in segment_videos:
            dur = self.ffmpeg.get_duration(video)
            durations.append(dur)

        # Build filter complex
        filter_parts = []
        current_input = "[0:v]"

        for i in range(1, n):
            next_input = f"[{i}:v]"
            output_label = f"[v{i}]" if i < n - 1 else "[vout]"

            # Calculate offset: cumulative duration minus transition overlaps so far
            offset = sum(durations[:i]) - (transition_dur * (i))
            offset = max(0, offset)

            filter_parts.append(
                f"{current_input}{next_input}xfade=transition=fade:duration={transition_dur}:offset={offset:.3f}{output_label}"
            )

            current_input = output_label

        filter_complex = ";".join(filter_parts)

        output_path = self.temp_dir / "slides_transition.mp4"

        cmd = ["-y"] + inputs + [
            "-filter_complex", filter_complex,
            "-map", "[vout]",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-r", str(OUTPUT_FPS),
            str(output_path)
        ]

        success, msg = self.ffmpeg.run_ffmpeg(cmd)

        if not success:
            self.logger.warning(f"Transition concatenation failed, falling back to simple concat: {msg}")
            return self.concatenate_segments_simple(segment_videos)

        return output_path

    def adjust_video_duration(self, video_path: Path, target_duration: float) -> Optional[Path]:
        """Adjust video duration to match target (audio) duration."""
        video_duration = self.ffmpeg.get_duration(video_path)

        if abs(video_duration - target_duration) < 0.1:
            # Close enough, no adjustment needed
            return video_path

        self.logger.info(f"Adjusting video from {video_duration:.2f}s to {target_duration:.2f}s")

        output_path = self.temp_dir / "slides_adjusted.mp4"

        if video_duration < target_duration:
            # Video is shorter - extend by holding last frame
            extend_duration = target_duration - video_duration
            self.logger.info(f"Extending video by {extend_duration:.2f}s (holding last frame)")

            success, msg = self.ffmpeg.run_ffmpeg([
                "-y",
                "-i", str(video_path),
                "-vf", f"tpad=stop_mode=clone:stop_duration={extend_duration}",
                "-c:v", "libx264",
                "-preset", "medium",
                "-crf", "18",
                "-pix_fmt", "yuv420p",
                str(output_path)
            ])

        else:
            # Video is longer - trim to target duration
            self.logger.info(f"Trimming video to {target_duration:.2f}s")

            success, msg = self.ffmpeg.run_ffmpeg([
                "-y",
                "-i", str(video_path),
                "-t", str(target_duration),
                "-c:v", "libx264",
                "-preset", "medium",
                "-crf", "18",
                "-pix_fmt", "yuv420p",
                str(output_path)
            ])

        if not success:
            self.logger.error(f"Failed to adjust video duration: {msg}")
            return video_path  # Return original as fallback

        return output_path

    def combine_audio_video(self, video_path: Path) -> bool:
        """Combine the video track with audio to create final output."""
        self.logger.info("Combining audio and video tracks...")

        # Determine output codec based on audio format
        audio_suffix = self.config.audio_path.suffix.lower()

        success, msg = self.ffmpeg.run_ffmpeg([
            "-y",
            "-i", str(video_path),
            "-i", str(self.config.audio_path),
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            "-movflags", "+faststart",
            str(self.config.output_path)
        ], progress_callback=self._progress_callback)

        if success:
            self.logger.info(f"Final video created: {self.config.output_path}")
            return True
        else:
            self.logger.error(f"Failed to combine audio/video: {msg}")
            return False

    def _progress_callback(self, line: str):
        """Handle FFmpeg progress output."""
        import re
        match = re.search(r'time=(\d+):(\d+):(\d+\.?\d*)', line)
        if match:
            hours, minutes, seconds = match.groups()
            current = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
            total = self.audio_duration or 60
            percent = min(100, (current / total) * 100)
            print(f"\rProgress: {percent:.1f}% ({current:.1f}s / {total:.1f}s)", end="", flush=True)

    def run(self) -> bool:
        """Execute the full composition pipeline."""
        self.logger.info("=" * 60)
        self.logger.info("Audio-Slides Compositor Starting")
        self.logger.info("=" * 60)

        # Validate inputs
        self.logger.info("Validating inputs...")
        if not self.validate_inputs():
            return False

        # Match slides to segments
        self.logger.info("Matching slides to segments...")
        segments = self.slide_manager.match_slides_to_segments(self.script_parser.segments)

        if not segments:
            self.logger.error("No segments to process")
            return False

        # Prepare individual segment videos
        self.logger.info(f"Creating {len(segments)} segment videos...")
        segment_videos = []

        for i, segment in enumerate(segments):
            print(f"\rProcessing segment {i+1}/{len(segments)}: {segment.segment_id}", end="", flush=True)
            video_path = self.prepare_segment_video(segment, i)
            if video_path:
                segment_videos.append(video_path)
            else:
                self.logger.warning(f"Skipping segment {segment.segment_id} due to error")

        print()  # New line after progress

        if not segment_videos:
            self.logger.error("No segment videos created")
            return False

        self.logger.info(f"Created {len(segment_videos)} segment videos")

        # Concatenate segments with transitions
        self.logger.info("Concatenating segments...")
        if self.config.transition_duration > 0:
            slides_video = self.concatenate_segments_with_transitions(segment_videos)
        else:
            slides_video = self.concatenate_segments_simple(segment_videos)

        if slides_video is None:
            self.logger.error("Failed to concatenate segments")
            return False

        # Adjust video duration to match audio
        self.logger.info("Adjusting video duration to match audio...")
        slides_video = self.adjust_video_duration(slides_video, self.audio_duration)

        if slides_video is None:
            self.logger.error("Failed to adjust video duration")
            return False

        # Combine with audio
        self.logger.info("Combining with audio track...")
        success = self.combine_audio_video(slides_video)

        # Cleanup temp files
        if success and not self.config.keep_temp:
            self.logger.info("Cleaning up temporary files...")
            try:
                shutil.rmtree(self.temp_dir, ignore_errors=True)
            except Exception as e:
                self.logger.warning(f"Failed to cleanup temp dir: {e}")

        print()  # New line after progress
        self.logger.info("=" * 60)

        if success:
            file_size = self.config.output_path.stat().st_size / (1024 * 1024)
            duration = self.ffmpeg.get_duration(self.config.output_path)
            self.logger.info(f"Composition complete!")
            self.logger.info(f"Output: {self.config.output_path}")
            self.logger.info(f"Duration: {duration:.2f}s ({duration/60:.1f} min)")
            self.logger.info(f"File size: {file_size:.1f} MB")
        else:
            self.logger.error("Composition failed")

        self.logger.info("=" * 60)

        return success


# ============================================================================
# CLI
# ============================================================================

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Combine audio tracks with timed slide images to create video",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic composition
    python audio-slides-compositor.py \\
        --audio voiceover.aac \\
        --slides ./slides/ \\
        --script parsed-script.json \\
        --output final.mp4

    # With custom transition duration
    python audio-slides-compositor.py \\
        --audio voiceover.mp3 \\
        --slides ./slides/ \\
        --script script.json \\
        --output final.mp4 \\
        --transition 0.5

    # No transitions (hard cuts)
    python audio-slides-compositor.py \\
        --audio audio.aac \\
        --slides ./slides/ \\
        --script script.json \\
        --output final.mp4 \\
        --transition 0

    # Verbose mode with temp file retention
    python audio-slides-compositor.py \\
        --audio audio.aac \\
        --slides ./slides/ \\
        --script script.json \\
        --output final.mp4 \\
        -v --keep-temp

Slide Naming Convention:
    Slides should be named: segment_001.png, segment_002.png, etc.
    The number corresponds to the segment_id in the parsed script JSON.

Supported Audio Formats:
    AAC, MP3, WAV, M4A, FLAC, OGG

Supported Image Formats:
    PNG, JPG, JPEG, WEBP, BMP
        """
    )

    # Required arguments
    parser.add_argument(
        "--audio",
        type=Path,
        required=True,
        help="Path to audio file (AAC, MP3, WAV, etc.)"
    )

    parser.add_argument(
        "--slides",
        type=Path,
        required=True,
        help="Path to directory containing slide images (segment_001.png, etc.)"
    )

    parser.add_argument(
        "--script",
        type=Path,
        required=True,
        help="Path to parsed script JSON with segment timings"
    )

    parser.add_argument(
        "--output", "-o",
        type=Path,
        required=True,
        help="Output video path (MP4)"
    )

    # Optional arguments
    parser.add_argument(
        "--transition",
        type=float,
        default=DEFAULT_TRANSITION_DURATION,
        help=f"Crossfade transition duration in seconds (default: {DEFAULT_TRANSITION_DURATION}s, 0 for hard cuts)"
    )

    parser.add_argument(
        "--temp-dir",
        type=Path,
        help="Custom temporary directory for intermediate files"
    )

    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep temporary files after completion (useful for debugging)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    parser.add_argument(
        "--check-ffmpeg",
        action="store_true",
        help="Check FFmpeg availability and exit"
    )

    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()

    # Setup logging
    log_path = DEFAULT_LOG_PATH
    logger = setup_logging(log_path, args.verbose)

    # FFmpeg check mode
    if args.check_ffmpeg:
        ffmpeg = FFmpegWrapper(logger)
        available, version = ffmpeg.check_availability()
        if available:
            print(f"FFmpeg is available: {version}")
            print(f"FFmpeg path: {ffmpeg.ffmpeg_path}")
            print(f"FFprobe path: {ffmpeg.ffprobe_path}")
            sys.exit(0)
        else:
            print(f"FFmpeg not available: {version}")
            print("\nExpected FFmpeg at: C:\\ffmpeg\\bin\\ffmpeg.exe")
            print("\nTo install FFmpeg:")
            print("  1. Download from https://ffmpeg.org/download.html")
            print("  2. Extract to C:\\ffmpeg\\")
            print("  3. Ensure C:\\ffmpeg\\bin\\ contains ffmpeg.exe and ffprobe.exe")
            sys.exit(1)

    # Ensure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)

    # Create compositor config
    config = CompositorConfig(
        audio_path=args.audio,
        slides_dir=args.slides,
        script_path=args.script,
        output_path=args.output,
        transition_duration=args.transition,
        verbose=args.verbose,
        temp_dir=args.temp_dir,
        keep_temp=args.keep_temp
    )

    # Run compositor
    compositor = AudioSlidesCompositor(config, logger)
    success = compositor.run()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
