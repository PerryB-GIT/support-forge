#!/usr/bin/env python3
"""
HeyGen Avatar Video Generator
============================
A Python client for the HeyGen API to generate AI avatar videos.

This script provides functionality to:
- List available avatars and voices
- Generate videos from script text
- Poll for video completion status
- Download completed videos
- Batch process multiple scripts

Reference: https://docs.heygen.com/

Usage:
    python heygen-avatar-generator.py --script "path/to/script.txt" --avatar <avatar_id> --voice <voice_id>
    python heygen-avatar-generator.py --list-avatars
    python heygen-avatar-generator.py --list-voices
    python heygen-avatar-generator.py --batch "path/to/scripts_dir" --output "path/to/output_dir"

Environment Variables:
    HEYGEN_API_KEY: Your HeyGen API key (required)
"""

import os
import sys
import json
import time
import argparse
import logging
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from dataclasses import dataclass
from enum import Enum

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class VideoStatus(Enum):
    """Video generation status values."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    WAITING = "waiting"


@dataclass
class VideoGenerationResult:
    """Result of a video generation request."""
    video_id: str
    status: VideoStatus
    video_url: Optional[str] = None
    error_message: Optional[str] = None
    duration: Optional[float] = None


@dataclass
class Avatar:
    """HeyGen avatar information."""
    avatar_id: str
    avatar_name: str
    avatar_type: str
    preview_image_url: Optional[str] = None

    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> 'Avatar':
        return cls(
            avatar_id=data.get('avatar_id', ''),
            avatar_name=data.get('avatar_name', ''),
            avatar_type=data.get('type', 'avatar'),
            preview_image_url=data.get('preview_image_url')
        )


@dataclass
class Voice:
    """HeyGen voice information."""
    voice_id: str
    name: str
    language: str
    gender: Optional[str] = None

    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> 'Voice':
        return cls(
            voice_id=data.get('voice_id', ''),
            name=data.get('name', ''),
            language=data.get('language', ''),
            gender=data.get('gender')
        )


class HeyGenAPIError(Exception):
    """Custom exception for HeyGen API errors."""
    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[Dict] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class HeyGenClient:
    """
    HeyGen API client for video generation.

    Handles authentication, request retries, and all API interactions
    for generating AI avatar videos.
    """

    BASE_URL = "https://api.heygen.com"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the HeyGen client.

        Args:
            api_key: HeyGen API key. If not provided, reads from HEYGEN_API_KEY env var.

        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        self.api_key = api_key or os.getenv('HEYGEN_API_KEY')
        if not self.api_key:
            raise ValueError(
                "HeyGen API key is required. Provide it as an argument or set HEYGEN_API_KEY environment variable."
            )

        # Configure session with retry logic
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        # Set default headers
        self.session.headers.update({
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        timeout: int = 30
    ) -> Dict[str, Any]:
        """
        Make an API request with error handling.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without base URL)
            data: Request body data
            params: Query parameters
            timeout: Request timeout in seconds

        Returns:
            API response as dictionary

        Raises:
            HeyGenAPIError: If the API returns an error
        """
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=timeout
            )

            response_data = response.json() if response.content else {}

            if not response.ok:
                error_msg = response_data.get('message', response_data.get('error', 'Unknown error'))
                raise HeyGenAPIError(
                    f"API request failed: {error_msg}",
                    status_code=response.status_code,
                    response=response_data
                )

            return response_data

        except requests.exceptions.RequestException as e:
            raise HeyGenAPIError(f"Request failed: {str(e)}")

    def list_avatars(self) -> List[Avatar]:
        """
        List all available avatars.

        Returns:
            List of Avatar objects

        Raises:
            HeyGenAPIError: If the API request fails
        """
        logger.info("Fetching available avatars...")
        response = self._make_request('GET', '/v2/avatars')

        avatars = []
        avatar_data = response.get('data', {}).get('avatars', [])

        for item in avatar_data:
            avatars.append(Avatar.from_api_response(item))

        # Also include talking photos if available
        talking_photos = response.get('data', {}).get('talking_photos', [])
        for item in talking_photos:
            item['type'] = 'talking_photo'
            avatars.append(Avatar.from_api_response(item))

        logger.info(f"Found {len(avatars)} avatars")
        return avatars

    def list_voices(self) -> List[Voice]:
        """
        List all available voices.

        Returns:
            List of Voice objects

        Raises:
            HeyGenAPIError: If the API request fails
        """
        logger.info("Fetching available voices...")
        response = self._make_request('GET', '/v2/voices')

        voices = []
        voice_data = response.get('data', {}).get('voices', [])

        for item in voice_data:
            voices.append(Voice.from_api_response(item))

        logger.info(f"Found {len(voices)} voices")
        return voices

    def generate_video(
        self,
        script_text: str,
        avatar_id: str,
        voice_id: str,
        title: Optional[str] = None,
        test_mode: bool = False,
        dimension: Optional[Dict[str, int]] = None,
        caption: bool = False,
        background: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Generate a video from script text.

        Args:
            script_text: The text for the avatar to speak (max 5000 chars)
            avatar_id: ID of the avatar to use
            voice_id: ID of the voice to use
            title: Optional title for the video
            test_mode: If True, generates a test video (faster, lower quality)
            dimension: Video dimensions, e.g., {"width": 1280, "height": 720}
            caption: Whether to include captions
            background: Background configuration

        Returns:
            video_id for tracking the generation status

        Raises:
            HeyGenAPIError: If the API request fails
            ValueError: If script_text exceeds 5000 characters
        """
        if len(script_text) > 5000:
            raise ValueError(f"Script text exceeds 5000 character limit (got {len(script_text)})")

        logger.info(f"Generating video with avatar '{avatar_id}' and voice '{voice_id}'")
        logger.info(f"Script length: {len(script_text)} characters")

        # Build the request payload
        video_input = {
            "character": {
                "type": "avatar",
                "avatar_id": avatar_id,
                "avatar_style": "normal"
            },
            "voice": {
                "type": "text",
                "input_text": script_text,
                "voice_id": voice_id
            }
        }

        # Add optional background
        if background:
            video_input["background"] = background

        payload = {
            "video_inputs": [video_input],
            "test": test_mode,
            "caption": caption
        }

        if title:
            payload["title"] = title

        if dimension:
            payload["dimension"] = dimension
        else:
            # Default to 1080p
            payload["dimension"] = {"width": 1920, "height": 1080}

        response = self._make_request('POST', '/v2/video/generate', data=payload)

        video_id = response.get('data', {}).get('video_id')
        if not video_id:
            raise HeyGenAPIError("No video_id returned in response", response=response)

        logger.info(f"Video generation started. Video ID: {video_id}")
        return video_id

    def get_video_status(self, video_id: str) -> VideoGenerationResult:
        """
        Check the status of a video generation.

        Args:
            video_id: The ID of the video to check

        Returns:
            VideoGenerationResult with current status and video URL if completed

        Raises:
            HeyGenAPIError: If the API request fails
        """
        response = self._make_request('GET', f'/v1/video_status.get', params={'video_id': video_id})

        data = response.get('data', {})
        status_str = data.get('status', 'pending')

        try:
            status = VideoStatus(status_str)
        except ValueError:
            status = VideoStatus.PENDING

        return VideoGenerationResult(
            video_id=video_id,
            status=status,
            video_url=data.get('video_url'),
            error_message=data.get('error'),
            duration=data.get('duration')
        )

    def wait_for_video(
        self,
        video_id: str,
        poll_interval: int = 10,
        max_wait_time: int = 600,
        callback: Optional[callable] = None
    ) -> VideoGenerationResult:
        """
        Poll for video completion with async polling.

        Args:
            video_id: The ID of the video to wait for
            poll_interval: Seconds between status checks
            max_wait_time: Maximum seconds to wait before timing out
            callback: Optional callback function called with each status update

        Returns:
            VideoGenerationResult with final status

        Raises:
            HeyGenAPIError: If the video generation fails
            TimeoutError: If max_wait_time is exceeded
        """
        logger.info(f"Waiting for video {video_id} to complete...")
        start_time = time.time()

        while True:
            elapsed = time.time() - start_time
            if elapsed > max_wait_time:
                raise TimeoutError(f"Video generation timed out after {max_wait_time} seconds")

            result = self.get_video_status(video_id)

            if callback:
                callback(result)

            if result.status == VideoStatus.COMPLETED:
                logger.info(f"Video completed! Duration: {result.duration}s")
                return result

            if result.status == VideoStatus.FAILED:
                raise HeyGenAPIError(
                    f"Video generation failed: {result.error_message or 'Unknown error'}",
                    response={'video_id': video_id, 'status': 'failed'}
                )

            logger.info(f"Video status: {result.status.value} (elapsed: {int(elapsed)}s)")
            time.sleep(poll_interval)

    def download_video(
        self,
        video_url: str,
        output_path: str,
        chunk_size: int = 8192
    ) -> str:
        """
        Download a completed video.

        Args:
            video_url: URL of the video to download
            output_path: Path where the video will be saved
            chunk_size: Size of download chunks in bytes

        Returns:
            Path to the downloaded video file

        Raises:
            HeyGenAPIError: If the download fails
        """
        logger.info(f"Downloading video to {output_path}")

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            response = requests.get(video_url, stream=True, timeout=300)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = (downloaded / total_size) * 100
                            logger.debug(f"Download progress: {progress:.1f}%")

            logger.info(f"Video downloaded successfully: {output_path}")
            return str(output_path)

        except requests.exceptions.RequestException as e:
            raise HeyGenAPIError(f"Failed to download video: {str(e)}")

    def generate_and_download(
        self,
        script_text: str,
        avatar_id: str,
        voice_id: str,
        output_path: str,
        **kwargs
    ) -> Tuple[str, str]:
        """
        Convenience method to generate a video and download it.

        Args:
            script_text: Text for the avatar to speak
            avatar_id: ID of the avatar
            voice_id: ID of the voice
            output_path: Where to save the video
            **kwargs: Additional arguments passed to generate_video

        Returns:
            Tuple of (video_id, downloaded_file_path)
        """
        video_id = self.generate_video(script_text, avatar_id, voice_id, **kwargs)
        result = self.wait_for_video(video_id)

        if result.video_url:
            file_path = self.download_video(result.video_url, output_path)
            return video_id, file_path
        else:
            raise HeyGenAPIError("Video completed but no URL provided", response={'video_id': video_id})


def process_batch(
    client: HeyGenClient,
    scripts_dir: str,
    output_dir: str,
    avatar_id: str,
    voice_id: str,
    file_extension: str = ".txt"
) -> List[Dict[str, Any]]:
    """
    Process multiple script files in batch.

    Args:
        client: HeyGenClient instance
        scripts_dir: Directory containing script files
        output_dir: Directory for output videos
        avatar_id: ID of the avatar to use
        voice_id: ID of the voice to use
        file_extension: Extension of script files to process

    Returns:
        List of results with status for each script
    """
    scripts_path = Path(scripts_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    script_files = list(scripts_path.glob(f"*{file_extension}"))
    logger.info(f"Found {len(script_files)} script files to process")

    results = []

    for idx, script_file in enumerate(script_files, 1):
        logger.info(f"\n{'='*50}")
        logger.info(f"Processing [{idx}/{len(script_files)}]: {script_file.name}")
        logger.info('='*50)

        result = {
            "script_file": str(script_file),
            "status": "pending",
            "video_id": None,
            "output_path": None,
            "error": None
        }

        try:
            # Read script content
            script_text = script_file.read_text(encoding='utf-8').strip()

            if not script_text:
                result["status"] = "skipped"
                result["error"] = "Empty script file"
                logger.warning(f"Skipping {script_file.name}: empty file")
                results.append(result)
                continue

            # Generate video
            output_file = output_path / f"{script_file.stem}.mp4"
            video_id, downloaded_path = client.generate_and_download(
                script_text=script_text,
                avatar_id=avatar_id,
                voice_id=voice_id,
                output_path=str(output_file),
                title=script_file.stem
            )

            result["status"] = "completed"
            result["video_id"] = video_id
            result["output_path"] = downloaded_path

        except HeyGenAPIError as e:
            result["status"] = "failed"
            result["error"] = str(e)
            logger.error(f"Failed to process {script_file.name}: {e}")

        except Exception as e:
            result["status"] = "error"
            result["error"] = str(e)
            logger.error(f"Unexpected error processing {script_file.name}: {e}")

        results.append(result)

    # Summary
    completed = sum(1 for r in results if r["status"] == "completed")
    failed = sum(1 for r in results if r["status"] in ["failed", "error"])
    skipped = sum(1 for r in results if r["status"] == "skipped")

    logger.info(f"\n{'='*50}")
    logger.info("BATCH PROCESSING COMPLETE")
    logger.info(f"  Completed: {completed}")
    logger.info(f"  Failed: {failed}")
    logger.info(f"  Skipped: {skipped}")
    logger.info('='*50)

    return results


def main():
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description="Generate AI avatar videos using HeyGen API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List available avatars
  python heygen-avatar-generator.py --list-avatars

  # List available voices
  python heygen-avatar-generator.py --list-voices

  # Generate a single video from script file
  python heygen-avatar-generator.py --script script.txt --avatar <avatar_id> --voice <voice_id> --output video.mp4

  # Generate from inline text
  python heygen-avatar-generator.py --text "Hello, welcome to Support Forge!" --avatar <avatar_id> --voice <voice_id>

  # Batch process multiple scripts
  python heygen-avatar-generator.py --batch ./scripts --output ./videos --avatar <avatar_id> --voice <voice_id>

Environment Variables:
  HEYGEN_API_KEY    Your HeyGen API key (required)
        """
    )

    # Action arguments
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('--list-avatars', action='store_true', help='List available avatars')
    action_group.add_argument('--list-voices', action='store_true', help='List available voices')
    action_group.add_argument('--script', type=str, help='Path to script file')
    action_group.add_argument('--text', type=str, help='Inline script text')
    action_group.add_argument('--batch', type=str, help='Directory containing script files for batch processing')
    action_group.add_argument('--status', type=str, help='Check status of a video by ID')

    # Video generation options
    parser.add_argument('--avatar', type=str, help='Avatar ID to use')
    parser.add_argument('--voice', type=str, help='Voice ID to use')
    parser.add_argument('--output', type=str, help='Output path for video(s)')
    parser.add_argument('--title', type=str, help='Title for the video')
    parser.add_argument('--test', action='store_true', help='Generate in test mode (faster, lower quality)')
    parser.add_argument('--caption', action='store_true', help='Include captions in video')
    parser.add_argument('--width', type=int, default=1920, help='Video width (default: 1920)')
    parser.add_argument('--height', type=int, default=1080, help='Video height (default: 1080)')

    # General options
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--api-key', type=str, help='HeyGen API key (or use HEYGEN_API_KEY env var)')

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Initialize client
    try:
        client = HeyGenClient(api_key=args.api_key)
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    # Handle actions
    try:
        if args.list_avatars:
            avatars = client.list_avatars()
            print("\nAvailable Avatars:")
            print("-" * 80)
            for avatar in avatars:
                print(f"  ID: {avatar.avatar_id}")
                print(f"  Name: {avatar.avatar_name}")
                print(f"  Type: {avatar.avatar_type}")
                print("-" * 40)

        elif args.list_voices:
            voices = client.list_voices()
            print("\nAvailable Voices:")
            print("-" * 80)
            for voice in voices:
                print(f"  ID: {voice.voice_id}")
                print(f"  Name: {voice.name}")
                print(f"  Language: {voice.language}")
                if voice.gender:
                    print(f"  Gender: {voice.gender}")
                print("-" * 40)

        elif args.status:
            result = client.get_video_status(args.status)
            print(f"\nVideo Status: {result.status.value}")
            if result.video_url:
                print(f"Video URL: {result.video_url}")
            if result.duration:
                print(f"Duration: {result.duration}s")
            if result.error_message:
                print(f"Error: {result.error_message}")

        elif args.script or args.text:
            if not args.avatar or not args.voice:
                logger.error("--avatar and --voice are required for video generation")
                sys.exit(1)

            # Get script text
            if args.script:
                script_path = Path(args.script)
                if not script_path.exists():
                    logger.error(f"Script file not found: {args.script}")
                    sys.exit(1)
                script_text = script_path.read_text(encoding='utf-8').strip()
            else:
                script_text = args.text

            # Determine output path
            output_path = args.output
            if not output_path:
                if args.script:
                    output_path = Path(args.script).stem + ".mp4"
                else:
                    output_path = "output.mp4"

            # Generate video
            video_id, downloaded_path = client.generate_and_download(
                script_text=script_text,
                avatar_id=args.avatar,
                voice_id=args.voice,
                output_path=output_path,
                title=args.title,
                test_mode=args.test,
                caption=args.caption,
                dimension={"width": args.width, "height": args.height}
            )

            print(f"\nVideo generated successfully!")
            print(f"Video ID: {video_id}")
            print(f"Saved to: {downloaded_path}")

        elif args.batch:
            if not args.avatar or not args.voice:
                logger.error("--avatar and --voice are required for batch processing")
                sys.exit(1)

            if not args.output:
                logger.error("--output directory is required for batch processing")
                sys.exit(1)

            results = process_batch(
                client=client,
                scripts_dir=args.batch,
                output_dir=args.output,
                avatar_id=args.avatar,
                voice_id=args.voice
            )

            # Save results to JSON
            results_file = Path(args.output) / "batch_results.json"
            with open(results_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nBatch results saved to: {results_file}")

        else:
            parser.print_help()

    except HeyGenAPIError as e:
        logger.error(f"API Error: {e}")
        if e.response:
            logger.debug(f"Response: {json.dumps(e.response, indent=2)}")
        sys.exit(1)

    except KeyboardInterrupt:
        logger.info("\nOperation cancelled by user")
        sys.exit(130)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
