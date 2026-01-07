#!/usr/bin/env python3
"""
Composite 8.2 Building Client Onboarding Agent Video
"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FFPROBE = Path(r"C:\ffmpeg\bin\ffprobe.exe")
FFMPEG = Path(r"C:\ffmpeg\bin\ffmpeg.exe")

# Part 1 covers segments 1-14
MAX_SEGMENT = 14


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
    """Create a scaled script JSON for part1 segments."""
    with open(script_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data.get("segments", [])

    # Filter to part1 segments only
    part1_segments = [s for s in segments if s.get("segment_id", 0) <= MAX_SEGMENT]

    if not part1_segments:
        print("No segments found!")
        return 0

    # Get original duration of part1 content
    last_segment = part1_segments[-1]
    original_duration = last_segment.get("end_time", 0)

    # Calculate scaling factor
    scale = audio_duration / original_duration if original_duration > 0 else 1.0
    print(f"Original part1 duration: {original_duration:.1f}s")
    print(f"Audio duration: {audio_duration:.1f}s")
    print(f"Scale factor: {scale:.3f}")

    # Scale timings
    for seg in part1_segments:
        seg["start_time"] = seg["start_time"] * scale
        seg["end_time"] = seg["end_time"] * scale

    # Update data
    data["segments"] = part1_segments
    data["total_duration_seconds"] = audio_duration

    # Write scaled script
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Created scaled script: {output_path}")
    return len(part1_segments)


def main():
    # Use trimmed audio (M4A has correct duration metadata)
    audio_path = SCRIPT_DIR / "output/devon-audio/8.2-onboarding-trimmed.m4a"
    script_path = SCRIPT_DIR / "output/parsed-scripts/8.2-building-client-onboarding-agent.json"
    scaled_script = SCRIPT_DIR / "output/parsed-scripts/8.2-onboarding-scaled.json"
    slides_dir = SCRIPT_DIR / "output/onboarding-slides"
    output_video = SCRIPT_DIR / "output/8.2-onboarding-agent-part1.mp4"

    print("=" * 60)
    print("Creating 8.2 Client Onboarding Agent Video (Part 1)")
    print("=" * 60)

    # Get audio duration
    print(f"\nChecking audio: {audio_path.name}")
    audio_duration = get_audio_duration(audio_path)
    print(f"Audio duration: {audio_duration:.1f}s ({audio_duration/60:.1f} min)")

    # Create scaled script
    print(f"\nScaling segment timings...")
    num_segments = create_scaled_script(script_path, audio_duration, scaled_script)
    print(f"Segments: {num_segments}")

    # Run compositor
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
