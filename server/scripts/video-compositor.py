#!/usr/bin/env python3
"""
Video Compositor
================
Composites Devon avatar videos with visual assets for final video production.

Combines:
- Devon talking head video (HeyGen avatar, 720p)
- Visual assets (images/videos from asset generator)
- Timing information from parsed script JSON

Output:
- Professional 1080p video with picture-in-picture layout
- Main area for visuals, Devon PiP in corner
- Smooth transitions and lower third overlays

Usage:
    python video-compositor.py --devon devon.mp4 --assets ./assets/ --script parsed.json --output final.mp4
    python video-compositor.py --preview                    # Generate preview frames only
    python video-compositor.py --pip-position bottom-right  # Change PiP position
    python video-compositor.py --pip-size medium            # Change PiP size

Requirements:
    - FFmpeg installed and accessible via command line
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
from enum import Enum
from pathlib import Path
from typing import Any, Optional

# ============================================================================
# Constants and Configuration
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "output"
DEFAULT_LOG_PATH = SCRIPT_DIR / "video-compositor.log"

# Output specifications
OUTPUT_WIDTH = 1920
OUTPUT_HEIGHT = 1080
VISUAL_HEIGHT = 864  # 80% of 1080
PIP_PADDING = 20
BACKGROUND_COLOR = "0x1E1B4B"  # Dark purple (BGR for FFmpeg)
TRANSITION_DURATION = 0.5  # seconds

# PiP size presets (width, height)
PIP_SIZES = {
    "small": (288, 162),
    "medium": (384, 216),
    "large": (480, 270),
}

# PiP position presets (returns x, y based on size)
def get_pip_position(position: str, pip_width: int, pip_height: int) -> tuple[int, int]:
    """Calculate PiP position based on preset name."""
    positions = {
        "bottom-right": (OUTPUT_WIDTH - pip_width - PIP_PADDING, OUTPUT_HEIGHT - pip_height - PIP_PADDING),
        "bottom-left": (PIP_PADDING, OUTPUT_HEIGHT - pip_height - PIP_PADDING),
        "top-right": (OUTPUT_WIDTH - pip_width - PIP_PADDING, PIP_PADDING),
        "top-left": (PIP_PADDING, PIP_PADDING),
    }
    return positions.get(position, positions["bottom-right"])


# ============================================================================
# Logging Setup
# ============================================================================

def setup_logging(log_path: Path, verbose: bool = False) -> logging.Logger:
    """Configure logging with file and console handlers."""
    logger = logging.getLogger("video-compositor")
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
class Segment:
    """Represents a timed segment in the video."""
    index: int
    start_time: float
    end_time: float
    duration: float
    visual_asset: Optional[Path] = None
    title: Optional[str] = None
    description: Optional[str] = None
    asset_type: str = "image"  # "image" or "video"


@dataclass
class CompositorConfig:
    """Configuration for the compositor."""
    devon_video: Path
    assets_dir: Path
    script_json: Path
    output_path: Path
    pip_position: str = "bottom-right"
    pip_size: str = "medium"
    preview_only: bool = False
    temp_dir: Optional[Path] = None
    verbose: bool = False

    # Computed properties
    pip_width: int = field(init=False)
    pip_height: int = field(init=False)
    pip_x: int = field(init=False)
    pip_y: int = field(init=False)

    def __post_init__(self):
        self.pip_width, self.pip_height = PIP_SIZES.get(self.pip_size, PIP_SIZES["medium"])
        self.pip_x, self.pip_y = get_pip_position(self.pip_position, self.pip_width, self.pip_height)


# ============================================================================
# FFmpeg Utilities
# ============================================================================

class FFmpegWrapper:
    """Wrapper for FFmpeg operations."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.ffmpeg_path = self._find_ffmpeg()
        self.ffprobe_path = self._find_ffprobe()

    def _find_ffmpeg(self) -> str:
        """Find FFmpeg executable."""
        # Check common locations
        common_paths = [
            "ffmpeg",
            "ffmpeg.exe",
            r"C:\ffmpeg\bin\ffmpeg.exe",
            r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
            r"C:\ProgramData\chocolatey\bin\ffmpeg.exe",
            "/usr/bin/ffmpeg",
            "/usr/local/bin/ffmpeg",
        ]

        for path in common_paths:
            if shutil.which(path):
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
        # Check common locations first
        common_paths = [
            r"C:\ffmpeg\bin\ffprobe.exe",
            r"C:\Program Files\ffmpeg\bin\ffprobe.exe",
            "ffprobe.exe",
            "ffprobe",
        ]

        for path in common_paths:
            if os.path.exists(path):
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
            return False, "FFmpeg not found in PATH"
        except subprocess.TimeoutExpired:
            return False, "FFmpeg check timed out"
        except Exception as e:
            return False, f"Error checking FFmpeg: {e}"

    def get_video_info(self, video_path: Path) -> dict[str, Any]:
        """Get video information using ffprobe."""
        try:
            result = subprocess.run(
                [
                    self.ffprobe_path,
                    "-v", "quiet",
                    "-print_format", "json",
                    "-show_format",
                    "-show_streams",
                    str(video_path)
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
            self.logger.error(f"Error getting video info: {e}")
            return {}

    def get_duration(self, video_path: Path) -> float:
        """Get video duration in seconds."""
        info = self.get_video_info(video_path)
        if info and "format" in info:
            return float(info["format"].get("duration", 0))
        return 0.0

    def get_dimensions(self, video_path: Path) -> tuple[int, int]:
        """Get video dimensions (width, height)."""
        info = self.get_video_info(video_path)
        if info and "streams" in info:
            for stream in info["streams"]:
                if stream.get("codec_type") == "video":
                    return stream.get("width", 0), stream.get("height", 0)
        return 0, 0

    def run_ffmpeg(
        self,
        args: list[str],
        progress_callback: Optional[callable] = None,
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
                elif "error" in line.lower():
                    self.logger.warning(line.strip())

            process.wait(timeout=timeout)

            if process.returncode == 0:
                return True, "Success"
            else:
                error_msg = ''.join(stderr_output[-10:])  # Last 10 lines
                return False, error_msg

        except subprocess.TimeoutExpired:
            process.kill()
            return False, "FFmpeg timed out"
        except Exception as e:
            return False, f"FFmpeg error: {e}"


# ============================================================================
# Asset Management
# ============================================================================

class AssetManager:
    """Manages visual assets for compositing."""

    SUPPORTED_IMAGE_FORMATS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
    SUPPORTED_VIDEO_FORMATS = {".mp4", ".mov", ".webm", ".avi", ".mkv"}

    def __init__(self, assets_dir: Path, logger: logging.Logger):
        self.assets_dir = assets_dir
        self.logger = logger
        self.assets: dict[str, Path] = {}
        self._scan_assets()

    def _scan_assets(self):
        """Scan assets directory and index files."""
        if not self.assets_dir.exists():
            self.logger.warning(f"Assets directory not found: {self.assets_dir}")
            return

        for file in self.assets_dir.iterdir():
            if file.is_file():
                suffix = file.suffix.lower()
                if suffix in self.SUPPORTED_IMAGE_FORMATS | self.SUPPORTED_VIDEO_FORMATS:
                    key = file.stem.lower()
                    self.assets[key] = file
                    self.logger.debug(f"Found asset: {key} -> {file}")

        self.logger.info(f"Indexed {len(self.assets)} assets from {self.assets_dir}")

    def get_asset(self, name: str) -> Optional[Path]:
        """Get asset by name (case-insensitive, without extension)."""
        return self.assets.get(name.lower())

    def find_asset_for_segment(self, segment_index: int, segment_title: Optional[str] = None) -> Optional[Path]:
        """Find appropriate asset for a segment."""
        # Try by segment index with various formats
        # Note: segment_index is 0-based from parser, but segment_id in scripts is 1-based
        segment_id = segment_index + 1  # Convert to 1-based for matching

        patterns = [
            f"segment_{segment_id:03d}",  # segment_001, segment_002, etc.
            f"segment_{segment_id:02d}",  # segment_01, segment_02, etc.
            f"segment_{segment_id}",      # segment_1, segment_2, etc.
            f"segment_{segment_index:03d}",  # 0-based versions
            f"segment_{segment_index}",
            f"slide_{segment_id}",
            f"slide_{segment_index}",
            f"{segment_id}",
            f"{segment_index}",
        ]

        for pattern in patterns:
            if asset := self.get_asset(pattern):
                return asset

        # Try by title
        if segment_title:
            title_key = segment_title.lower().replace(" ", "_").replace("-", "_")
            if asset := self.get_asset(title_key):
                return asset

        return None

    def is_video_asset(self, path: Path) -> bool:
        """Check if asset is a video file."""
        return path.suffix.lower() in self.SUPPORTED_VIDEO_FORMATS

    def create_placeholder(self, output_path: Path, text: str = "Content") -> bool:
        """Create a placeholder image with text."""
        # Use FFmpeg to create a placeholder
        # Find ffmpeg path
        ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
        if not os.path.exists(ffmpeg_path):
            ffmpeg_path = "ffmpeg"

        # Escape special characters in text for FFmpeg filter
        safe_text = text.replace("'", "").replace(":", " -").replace("\\", "")[:40]

        try:
            result = subprocess.run(
                [
                    ffmpeg_path, "-y",
                    "-f", "lavfi",
                    "-i", f"color=c={BACKGROUND_COLOR}:s={OUTPUT_WIDTH}x{VISUAL_HEIGHT}:d=1",
                    "-vf", f"drawtext=text='{safe_text}':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2",
                    "-frames:v", "1",
                    str(output_path)
                ],
                capture_output=True,
                timeout=30
            )
            if result.returncode != 0:
                self.logger.debug(f"FFmpeg placeholder error: {result.stderr.decode()}")
            return output_path.exists()
        except Exception as e:
            self.logger.error(f"Failed to create placeholder: {e}")
            return False


# ============================================================================
# Script Parser
# ============================================================================

class ScriptParser:
    """Parses script JSON with timing information."""

    def __init__(self, script_path: Path, logger: logging.Logger):
        self.script_path = script_path
        self.logger = logger
        self.segments: list[Segment] = []
        self.total_duration: float = 0
        self._parse()

    def _parse(self):
        """Parse the script JSON file."""
        if not self.script_path.exists():
            self.logger.error(f"Script file not found: {self.script_path}")
            return

        try:
            with open(self.script_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Handle various JSON structures
            segments_data = data.get("segments", data.get("scenes", data.get("slides", [])))

            if not segments_data:
                # If flat structure, treat entire content as one segment
                self.logger.warning("No segments found, treating as single segment")
                duration = data.get("duration", data.get("total_duration", 60))
                self.segments.append(Segment(
                    index=0,
                    start_time=0,
                    end_time=duration,
                    duration=duration,
                    title=data.get("title", "Main Content")
                ))
                self.total_duration = duration
                return

            current_time = 0.0
            for i, seg in enumerate(segments_data):
                # Extract timing - support various field names
                start = seg.get("start_time", seg.get("start", current_time))
                end = seg.get("end_time", seg.get("end"))
                duration = seg.get("duration")

                if duration and not end:
                    end = start + duration
                elif end and not duration:
                    duration = end - start
                elif not duration and not end:
                    # Default to 10 seconds if no timing info
                    duration = 10.0
                    end = start + duration

                segment = Segment(
                    index=i,
                    start_time=float(start),
                    end_time=float(end),
                    duration=float(duration),
                    title=seg.get("title", seg.get("name", seg.get("heading"))),
                    description=seg.get("description", seg.get("text", seg.get("content"))),
                )

                # Check for visual asset reference
                if visual := seg.get("visual", seg.get("asset", seg.get("image"))):
                    segment.visual_asset = Path(visual) if visual else None

                self.segments.append(segment)
                current_time = end

            self.total_duration = max(seg.end_time for seg in self.segments) if self.segments else 0
            self.logger.info(f"Parsed {len(self.segments)} segments, total duration: {self.total_duration:.2f}s")

        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in script file: {e}")
        except Exception as e:
            self.logger.error(f"Error parsing script: {e}")

    def get_segment_at_time(self, time: float) -> Optional[Segment]:
        """Get the segment at a specific time."""
        for segment in self.segments:
            if segment.start_time <= time < segment.end_time:
                return segment
        return None


# ============================================================================
# Video Compositor
# ============================================================================

class VideoCompositor:
    """Main compositor class that orchestrates the video composition."""

    def __init__(self, config: CompositorConfig, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.ffmpeg = FFmpegWrapper(logger)
        self.asset_manager = AssetManager(config.assets_dir, logger)
        self.script_parser = ScriptParser(config.script_json, logger)
        self.temp_dir = config.temp_dir or Path(tempfile.mkdtemp(prefix="compositor_"))

    def validate_inputs(self) -> bool:
        """Validate all input files and configuration."""
        errors = []

        # Check FFmpeg
        available, msg = self.ffmpeg.check_availability()
        if not available:
            errors.append(f"FFmpeg: {msg}")

        # Check Devon video
        if not self.config.devon_video.exists():
            errors.append(f"Devon video not found: {self.config.devon_video}")
        else:
            duration = self.ffmpeg.get_duration(self.config.devon_video)
            if duration == 0:
                errors.append(f"Could not read Devon video duration")
            else:
                self.logger.info(f"Devon video duration: {duration:.2f}s")

        # Check assets directory
        if not self.config.assets_dir.exists():
            self.logger.warning(f"Assets directory not found, will use placeholders")

        # Check script JSON
        if not self.config.script_json.exists():
            errors.append(f"Script JSON not found: {self.config.script_json}")
        elif not self.script_parser.segments:
            errors.append("No segments parsed from script JSON")

        # Report errors
        if errors:
            for error in errors:
                self.logger.error(error)
            return False

        return True

    def prepare_devon_video(self) -> Optional[Path]:
        """Prepare Devon video (concatenate if in parts, scale if needed)."""
        devon_path = self.config.devon_video

        # Check if it's a directory with parts
        if devon_path.is_dir():
            parts = sorted(devon_path.glob("*.mp4"))
            if not parts:
                self.logger.error("No MP4 files found in Devon video directory")
                return None

            if len(parts) > 1:
                self.logger.info(f"Concatenating {len(parts)} Devon video parts")
                concat_path = self.temp_dir / "devon_concat.mp4"

                # Create concat file list
                concat_list = self.temp_dir / "concat_list.txt"
                with open(concat_list, 'w') as f:
                    for part in parts:
                        f.write(f"file '{part}'\n")

                success, msg = self.ffmpeg.run_ffmpeg([
                    "-y", "-f", "concat", "-safe", "0",
                    "-i", str(concat_list),
                    "-c", "copy",
                    str(concat_path)
                ])

                if not success:
                    self.logger.error(f"Failed to concatenate Devon videos: {msg}")
                    return None

                devon_path = concat_path
            else:
                devon_path = parts[0]

        # Get current dimensions
        width, height = self.ffmpeg.get_dimensions(devon_path)
        self.logger.info(f"Devon video dimensions: {width}x{height}")

        # Scale to PiP size and apply mask
        pip_path = self.temp_dir / "devon_pip.mp4"

        # Create circular/rounded mask and add shadow effect
        filter_complex = (
            f"[0:v]scale={self.config.pip_width}:{self.config.pip_height},"
            f"format=rgba,"
            # Rounded rectangle mask
            f"geq=lum='p(X,Y)':a='if(gt(abs(X-W/2),W/2-20)*gt(abs(Y-H/2),H/2-20),"
            f"if(lte(hypot(abs(X-W/2)-(W/2-20),abs(Y-H/2)-(H/2-20)),20),255,0),255)'"
            f"[pip]"
        )

        # Simpler approach with just scaling and slight vignette
        filter_simple = (
            f"scale={self.config.pip_width}:{self.config.pip_height}:force_original_aspect_ratio=decrease,"
            f"pad={self.config.pip_width}:{self.config.pip_height}:(ow-iw)/2:(oh-ih)/2:color=black,"
            f"format=yuv420p"
        )

        success, msg = self.ffmpeg.run_ffmpeg([
            "-y", "-i", str(devon_path),
            "-vf", filter_simple,
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-c:a", "aac", "-b:a", "128k",
            str(pip_path)
        ])

        if not success:
            self.logger.error(f"Failed to prepare Devon PiP: {msg}")
            return None

        self.logger.info(f"Prepared Devon PiP video: {pip_path}")
        return pip_path

    def prepare_visual_sequence(self, devon_duration: float) -> Optional[Path]:
        """Create the visual sequence video from assets."""
        segments = self.script_parser.segments

        if not segments:
            self.logger.warning("No segments, creating placeholder visual")
            placeholder_path = self.temp_dir / "placeholder.png"
            self.asset_manager.create_placeholder(placeholder_path, "Support Forge")

            # Create video from placeholder
            visual_path = self.temp_dir / "visuals.mp4"
            success, msg = self.ffmpeg.run_ffmpeg([
                "-y", "-loop", "1",
                "-i", str(placeholder_path),
                "-t", str(devon_duration),
                "-vf", f"scale={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:force_original_aspect_ratio=decrease,pad={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color={BACKGROUND_COLOR}",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                "-pix_fmt", "yuv420p",
                str(visual_path)
            ])
            return visual_path if success else None

        # Prepare individual segment videos
        segment_videos = []

        for segment in segments:
            segment_video = self.temp_dir / f"segment_{segment.index}.mp4"

            # Find visual asset
            visual_asset = None
            if segment.visual_asset and segment.visual_asset.exists():
                visual_asset = segment.visual_asset
            else:
                visual_asset = self.asset_manager.find_asset_for_segment(
                    segment.index,
                    segment.title
                )

            if visual_asset is None:
                # Create placeholder
                placeholder = self.temp_dir / f"placeholder_{segment.index}.png"
                text = segment.title or f"Segment {segment.index + 1}"
                self.asset_manager.create_placeholder(placeholder, text)
                visual_asset = placeholder

            self.logger.info(f"Segment {segment.index}: {visual_asset.name} ({segment.duration:.2f}s)")

            # Create segment video
            is_video = self.asset_manager.is_video_asset(visual_asset)

            if is_video:
                # Handle video asset
                success, msg = self.ffmpeg.run_ffmpeg([
                    "-y", "-i", str(visual_asset),
                    "-t", str(segment.duration),
                    "-vf", f"scale={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:force_original_aspect_ratio=decrease,pad={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color={BACKGROUND_COLOR},setsar=1",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                    "-an",  # Remove audio from visual assets
                    "-pix_fmt", "yuv420p",
                    str(segment_video)
                ])
            else:
                # Handle image asset
                success, msg = self.ffmpeg.run_ffmpeg([
                    "-y", "-loop", "1",
                    "-i", str(visual_asset),
                    "-t", str(segment.duration),
                    "-vf", f"scale={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:force_original_aspect_ratio=decrease,pad={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color={BACKGROUND_COLOR},setsar=1",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                    "-pix_fmt", "yuv420p",
                    str(segment_video)
                ])

            if not success:
                self.logger.error(f"Failed to create segment {segment.index}: {msg}")
                return None

            segment_videos.append(segment_video)

        # Concatenate with crossfade transitions
        if len(segment_videos) == 1:
            final_visual = segment_videos[0]
        else:
            final_visual = self._concatenate_with_transitions(segment_videos)

        # Ensure duration matches Devon video
        visual_duration = self.ffmpeg.get_duration(final_visual)
        if visual_duration < devon_duration:
            # Extend last frame
            self.logger.info(f"Extending visual from {visual_duration:.2f}s to {devon_duration:.2f}s")
            extended = self.temp_dir / "visuals_extended.mp4"

            # Use tpad filter to extend
            success, msg = self.ffmpeg.run_ffmpeg([
                "-y", "-i", str(final_visual),
                "-vf", f"tpad=stop_mode=clone:stop_duration={devon_duration - visual_duration}",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                str(extended)
            ])

            if success:
                final_visual = extended

        return final_visual

    def _concatenate_with_transitions(self, videos: list[Path]) -> Path:
        """Concatenate videos with crossfade transitions."""
        if len(videos) <= 1:
            return videos[0] if videos else None

        # Build complex filter for crossfades
        # For simplicity, use xfade filter between consecutive videos
        output_path = self.temp_dir / "visuals_concat.mp4"

        # Simple concat for now (xfade is complex with multiple inputs)
        concat_list = self.temp_dir / "visual_concat.txt"
        with open(concat_list, 'w') as f:
            for video in videos:
                f.write(f"file '{video}'\n")

        success, msg = self.ffmpeg.run_ffmpeg([
            "-y", "-f", "concat", "-safe", "0",
            "-i", str(concat_list),
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            str(output_path)
        ])

        if not success:
            self.logger.error(f"Failed to concatenate visuals: {msg}")
            return videos[0]  # Return first video as fallback

        return output_path

    def compose_final_video(
        self,
        devon_pip: Path,
        visuals: Path,
        lower_thirds: Optional[list[dict]] = None
    ) -> bool:
        """Compose the final video with all layers."""
        self.logger.info("Composing final video...")

        # Build filter complex for composition
        # Background -> Visuals -> Devon PiP

        filter_complex = (
            # Create background
            f"color=c={BACKGROUND_COLOR}:s={OUTPUT_WIDTH}x{OUTPUT_HEIGHT}:d=1[bg];"

            # Scale visuals to fit visual area
            f"[1:v]scale={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:force_original_aspect_ratio=decrease,"
            f"pad={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color={BACKGROUND_COLOR}[visual];"

            # Overlay visuals on background (top portion)
            f"[bg][visual]overlay=0:0:shortest=0[with_visual];"

            # Overlay Devon PiP
            f"[with_visual][2:v]overlay={self.config.pip_x}:{self.config.pip_y}[final]"
        )

        # Calculate Devon video duration
        devon_duration = self.ffmpeg.get_duration(devon_pip)

        success, msg = self.ffmpeg.run_ffmpeg([
            "-y",
            "-f", "lavfi", "-i", f"color=c={BACKGROUND_COLOR}:s={OUTPUT_WIDTH}x{OUTPUT_HEIGHT}:r=30",
            "-i", str(visuals),
            "-i", str(devon_pip),
            "-filter_complex", filter_complex,
            "-map", "[final]",
            "-map", "2:a",  # Use Devon audio
            "-t", str(devon_duration),
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            str(self.config.output_path)
        ], progress_callback=self._progress_callback)

        if success:
            self.logger.info(f"Final video created: {self.config.output_path}")
            return True
        else:
            self.logger.error(f"Failed to compose final video: {msg}")
            return False

    def _progress_callback(self, line: str):
        """Handle FFmpeg progress output."""
        if "time=" in line:
            # Extract time from FFmpeg output
            import re
            match = re.search(r'time=(\d+):(\d+):(\d+\.?\d*)', line)
            if match:
                hours, minutes, seconds = match.groups()
                current = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
                total = self.script_parser.total_duration or 60
                percent = min(100, (current / total) * 100)
                print(f"\rProgress: {percent:.1f}% ({current:.1f}s / {total:.1f}s)", end="", flush=True)

    def generate_preview(self, times: list[float] = None) -> list[Path]:
        """Generate preview frames at specified times."""
        if times is None:
            # Default: start, 25%, 50%, 75%, end
            duration = self.ffmpeg.get_duration(self.config.devon_video)
            times = [0, duration * 0.25, duration * 0.5, duration * 0.75, duration - 0.5]

        previews = []

        for i, time in enumerate(times):
            preview_path = self.config.output_path.parent / f"preview_{i}_{time:.1f}s.png"

            # For preview, we need to actually compose a single frame
            self.logger.info(f"Generating preview at {time:.1f}s")

            # Get segment at this time for visual
            segment = self.script_parser.get_segment_at_time(time)
            visual_asset = None

            if segment:
                if segment.visual_asset and segment.visual_asset.exists():
                    visual_asset = segment.visual_asset
                else:
                    visual_asset = self.asset_manager.find_asset_for_segment(
                        segment.index,
                        segment.title
                    )

            if visual_asset is None:
                # Create placeholder
                placeholder = self.temp_dir / "preview_placeholder.png"
                text = segment.title if segment else "Preview"
                self.asset_manager.create_placeholder(placeholder, text)
                visual_asset = placeholder

            # Extract Devon frame at this time
            devon_frame = self.temp_dir / f"devon_frame_{i}.png"
            success, _ = self.ffmpeg.run_ffmpeg([
                "-y", "-ss", str(time),
                "-i", str(self.config.devon_video),
                "-vframes", "1",
                "-vf", f"scale={self.config.pip_width}:{self.config.pip_height}",
                str(devon_frame)
            ])

            if not success:
                continue

            # Compose preview frame
            filter_complex = (
                # Background
                f"color=c={BACKGROUND_COLOR}:s={OUTPUT_WIDTH}x{OUTPUT_HEIGHT}[bg];"

                # Scale visual
                f"[1:v]scale={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:force_original_aspect_ratio=decrease,"
                f"pad={OUTPUT_WIDTH}:{VISUAL_HEIGHT}:(ow-iw)/2:(oh-ih)/2:color={BACKGROUND_COLOR}[visual];"

                # Overlay visual
                f"[bg][visual]overlay=0:0[with_visual];"

                # Overlay Devon PiP
                f"[with_visual][2:v]overlay={self.config.pip_x}:{self.config.pip_y}[final]"
            )

            success, msg = self.ffmpeg.run_ffmpeg([
                "-y",
                "-f", "lavfi", "-i", f"color=c={BACKGROUND_COLOR}:s={OUTPUT_WIDTH}x{OUTPUT_HEIGHT}",
                "-i", str(visual_asset),
                "-i", str(devon_frame),
                "-filter_complex", filter_complex,
                "-map", "[final]",
                "-frames:v", "1",
                str(preview_path)
            ])

            if success and preview_path.exists():
                previews.append(preview_path)
                self.logger.info(f"Preview saved: {preview_path}")

        return previews

    def run(self) -> bool:
        """Execute the full composition pipeline."""
        self.logger.info("=" * 60)
        self.logger.info("Video Compositor Starting")
        self.logger.info("=" * 60)

        # Validate inputs
        if not self.validate_inputs():
            return False

        # Preview mode
        if self.config.preview_only:
            self.logger.info("Preview mode - generating preview frames only")
            previews = self.generate_preview()
            self.logger.info(f"Generated {len(previews)} preview frames")
            return len(previews) > 0

        # Prepare Devon PiP video
        self.logger.info("Preparing Devon PiP video...")
        devon_pip = self.prepare_devon_video()
        if devon_pip is None:
            return False

        devon_duration = self.ffmpeg.get_duration(devon_pip)
        self.logger.info(f"Devon duration: {devon_duration:.2f}s")

        # Prepare visual sequence
        self.logger.info("Preparing visual sequence...")
        visuals = self.prepare_visual_sequence(devon_duration)
        if visuals is None:
            return False

        # Compose final video
        success = self.compose_final_video(devon_pip, visuals)

        # Cleanup temp files
        if success and not self.config.verbose:
            self.logger.info("Cleaning up temporary files...")
            try:
                import shutil
                shutil.rmtree(self.temp_dir, ignore_errors=True)
            except Exception:
                pass

        print()  # New line after progress
        self.logger.info("=" * 60)
        if success:
            self.logger.info(f"Composition complete: {self.config.output_path}")
            file_size = self.config.output_path.stat().st_size / (1024 * 1024)
            self.logger.info(f"Output size: {file_size:.1f} MB")
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
        description="Composite Devon avatar videos with visual assets",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic composition
    python video-compositor.py --devon devon.mp4 --assets ./assets/ --script parsed.json --output final.mp4

    # Preview mode
    python video-compositor.py --devon devon.mp4 --assets ./assets/ --script parsed.json --preview

    # Custom PiP position and size
    python video-compositor.py --devon devon.mp4 --assets ./assets/ --script parsed.json --output final.mp4 \\
        --pip-position bottom-left --pip-size large

    # Verbose mode for debugging
    python video-compositor.py --devon devon.mp4 --assets ./assets/ --script parsed.json --output final.mp4 -v
        """
    )

    # Required arguments (not required if --check-ffmpeg is used)
    parser.add_argument(
        "--devon",
        type=Path,
        help="Path to Devon avatar video (MP4) or directory with video parts"
    )

    parser.add_argument(
        "--assets",
        type=Path,
        help="Path to visual assets directory"
    )

    parser.add_argument(
        "--script",
        type=Path,
        help="Path to parsed script JSON with timing info"
    )

    # Output options
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=DEFAULT_OUTPUT_DIR / "composed_video.mp4",
        help="Output video path (default: ./output/composed_video.mp4)"
    )

    # PiP options
    parser.add_argument(
        "--pip-position",
        choices=["bottom-right", "bottom-left", "top-right", "top-left"],
        default="bottom-right",
        help="Position of Devon PiP (default: bottom-right)"
    )

    parser.add_argument(
        "--pip-size",
        choices=["small", "medium", "large"],
        default="medium",
        help="Size of Devon PiP (default: medium)"
    )

    # Mode options
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Generate preview frames only (no video output)"
    )

    # Other options
    parser.add_argument(
        "--temp-dir",
        type=Path,
        help="Custom temporary directory for intermediate files"
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
            print("\nTo install FFmpeg:")
            print("  Windows: choco install ffmpeg  (or download from ffmpeg.org)")
            print("  macOS:   brew install ffmpeg")
            print("  Linux:   apt install ffmpeg")
            sys.exit(1)

    # Validate required arguments for composition mode
    if not args.devon or not args.assets or not args.script:
        print("Error: --devon, --assets, and --script are required for composition")
        print("Use --check-ffmpeg to just check FFmpeg availability")
        sys.exit(1)

    # Ensure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)

    # Create compositor config
    config = CompositorConfig(
        devon_video=args.devon,
        assets_dir=args.assets,
        script_json=args.script,
        output_path=args.output,
        pip_position=args.pip_position,
        pip_size=args.pip_size,
        preview_only=args.preview,
        temp_dir=args.temp_dir,
        verbose=args.verbose
    )

    # Run compositor
    compositor = VideoCompositor(config, logger)
    success = compositor.run()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
