#!/usr/bin/env python3
"""
Upload completed videos to S3 bucket for AI Launchpad Academy.
"""

import subprocess
import sys
from pathlib import Path

AWS_CLI = r"C:\Program Files\Amazon\AWSCLIV2\aws.exe"
PROFILE = "support-forge"
REGION = "us-east-1"
BUCKET = "launchpad-academy-videos"

SCRIPT_DIR = Path(__file__).parent
VIDEOS_DIR = SCRIPT_DIR / "output/thinkific-deploy"

# Video mappings: local filename -> S3 key
VIDEO_MAPPINGS = {
    "Module7-Lesson1-Security-Part1.mp4": "videos/module-7/7.1-credential-security-part1.mp4",
    "Module7-Lesson1-Security-Part2.mp4": "videos/module-7/7.1-credential-security-part2.mp4",
    "Module7-Lesson1-Security-Part3.mp4": "videos/module-7/7.1-credential-security-part3.mp4",
    "Module7-Lesson1-Security-Part4.mp4": "videos/module-7/7.1-credential-security-part4.mp4",
    "Module8-Lesson1-Capstone-Overview.mp4": "videos/module-8/8.1-capstone-overview.mp4",
    "Module8-Lesson2-Onboarding-Part1.mp4": "videos/module-8/8.2-onboarding-part1.mp4",
    "Module8-Lesson2-Onboarding-Part2.mp4": "videos/module-8/8.2-onboarding-part2.mp4",
}


def run_aws(args: list) -> tuple[int, str, str]:
    """Run AWS CLI command."""
    cmd = [AWS_CLI] + args + ["--profile", PROFILE, "--region", REGION]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def upload_video(local_path: Path, s3_key: str) -> bool:
    """Upload a video to S3."""
    s3_uri = f"s3://{BUCKET}/{s3_key}"

    print(f"Uploading {local_path.name} -> {s3_key}...")

    code, stdout, stderr = run_aws([
        "s3", "cp",
        str(local_path),
        s3_uri,
        "--content-type", "video/mp4"
    ])

    if code == 0:
        print(f"  Success!")
        return True
    else:
        print(f"  Failed: {stderr}")
        return False


def main():
    print("=" * 60)
    print("Uploading Videos to S3")
    print(f"Bucket: {BUCKET}")
    print("=" * 60)

    # Check if bucket exists
    print("\nChecking bucket...")
    code, stdout, stderr = run_aws(["s3", "ls", f"s3://{BUCKET}"])
    if code != 0:
        print(f"Bucket {BUCKET} not found or not accessible!")
        print("Please create the bucket first.")
        return 1

    print(f"Bucket exists. Uploading {len(VIDEO_MAPPINGS)} videos...\n")

    success_count = 0
    fail_count = 0

    for local_name, s3_key in VIDEO_MAPPINGS.items():
        local_path = VIDEOS_DIR / local_name

        if not local_path.exists():
            print(f"Skipping {local_name} - file not found")
            fail_count += 1
            continue

        if upload_video(local_path, s3_key):
            success_count += 1
        else:
            fail_count += 1

    print("\n" + "=" * 60)
    print(f"Upload complete: {success_count} succeeded, {fail_count} failed")
    print("=" * 60)

    # List uploaded files
    print("\nVerifying uploads...")
    code, stdout, stderr = run_aws(["s3", "ls", f"s3://{BUCKET}/videos/", "--recursive"])
    if code == 0:
        print(stdout)

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
