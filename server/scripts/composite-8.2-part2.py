#!/usr/bin/env python3
"""
Composite 8.2 Building Client Onboarding Agent - Part 2
Creates video from Devon audio + slides for segments 15-28
"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FFPROBE = Path(r"C:\ffmpeg\bin\ffprobe.exe")

# Part 2 configuration
AUDIO_FILE = "8.2-onboarding-part2.m4a"
MIN_SEGMENT = 15
MAX_SEGMENT = 28  # Approximate based on ~360 words
OUTPUT_NAME = "8.2-onboarding-agent-part2.mp4"


def get_audio_duration(audio_path: Path) -> float:
    cmd = [
        str(FFPROBE), "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(audio_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())


def create_scaled_script(script_path: Path, audio_duration: float,
                         output_path: Path, min_seg: int, max_seg: int) -> int:
    with open(script_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data.get("segments", [])

    # Filter to target segments
    part_segments = [s for s in segments
                     if min_seg <= s.get("segment_id", 0) <= max_seg]

    if not part_segments:
        print("No segments found!")
        return 0

    # Adjust timings relative to first segment
    first_start = part_segments[0].get("start_time", 0)
    for seg in part_segments:
        seg["start_time"] -= first_start
        seg["end_time"] -= first_start

    # Get duration and scale
    original_duration = part_segments[-1].get("end_time", 0)
    scale = audio_duration / original_duration if original_duration > 0 else 1.0

    print(f"Original duration: {original_duration:.1f}s")
    print(f"Audio duration: {audio_duration:.1f}s")
    print(f"Scale factor: {scale:.3f}")

    # Scale timings
    for seg in part_segments:
        seg["start_time"] *= scale
        seg["end_time"] *= scale

    data["segments"] = part_segments
    data["total_duration_seconds"] = audio_duration

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    return len(part_segments)


def generate_slides():
    """Generate slides for part 2 segments."""
    print("Generating slides for part 2...")

    # Use existing slide generator but modify for part 2 segments
    slides_dir = SCRIPT_DIR / "output/onboarding-slides"
    slides_dir.mkdir(parents=True, exist_ok=True)

    # Check if slides already exist
    existing = list(slides_dir.glob("slide_*.png"))
    max_existing = max([int(f.stem.split('_')[1]) for f in existing]) if existing else 0

    if max_existing >= MAX_SEGMENT:
        print(f"Slides already exist up to segment {max_existing}")
        return True

    # Generate missing slides
    print(f"Need to generate slides {max_existing + 1} to {MAX_SEGMENT}...")

    # Import and run slide generator for specific segments
    from generate_onboarding_slides_part2 import main as gen_slides
    gen_slides()

    return True


def main():
    audio_path = SCRIPT_DIR / f"output/devon-audio/{AUDIO_FILE}"
    script_path = SCRIPT_DIR / "output/parsed-scripts/8.2-building-client-onboarding-agent.json"
    scaled_script = SCRIPT_DIR / "output/parsed-scripts/8.2-onboarding-part2-scaled.json"
    slides_dir = SCRIPT_DIR / "output/onboarding-slides"
    output_video = SCRIPT_DIR / f"output/{OUTPUT_NAME}"

    print("=" * 60)
    print("Creating 8.2 Building Client Onboarding Agent - Part 2")
    print("=" * 60)

    # Get audio duration
    print(f"\nChecking audio: {AUDIO_FILE}")
    audio_duration = get_audio_duration(audio_path)
    print(f"Audio duration: {audio_duration:.1f}s ({audio_duration/60:.1f} min)")

    # Create scaled script
    print(f"\nSegments: {MIN_SEGMENT}-{MAX_SEGMENT}")
    print("Scaling segment timings...")
    num_segments = create_scaled_script(script_path, audio_duration,
                                        scaled_script, MIN_SEGMENT, MAX_SEGMENT)
    print(f"Processed {num_segments} segments")

    # Check if slides exist
    slides_exist = all((slides_dir / f"slide_{i:02d}.png").exists()
                       for i in range(MIN_SEGMENT, MAX_SEGMENT + 1))

    if not slides_exist:
        print("\nGenerating missing slides...")
        # Run slide generator
        cmd = [sys.executable, str(SCRIPT_DIR / "generate-onboarding-slides-part2.py")]
        subprocess.run(cmd)

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
