#!/usr/bin/env python3
"""
Composite 7.1 Credential Security Videos
Handles multiple parts with segment mapping
"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FFPROBE = Path(r"C:\ffmpeg\bin\ffprobe.exe")

# Part definitions: (audio_file, max_segment, output_name)
PARTS = {
    1: ("7.1-credential-part1-trimmed.m4a", 13, "7.1-credential-security-part1.mp4"),
    3: ("7.1-credential-part3-trimmed.m4a", 22, "7.1-credential-security-part3.mp4"),
    4: ("7.1-credential-part4-trimmed.m4a", 26, "7.1-credential-security-part4.mp4"),
    5: ("7.1-credential-part5-trimmed.m4a", 28, "7.1-credential-security-part5.mp4"),
}


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


def process_part(part_num: int):
    if part_num not in PARTS:
        print(f"Unknown part: {part_num}")
        return 1

    audio_file, max_seg, output_name = PARTS[part_num]

    audio_path = SCRIPT_DIR / f"output/devon-audio/{audio_file}"
    script_path = SCRIPT_DIR / "output/parsed-scripts/7.1-credential-security.json"
    scaled_script = SCRIPT_DIR / f"output/parsed-scripts/7.1-credential-part{part_num}-scaled.json"
    slides_dir = SCRIPT_DIR / "output/credential-slides"
    output_video = SCRIPT_DIR / f"output/{output_name}"

    print("=" * 60)
    print(f"Creating 7.1 Credential Security Video (Part {part_num})")
    print("=" * 60)

    # Get audio duration
    print(f"\nChecking audio: {audio_file}")
    audio_duration = get_audio_duration(audio_path)
    print(f"Audio duration: {audio_duration:.1f}s ({audio_duration/60:.1f} min)")

    # Calculate segment range for this part
    # Part 1: segments 1-13
    # Part 3: segments 14-? (need to calculate based on accumulated time)
    # etc.

    if part_num == 1:
        min_seg, max_seg = 1, 13
    elif part_num == 3:
        min_seg, max_seg = 14, 22  # Approximate
    elif part_num == 4:
        min_seg, max_seg = 23, 26
    elif part_num == 5:
        min_seg, max_seg = 27, 28

    print(f"\nSegments: {min_seg}-{max_seg}")

    # Create scaled script
    print(f"Scaling segment timings...")
    num_segments = create_scaled_script(script_path, audio_duration,
                                        scaled_script, min_seg, max_seg)
    print(f"Processed {num_segments} segments")

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


def main():
    # Process part 1 by default, or specify part number
    part = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    return process_part(part)


if __name__ == "__main__":
    sys.exit(main())
