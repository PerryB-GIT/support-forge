#!/usr/bin/env python3
"""
Composite Synced Video
======================
Creates a video where slides are properly synced to audio duration.
Scales segment timings proportionally to match actual audio length.
"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FFPROBE = Path(r"C:\ffmpeg\bin\ffprobe.exe")
FFMPEG = Path(r"C:\ffmpeg\bin\ffmpeg.exe")

# Skip segment 25 (production notes)
SKIP_SEGMENTS = [25]

def get_audio_duration(audio_path: Path) -> float:
    """Get audio duration in seconds."""
    cmd = [
        str(FFPROBE), "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(audio_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())


def create_scaled_script(script_path: Path, audio_duration: float, output_path: Path) -> int:
    """Create a new script JSON with scaled timings to match audio duration."""
    with open(script_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data.get("segments", [])

    # Filter out skipped segments
    filtered = [s for s in segments if s.get("segment_id") not in SKIP_SEGMENTS]

    if not filtered:
        print("No segments found!")
        return 0

    # Get the original content duration (excluding skipped segments)
    last_segment = filtered[-1]
    original_duration = last_segment.get("end_time", 0)

    # Calculate scaling factor
    scale = audio_duration / original_duration if original_duration > 0 else 1.0
    print(f"Original content duration: {original_duration:.1f}s")
    print(f"Audio duration: {audio_duration:.1f}s")
    print(f"Scale factor: {scale:.3f}")

    # Scale all segment timings
    for seg in filtered:
        seg["start_time"] = seg["start_time"] * scale
        seg["end_time"] = seg["end_time"] * scale

    # Update the data
    data["segments"] = filtered
    data["total_duration_seconds"] = audio_duration

    # Write scaled script
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Created scaled script: {output_path}")
    return len(filtered)


def main():
    # Use trimmed audio (M4A has correct duration metadata)
    audio_path = SCRIPT_DIR / "output/devon-audio/8.1-capstone-trimmed.m4a"
    script_path = SCRIPT_DIR / "output/parsed-scripts/8.1-capstone-project-overview.json"
    scaled_script = SCRIPT_DIR / "output/parsed-scripts/8.1-capstone-scaled.json"
    slides_dir = SCRIPT_DIR / "output/capstone-slides"
    output_video = SCRIPT_DIR / "output/8.1-capstone-final.mp4"

    print("=" * 60)
    print("Creating Synced Video with Trimmed Audio")
    print("=" * 60)

    # Get actual audio duration
    print(f"\nChecking audio: {audio_path.name}")
    audio_duration = get_audio_duration(audio_path)
    print(f"Audio duration: {audio_duration:.1f}s ({audio_duration/60:.1f} min)")

    # Create scaled script
    print(f"\nScaling segment timings...")
    num_segments = create_scaled_script(script_path, audio_duration, scaled_script)
    print(f"Segments: {num_segments} (skipped: {SKIP_SEGMENTS})")

    # Run compositor with scaled script
    print(f"\nRunning compositor...")
    cmd = [
        sys.executable, str(SCRIPT_DIR / "audio-slides-compositor.py"),
        "--audio", str(audio_path),
        "--slides", str(slides_dir),
        "--script", str(scaled_script),
        "--output", str(output_video),
        "--transition", "0.3"
    ]

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"\n{'=' * 60}")
        print("Video created successfully!")
        print(f"Output: {output_video}")
        print(f"{'=' * 60}")
    else:
        print(f"\nCompositor failed with code {result.returncode}")

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
