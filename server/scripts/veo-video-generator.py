#!/usr/bin/env python3
"""
Veo Video Generator for Support Forge
=====================================

Generates video content using Google's Veo 3 on Vertex AI.
Supports text-to-video and image-to-video generation for B-roll content.

Requirements:
    pip install google-genai google-cloud-storage pillow

Environment Setup (Vertex AI):
    export GOOGLE_CLOUD_PROJECT=your-project-id
    export GOOGLE_CLOUD_LOCATION=global
    export GOOGLE_GENAI_USE_VERTEXAI=True

Usage:
    python veo-video-generator.py

References:
    - https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/overview
    - https://github.com/googleapis/python-genai
"""

import os
import sys
import time
import logging
from pathlib import Path
from typing import Optional, Literal
from dataclasses import dataclass

try:
    from google import genai
    from google.genai import types
    from google.genai.types import GenerateVideosConfig, Image
except ImportError:
    print("Error: google-genai package not installed.")
    print("Install with: pip install google-genai")
    sys.exit(1)

try:
    from PIL import Image as PILImage
except ImportError:
    PILImage = None
    print("Warning: PIL not installed. Image loading from local files limited.")
    print("Install with: pip install pillow")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class VideoConfig:
    """Configuration for video generation."""
    aspect_ratio: Literal["16:9", "9:16"] = "16:9"
    duration_seconds: Literal[4, 5, 6, 7, 8] = 8
    number_of_videos: int = 1
    person_generation: Literal["dont_allow", "allow_adult"] = "dont_allow"
    resolution: Literal["720p", "1080p"] = "720p"
    negative_prompt: Optional[str] = None
    output_gcs_uri: Optional[str] = None


class VeoVideoGenerator:
    """
    Veo Video Generator using Google's Vertex AI.

    Supports:
    - Text-to-video generation for B-roll content
    - Image-to-video generation for animated diagrams
    - Async job polling with progress tracking
    - Local and GCS video output
    """

    # Available Veo models (newest first)
    MODELS = {
        "veo-3.1": "veo-3.1-generate-001",      # Latest with audio
        "veo-3.0": "veo-3.0-generate-001",      # Stable release
        "veo-3.0-fast": "veo-3.0-fast-generate-001",  # Faster generation
    }

    DEFAULT_MODEL = "veo-3.0-fast"  # Good balance of speed/quality
    POLL_INTERVAL = 15  # seconds between status checks
    MAX_POLL_TIME = 600  # maximum wait time (10 minutes)

    def __init__(
        self,
        project_id: Optional[str] = None,
        location: str = "global",
        model: str = DEFAULT_MODEL
    ):
        """
        Initialize the Veo Video Generator.

        Args:
            project_id: Google Cloud project ID. Uses env var if not provided.
            location: Vertex AI location. Default "global" for Veo.
            model: Model version to use. See MODELS for options.
        """
        self.project_id = project_id or os.environ.get("GOOGLE_CLOUD_PROJECT")
        self.location = location

        if model in self.MODELS:
            self.model = self.MODELS[model]
        else:
            self.model = model

        # Ensure Vertex AI mode is enabled
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
        if self.project_id:
            os.environ["GOOGLE_CLOUD_PROJECT"] = self.project_id
        os.environ["GOOGLE_CLOUD_LOCATION"] = self.location

        # Initialize the client
        self.client = genai.Client()
        logger.info(f"Initialized VeoVideoGenerator with model: {self.model}")

    def generate_from_text(
        self,
        prompt: str,
        output_path: Optional[str] = None,
        config: Optional[VideoConfig] = None
    ) -> list[str]:
        """
        Generate video from a text prompt.

        Args:
            prompt: Text description of the video to generate.
            output_path: Local path to save video(s). Auto-generated if not provided.
            config: Video configuration options.

        Returns:
            List of paths to saved video files.
        """
        config = config or VideoConfig()

        logger.info(f"Generating video from prompt: '{prompt[:50]}...'")
        logger.info(f"Config: {config.aspect_ratio}, {config.duration_seconds}s, {config.resolution}")

        # Build generation config
        gen_config = self._build_config(config)

        # Start async generation
        operation = self.client.models.generate_videos(
            model=self.model,
            prompt=prompt,
            config=gen_config,
        )

        # Poll for completion
        operation = self._poll_operation(operation)

        # Download and save videos
        return self._save_videos(operation, output_path, prompt)

    def generate_from_image(
        self,
        image_source: str,
        prompt: str,
        output_path: Optional[str] = None,
        config: Optional[VideoConfig] = None
    ) -> list[str]:
        """
        Generate video from an image (animate a still image or diagram).

        Args:
            image_source: Path to local image file or GCS URI (gs://...).
            prompt: Text description of how to animate the image.
            output_path: Local path to save video(s). Auto-generated if not provided.
            config: Video configuration options.

        Returns:
            List of paths to saved video files.
        """
        config = config or VideoConfig()

        logger.info(f"Generating video from image: {image_source}")
        logger.info(f"Animation prompt: '{prompt[:50]}...'")

        # Load image based on source type
        image = self._load_image(image_source)

        # Build generation config
        gen_config = self._build_config(config)

        # Start async generation
        operation = self.client.models.generate_videos(
            model=self.model,
            prompt=prompt,
            image=image,
            config=gen_config,
        )

        # Poll for completion
        operation = self._poll_operation(operation)

        # Download and save videos
        return self._save_videos(operation, output_path, prompt)

    def _load_image(self, image_source: str):
        """Load image from local file or GCS URI."""
        if image_source.startswith("gs://"):
            # GCS URI - use directly
            mime_type = self._get_mime_type(image_source)
            return Image(gcs_uri=image_source, mime_type=mime_type)
        else:
            # Local file - load with PIL if available
            if PILImage is None:
                raise ImportError("PIL required for local image loading. pip install pillow")

            local_path = Path(image_source)
            if not local_path.exists():
                raise FileNotFoundError(f"Image not found: {image_source}")

            # Load and return PIL image
            return PILImage.open(local_path)

    def _get_mime_type(self, path: str) -> str:
        """Determine MIME type from file extension."""
        ext = Path(path).suffix.lower()
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }
        return mime_types.get(ext, "image/png")

    def _build_config(self, config: VideoConfig) -> GenerateVideosConfig:
        """Build GenerateVideosConfig from VideoConfig."""
        params = {
            "aspect_ratio": config.aspect_ratio,
            "number_of_videos": config.number_of_videos,
            "person_generation": config.person_generation,
        }

        # Duration is model-dependent
        if config.duration_seconds:
            params["duration_seconds"] = config.duration_seconds

        # Resolution only for Veo 3+
        if "veo-3" in self.model:
            params["resolution"] = config.resolution

        # Optional negative prompt
        if config.negative_prompt:
            params["negative_prompt"] = config.negative_prompt

        # Optional GCS output
        if config.output_gcs_uri:
            params["output_gcs_uri"] = config.output_gcs_uri

        return GenerateVideosConfig(**params)

    def _poll_operation(self, operation):
        """Poll operation until complete or timeout."""
        start_time = time.time()
        poll_count = 0

        while not operation.done:
            elapsed = time.time() - start_time
            if elapsed > self.MAX_POLL_TIME:
                raise TimeoutError(f"Video generation timed out after {self.MAX_POLL_TIME}s")

            poll_count += 1
            logger.info(f"Waiting for video generation... ({int(elapsed)}s elapsed)")

            time.sleep(self.POLL_INTERVAL)
            operation = self.client.operations.get(operation)

        total_time = time.time() - start_time
        logger.info(f"Video generation completed in {int(total_time)}s")

        return operation

    def _save_videos(
        self,
        operation,
        output_path: Optional[str],
        prompt: str
    ) -> list[str]:
        """Download and save generated videos locally."""
        saved_paths = []

        if not operation.response or not operation.response.generated_videos:
            logger.warning("No videos generated in response")
            return saved_paths

        # Generate base filename from prompt
        safe_prompt = "".join(c if c.isalnum() else "_" for c in prompt[:30])
        timestamp = int(time.time())

        for idx, generated_video in enumerate(operation.response.generated_videos):
            try:
                # Download video bytes
                self.client.files.download(file=generated_video.video)

                # Determine output path
                if output_path:
                    if len(operation.response.generated_videos) > 1:
                        path = Path(output_path)
                        save_path = path.parent / f"{path.stem}_{idx}{path.suffix}"
                    else:
                        save_path = Path(output_path)
                else:
                    save_path = Path(f"video_{safe_prompt}_{timestamp}_{idx}.mp4")

                # Ensure directory exists
                save_path.parent.mkdir(parents=True, exist_ok=True)

                # Save video
                generated_video.video.save(str(save_path))
                saved_paths.append(str(save_path))
                logger.info(f"Saved video to: {save_path}")

            except Exception as e:
                logger.error(f"Failed to save video {idx}: {e}")

        return saved_paths


def example_tech_background():
    """Generate a tech-themed B-roll background clip."""
    generator = VeoVideoGenerator()

    prompt = """
    Abstract technology background with flowing blue and purple digital particles.
    Subtle grid lines and glowing nodes connected by light trails.
    Slow camera movement forward through a network visualization.
    Clean, modern, professional aesthetic suitable for tech company video.
    Soft ambient lighting with subtle lens flares.
    """

    config = VideoConfig(
        aspect_ratio="16:9",
        duration_seconds=8,
        resolution="1080p",
        negative_prompt="people, faces, text, logos, watermarks"
    )

    output_path = "output/tech_background.mp4"

    videos = generator.generate_from_text(prompt, output_path, config)
    print(f"Generated tech background: {videos}")
    return videos


def example_ai_assistant():
    """Generate an AI assistant themed clip."""
    generator = VeoVideoGenerator()

    prompt = """
    Sleek holographic AI assistant interface floating in a modern office space.
    Glowing circular display with data visualizations and flowing information.
    Subtle particle effects around the hologram.
    Cool blue and white color palette with soft shadows.
    Gentle ambient movement and pulsing light effects.
    Cinematic depth of field with bokeh in background.
    """

    config = VideoConfig(
        aspect_ratio="16:9",
        duration_seconds=6,
        resolution="1080p",
        person_generation="dont_allow",
        negative_prompt="realistic humans, faces, text overlays"
    )

    output_path = "output/ai_assistant.mp4"

    videos = generator.generate_from_text(prompt, output_path, config)
    print(f"Generated AI assistant clip: {videos}")
    return videos


def example_animated_diagram():
    """Animate a static diagram image into video."""
    generator = VeoVideoGenerator()

    # Path to your diagram image (local or GCS)
    # For demo, using a placeholder - replace with actual diagram path
    image_path = "diagrams/system_architecture.png"

    # Check if demo image exists, create instructions if not
    if not Path(image_path).exists():
        print(f"Note: Place your diagram at '{image_path}' before running.")
        print("Using GCS sample image for demonstration...")
        image_path = "gs://cloud-samples-data/generative-ai/image/flowers.png"

    prompt = """
    Smooth animation of the diagram elements.
    Components fade in sequentially from left to right.
    Connecting lines draw themselves between elements.
    Subtle glow effects highlight active connections.
    Professional technical presentation style.
    Camera slowly zooms out to reveal full diagram.
    """

    config = VideoConfig(
        aspect_ratio="16:9",
        duration_seconds=8,
        resolution="720p",
        person_generation="dont_allow"
    )

    output_path = "output/animated_diagram.mp4"

    videos = generator.generate_from_image(image_path, prompt, output_path, config)
    print(f"Generated animated diagram: {videos}")
    return videos


def batch_generate_broll(prompts: list[dict], output_dir: str = "output/broll"):
    """
    Generate multiple B-roll clips from a list of prompts.

    Args:
        prompts: List of dicts with 'name' and 'prompt' keys.
        output_dir: Directory to save all generated videos.
    """
    generator = VeoVideoGenerator(model="veo-3.0-fast")  # Use fast model for batch
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    config = VideoConfig(
        aspect_ratio="16:9",
        duration_seconds=6,
        resolution="720p",
        person_generation="dont_allow",
        negative_prompt="text, watermarks, logos"
    )

    results = []
    for item in prompts:
        name = item["name"]
        prompt = item["prompt"]

        try:
            logger.info(f"Generating B-roll: {name}")
            video_path = output_path / f"{name}.mp4"
            videos = generator.generate_from_text(prompt, str(video_path), config)
            results.append({"name": name, "status": "success", "paths": videos})
        except Exception as e:
            logger.error(f"Failed to generate {name}: {e}")
            results.append({"name": name, "status": "error", "error": str(e)})

    return results


if __name__ == "__main__":
    # Ensure output directory exists
    Path("output").mkdir(exist_ok=True)

    print("=" * 60)
    print("Veo Video Generator for Support Forge")
    print("=" * 60)
    print()

    # Check environment
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project:
        print("WARNING: GOOGLE_CLOUD_PROJECT not set!")
        print("Set with: export GOOGLE_CLOUD_PROJECT=your-project-id")
        print()
    else:
        print(f"Using project: {project}")

    print()
    print("Available examples:")
    print("  1. Tech background B-roll")
    print("  2. AI assistant themed clip")
    print("  3. Animated diagram from image")
    print("  4. Batch B-roll generation")
    print()

    # Interactive mode
    choice = input("Enter choice (1-4) or 'q' to quit: ").strip()

    if choice == "1":
        example_tech_background()
    elif choice == "2":
        example_ai_assistant()
    elif choice == "3":
        example_animated_diagram()
    elif choice == "4":
        # Batch example with Support Forge themed prompts
        broll_prompts = [
            {
                "name": "data_flow",
                "prompt": "Abstract data flowing through neural network visualization, blue glowing particles traveling along connection lines, dark background, smooth animation"
            },
            {
                "name": "cloud_infrastructure",
                "prompt": "Minimalist cloud computing infrastructure diagram coming to life, server icons pulsing with activity, connections forming between nodes, professional tech aesthetic"
            },
            {
                "name": "code_typing",
                "prompt": "Close-up of clean code appearing on a modern dark IDE interface, syntax highlighting in blue and green, professional developer workspace feel, no visible screen edge"
            },
            {
                "name": "customer_support",
                "prompt": "Abstract representation of support tickets being resolved, geometric shapes transforming from red to green, flowing efficiency visualization, modern corporate style"
            }
        ]
        results = batch_generate_broll(broll_prompts)
        print("\nBatch Results:")
        for r in results:
            status = "SUCCESS" if r["status"] == "success" else "FAILED"
            print(f"  {r['name']}: {status}")
    elif choice.lower() == "q":
        print("Exiting.")
    else:
        print("Invalid choice.")

    print()
    print("Done!")
