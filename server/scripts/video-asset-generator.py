#!/usr/bin/env python3
"""
Video Asset Generator
=====================
Generates visual assets for video production from parsed script JSON files.

Uses:
- Canva via Zapier MCP for branded graphics/slides
- Google Gemini via Zapier MCP for AI-generated illustrations
- Placeholder generation for screen captures requiring manual recording

Usage:
    python video-asset-generator.py --script parsed-scripts/script-0.1.json
    python video-asset-generator.py --all
    python video-asset-generator.py --type title_cards
    python video-asset-generator.py --parse-only scripts/script-0.1-welcome.md

Author: AI Launchpad Academy
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Optional
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(path=None):
        """Stub if python-dotenv not installed."""
        pass

try:
    import requests
except ImportError:
    requests = None  # Will work in dry-run mode

# ============================================================================
# Constants and Configuration
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
ENV_FILE = SCRIPT_DIR / ".env.video"
OUTPUT_BASE = SCRIPT_DIR / "output" / "assets"
PARSED_SCRIPTS_DIR = SCRIPT_DIR / "output" / "parsed-scripts"
RAW_SCRIPTS_DIR = SCRIPT_DIR.parent.parent / "docs" / "academy-content" / "video-scripts"

# Brand colors from video-config.json
BRAND_PRIMARY = "#8B5CF6"  # Purple
BRAND_SECONDARY = "#1E1B4B"  # Dark background
BRAND_FONT = "Inter"

# Load environment variables
load_dotenv(ENV_FILE)


# ============================================================================
# Enums and Data Classes
# ============================================================================

class AssetType(Enum):
    TITLE_CARD = "title_card"
    CONTENT_SLIDE = "content_slide"
    COMPARISON_TABLE = "comparison_table"
    BULLET_POINTS = "bullet_points"
    END_CARD = "end_card"
    ILLUSTRATION = "illustration"
    FLOWCHART = "flowchart"
    ICON_SET = "icon_set"
    UI_MOCKUP = "ui_mockup"
    SCREEN_CAPTURE = "screen_capture"
    LOGO_ANIMATION = "logo_animation"
    QUOTE_CALLOUT = "quote_callout"
    UNKNOWN = "unknown"


class GenerationStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    NEEDS_RECORDING = "needs_recording"
    SKIPPED = "skipped"


@dataclass
class VisualCue:
    """Represents a visual cue extracted from a script."""
    index: int
    raw_text: str
    asset_type: AssetType
    description: str
    context: str = ""
    section: str = ""
    filename: str = ""
    status: GenerationStatus = GenerationStatus.PENDING
    output_path: Optional[str] = None
    error: Optional[str] = None
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dictionary."""
        return {
            "index": self.index,
            "raw_text": self.raw_text,
            "asset_type": self.asset_type.value if isinstance(self.asset_type, Enum) else self.asset_type,
            "description": self.description,
            "context": self.context,
            "section": self.section,
            "filename": self.filename,
            "status": self.status.value if isinstance(self.status, Enum) else self.status,
            "output_path": self.output_path,
            "error": self.error,
            "metadata": self.metadata
        }


@dataclass
class ParsedScript:
    """Represents a parsed video script with extracted visual cues."""
    script_id: str
    title: str
    module: str
    lesson: str
    duration: str
    purpose: str
    sections: list
    visual_cues: list
    raw_content: str
    parsed_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dictionary."""
        return {
            "script_id": self.script_id,
            "title": self.title,
            "module": self.module,
            "lesson": self.lesson,
            "duration": self.duration,
            "purpose": self.purpose,
            "sections": self.sections,
            "visual_cues": self.visual_cues,  # Already converted
            "raw_content": self.raw_content,
            "parsed_at": self.parsed_at
        }


# ============================================================================
# Logging Setup
# ============================================================================

def setup_logging(verbose: bool = False) -> logging.Logger:
    """Configure logging with console handler."""
    logger = logging.getLogger("video-asset-generator")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# ============================================================================
# Script Parser
# ============================================================================

class ScriptParser:
    """Parse video scripts and extract visual cues."""

    # Patterns for detecting visual cue types
    TYPE_PATTERNS = {
        AssetType.TITLE_CARD: [
            r"title\s*card", r"module.*title", r"lesson\s+title",
            r"logo\s+animation", r"opening.*title"
        ],
        AssetType.END_CARD: [
            r"fade\s+to", r"next:?\s+", r"end\s*card", r"closing",
            r"support\s+forge\s+branding"
        ],
        AssetType.COMPARISON_TABLE: [
            r"comparison", r"versus", r"vs\.", r"table\s+showing",
            r"side[- ]by[- ]side"
        ],
        AssetType.BULLET_POINTS: [
            r"bullet\s*points?", r"list\s+of", r"checklist",
            r"points?\s+appearing"
        ],
        AssetType.FLOWCHART: [
            r"flowchart", r"diagram", r"workflow", r"flow\s+showing",
            r"process\s+diagram"
        ],
        AssetType.ILLUSTRATION: [
            r"visualization?", r"visual\s+showing", r"image",
            r"graphic\s+of", r"icon"
        ],
        AssetType.UI_MOCKUP: [
            r"dashboard", r"interface", r"screen\s+showing",
            r"ui", r"mockup"
        ],
        AssetType.SCREEN_CAPTURE: [
            r"terminal", r"command", r"code", r"window",
            r"browser", r"powershell", r"installation",
            r"npm", r"login", r"website"
        ],
        AssetType.QUOTE_CALLOUT: [
            r"quote", r"callout", r"highlight", r"emphasis"
        ],
        AssetType.LOGO_ANIMATION: [
            r"logo\s+animation", r"branding\s+animation"
        ]
    }

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def parse_markdown(self, filepath: Path) -> ParsedScript:
        """Parse a markdown script file into structured data."""
        content = filepath.read_text(encoding="utf-8")

        # Extract metadata from header
        metadata = self._extract_metadata(content)

        # Extract sections
        sections = self._extract_sections(content)

        # Extract visual cues
        visual_cues = self._extract_visual_cues(content, sections)

        # Generate script ID from filename
        script_id = filepath.stem

        return ParsedScript(
            script_id=script_id,
            title=metadata.get("title", script_id),
            module=metadata.get("module", ""),
            lesson=metadata.get("lesson", ""),
            duration=metadata.get("duration", ""),
            purpose=metadata.get("purpose", ""),
            sections=sections,
            visual_cues=[vc.to_dict() for vc in visual_cues],
            raw_content=content
        )

    def _extract_metadata(self, content: str) -> dict:
        """Extract metadata from script header."""
        metadata = {}

        # Title from first H1
        title_match = re.search(r"^#\s+(?:Script\s+[\d.]+:\s+)?(.+)$", content, re.MULTILINE)
        if title_match:
            metadata["title"] = title_match.group(1).strip()

        # Duration
        duration_match = re.search(r"\*\*Duration:\*\*\s*(.+)", content)
        if duration_match:
            metadata["duration"] = duration_match.group(1).strip()

        # Lesson info
        lesson_match = re.search(r"\*\*Lesson:\*\*\s*(.+)", content)
        if lesson_match:
            lesson_info = lesson_match.group(1).strip()
            metadata["lesson"] = lesson_info
            # Extract module number
            module_match = re.search(r"Module\s+(\d+)", lesson_info)
            if module_match:
                metadata["module"] = module_match.group(1)

        # Purpose
        purpose_match = re.search(r"\*\*Purpose:\*\*\s*(.+)", content)
        if purpose_match:
            metadata["purpose"] = purpose_match.group(1).strip()

        return metadata

    def _extract_sections(self, content: str) -> list:
        """Extract section headers from script."""
        sections = []
        section_pattern = re.compile(r"^##\s+(.+)$", re.MULTILINE)

        for match in section_pattern.finditer(content):
            section_name = match.group(1).strip()
            if section_name not in ["---"]:
                sections.append({
                    "name": section_name,
                    "position": match.start()
                })

        return sections

    def _extract_visual_cues(self, content: str, sections: list) -> list:
        """Extract visual cues from [SCREEN: ...] markers."""
        visual_cues = []

        # Pattern to match [SCREEN: ...] markers
        screen_pattern = re.compile(r"\[SCREEN:\s*(.+?)\]", re.IGNORECASE | re.DOTALL)

        for idx, match in enumerate(screen_pattern.finditer(content)):
            raw_text = match.group(1).strip()
            position = match.start()

            # Determine which section this cue belongs to
            current_section = ""
            for section in sections:
                if section["position"] < position:
                    current_section = section["name"]

            # Get surrounding context (text before and after)
            context_start = max(0, position - 200)
            context_end = min(len(content), match.end() + 200)
            context = content[context_start:context_end]

            # Determine asset type
            asset_type = self._classify_visual_cue(raw_text)

            # Generate filename
            filename = self._generate_filename(idx + 1, asset_type, raw_text)

            visual_cue = VisualCue(
                index=idx + 1,
                raw_text=raw_text,
                asset_type=asset_type,
                description=raw_text,
                context=context,
                section=current_section,
                filename=filename,
                status=GenerationStatus.PENDING
            )

            visual_cues.append(visual_cue)

        self.logger.info(f"Extracted {len(visual_cues)} visual cues")
        return visual_cues

    def _classify_visual_cue(self, text: str) -> AssetType:
        """Classify a visual cue into an asset type."""
        text_lower = text.lower()

        for asset_type, patterns in self.TYPE_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    return asset_type

        # Default classification based on keywords
        if any(word in text_lower for word in ["heading", "title", "module", "phase"]):
            return AssetType.TITLE_CARD
        elif any(word in text_lower for word in ["roi", "hours", "visualization"]):
            return AssetType.ILLUSTRATION

        return AssetType.CONTENT_SLIDE

    def _generate_filename(self, index: int, asset_type: AssetType, description: str) -> str:
        """Generate a descriptive filename for an asset."""
        # Clean description for filename
        clean_desc = re.sub(r'[^\w\s-]', '', description.lower())
        clean_desc = re.sub(r'\s+', '_', clean_desc)
        clean_desc = clean_desc[:40]  # Limit length

        return f"segment_{index:03d}_{asset_type.value}_{clean_desc}.png"


# ============================================================================
# Asset Templates
# ============================================================================

class AssetTemplates:
    """Template definitions for brand-consistent assets."""

    TITLE_SLIDE = {
        "type": "title_slide",
        "dimensions": {"width": 1920, "height": 1080},
        "background_color": BRAND_SECONDARY,
        "elements": [
            {"type": "logo", "position": "top_center", "size": "medium"},
            {"type": "title", "position": "center", "font": BRAND_FONT, "color": "#FFFFFF", "size": 72},
            {"type": "subtitle", "position": "below_title", "font": BRAND_FONT, "color": BRAND_PRIMARY, "size": 36}
        ]
    }

    CONTENT_SLIDE = {
        "type": "content_slide",
        "dimensions": {"width": 1920, "height": 1080},
        "background_color": BRAND_SECONDARY,
        "elements": [
            {"type": "header", "position": "top_left", "font": BRAND_FONT, "color": BRAND_PRIMARY, "size": 48},
            {"type": "bullet_list", "position": "center_left", "font": BRAND_FONT, "color": "#FFFFFF", "size": 32},
            {"type": "accent_bar", "position": "left_edge", "color": BRAND_PRIMARY, "width": 8}
        ]
    }

    COMPARISON_TABLE = {
        "type": "comparison_table",
        "dimensions": {"width": 1920, "height": 1080},
        "background_color": BRAND_SECONDARY,
        "columns": 2,
        "elements": [
            {"type": "header", "position": "top_center", "font": BRAND_FONT, "color": "#FFFFFF", "size": 48},
            {"type": "column_headers", "font": BRAND_FONT, "color": BRAND_PRIMARY, "size": 36},
            {"type": "table_content", "font": BRAND_FONT, "color": "#FFFFFF", "size": 28}
        ]
    }

    END_CARD = {
        "type": "end_card",
        "dimensions": {"width": 1920, "height": 1080},
        "background_color": BRAND_SECONDARY,
        "elements": [
            {"type": "next_lesson_text", "position": "center", "font": BRAND_FONT, "color": "#FFFFFF", "size": 48},
            {"type": "lesson_title", "position": "below_center", "font": BRAND_FONT, "color": BRAND_PRIMARY, "size": 36},
            {"type": "logo", "position": "bottom_right", "size": "small"},
            {"type": "branding_bar", "position": "bottom", "color": BRAND_PRIMARY, "height": 4}
        ]
    }

    QUOTE_CALLOUT = {
        "type": "quote_callout",
        "dimensions": {"width": 1920, "height": 1080},
        "background_color": BRAND_SECONDARY,
        "elements": [
            {"type": "quote_marks", "position": "top_left", "color": BRAND_PRIMARY, "size": 120},
            {"type": "quote_text", "position": "center", "font": BRAND_FONT, "color": "#FFFFFF", "size": 48, "style": "italic"},
            {"type": "attribution", "position": "bottom_right", "font": BRAND_FONT, "color": BRAND_PRIMARY, "size": 24}
        ]
    }

    @classmethod
    def get_template(cls, asset_type: AssetType) -> dict:
        """Get template for a specific asset type."""
        templates = {
            AssetType.TITLE_CARD: cls.TITLE_SLIDE,
            AssetType.CONTENT_SLIDE: cls.CONTENT_SLIDE,
            AssetType.BULLET_POINTS: cls.CONTENT_SLIDE,
            AssetType.COMPARISON_TABLE: cls.COMPARISON_TABLE,
            AssetType.END_CARD: cls.END_CARD,
            AssetType.QUOTE_CALLOUT: cls.QUOTE_CALLOUT
        }
        return templates.get(asset_type, cls.CONTENT_SLIDE)


# ============================================================================
# Canva Generator (via Zapier MCP)
# ============================================================================

class CanvaGenerator:
    """Generate graphics using Canva via Zapier MCP tools."""

    def __init__(self, logger: logging.Logger, dry_run: bool = False):
        self.logger = logger
        self.dry_run = dry_run
        self.zapier_base_url = "https://actions.zapier.com/api/v2"

    def create_title_card(self, title: str, subtitle: str = "", output_path: Path = None) -> dict:
        """Create a title card design in Canva."""
        template = AssetTemplates.get_template(AssetType.TITLE_CARD)

        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would create title card: {title}")
            return {
                "success": True,
                "dry_run": True,
                "asset_type": "title_card",
                "title": title,
                "output_path": str(output_path) if output_path else None
            }

        # Build Canva creation instructions
        instructions = f"""Create a title slide with:
- Background color: {BRAND_SECONDARY} (dark purple)
- Title text: "{title}" in white, centered, {BRAND_FONT} font, 72px
- Subtitle: "{subtitle}" in {BRAND_PRIMARY} (purple accent), below title, 36px
- Dimensions: 1920x1080 (HD video)
- Clean, modern, professional look
- No additional decorative elements
"""

        self.logger.info(f"Creating title card via Canva: {title}")

        # This would call the Zapier MCP tool
        # In practice, we'd use: mcp__zapier__canva_create_design
        return {
            "success": True,
            "instructions": instructions,
            "template": template,
            "output_path": str(output_path) if output_path else None,
            "needs_mcp_call": True,
            "mcp_tool": "mcp__zapier__canva_create_design",
            "mcp_params": {
                "title": title,
                "design_type__type": "Presentation",
                "instructions": instructions
            }
        }

    def create_content_slide(self, header: str, bullets: list, output_path: Path = None) -> dict:
        """Create a content slide with bullet points."""
        template = AssetTemplates.get_template(AssetType.CONTENT_SLIDE)

        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would create content slide: {header}")
            return {
                "success": True,
                "dry_run": True,
                "asset_type": "content_slide",
                "header": header
            }

        bullet_text = "\n".join([f"- {b}" for b in bullets])
        instructions = f"""Create a content slide with:
- Background color: {BRAND_SECONDARY}
- Header: "{header}" in {BRAND_PRIMARY}, top-left, {BRAND_FONT} font, 48px
- Bullet points in white, {BRAND_FONT} font, 32px:
{bullet_text}
- Left accent bar in {BRAND_PRIMARY}, 8px wide
- Dimensions: 1920x1080
"""

        return {
            "success": True,
            "instructions": instructions,
            "template": template,
            "output_path": str(output_path) if output_path else None,
            "needs_mcp_call": True,
            "mcp_tool": "mcp__zapier__canva_create_design"
        }

    def create_comparison_table(self, header: str, columns: list, output_path: Path = None) -> dict:
        """Create a comparison table slide."""
        template = AssetTemplates.get_template(AssetType.COMPARISON_TABLE)

        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would create comparison table: {header}")
            return {"success": True, "dry_run": True}

        instructions = f"""Create a comparison table with:
- Background: {BRAND_SECONDARY}
- Header: "{header}" centered, white, 48px
- {len(columns)} columns with headers in {BRAND_PRIMARY}
- Table content in white
- Clean grid layout
- Dimensions: 1920x1080
"""

        return {
            "success": True,
            "instructions": instructions,
            "template": template,
            "needs_mcp_call": True
        }

    def create_end_card(self, next_lesson: str, branding: str = "Support Forge", output_path: Path = None) -> dict:
        """Create an end card for video closing."""
        template = AssetTemplates.get_template(AssetType.END_CARD)

        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would create end card: Next: {next_lesson}")
            return {"success": True, "dry_run": True}

        instructions = f"""Create an end card with:
- Background: {BRAND_SECONDARY}
- "Next:" text in white, centered, 48px
- "{next_lesson}" in {BRAND_PRIMARY}, below, 36px
- {branding} logo in bottom-right corner
- Subtle gradient or fade effect
- Dimensions: 1920x1080
"""

        return {
            "success": True,
            "instructions": instructions,
            "template": template,
            "needs_mcp_call": True
        }


# ============================================================================
# Gemini Image Generator (via Zapier MCP)
# ============================================================================

class GeminiImageGenerator:
    """Generate illustrations using Google Gemini via Zapier MCP."""

    def __init__(self, logger: logging.Logger, dry_run: bool = False):
        self.logger = logger
        self.dry_run = dry_run

    def generate_illustration(self, description: str, style: str = "modern", output_path: Path = None) -> dict:
        """Generate an illustration using Gemini."""
        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would generate illustration: {description[:50]}...")
            return {"success": True, "dry_run": True}

        prompt = f"""Create a professional illustration for a business training video:

Description: {description}

Style requirements:
- {style} design aesthetic
- Color palette: primary purple (#8B5CF6), dark backgrounds (#1E1B4B)
- Clean, minimalist style suitable for video production
- No text or labels (will be added separately)
- High contrast for video display
- Professional, corporate feel
- 16:9 aspect ratio (1920x1080)
"""

        self.logger.info(f"Generating illustration via Gemini: {description[:50]}...")

        return {
            "success": True,
            "prompt": prompt,
            "output_path": str(output_path) if output_path else None,
            "needs_mcp_call": True,
            "mcp_tool": "mcp__zapier__google_ai_studio_gemini_generate_image",
            "mcp_params": {
                "prompt": prompt,
                "model": "gemini-2.0-flash-exp"
            }
        }

    def generate_flowchart(self, description: str, steps: list = None, output_path: Path = None) -> dict:
        """Generate a flowchart or process diagram."""
        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would generate flowchart: {description[:50]}...")
            return {"success": True, "dry_run": True}

        steps_text = ""
        if steps:
            steps_text = "\nSteps to visualize:\n" + "\n".join([f"- {s}" for s in steps])

        prompt = f"""Create a clean flowchart/process diagram:

Description: {description}
{steps_text}

Visual requirements:
- Modern, flat design style
- Use purple (#8B5CF6) for primary elements
- Dark background (#1E1B4B) compatible
- Simple geometric shapes (rounded rectangles, circles)
- Clear directional arrows
- No text labels (they'll be overlaid)
- Professional business aesthetic
- 16:9 aspect ratio
"""

        return {
            "success": True,
            "prompt": prompt,
            "needs_mcp_call": True,
            "mcp_tool": "mcp__zapier__google_ai_studio_gemini_generate_image"
        }

    def generate_icon_set(self, concept: str, count: int = 4, output_path: Path = None) -> dict:
        """Generate a set of icons for a concept."""
        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would generate icon set: {concept}")
            return {"success": True, "dry_run": True}

        prompt = f"""Create a set of {count} simple, cohesive icons for: {concept}

Requirements:
- Minimalist line icon style
- Purple (#8B5CF6) icons on transparent/dark background
- Consistent stroke weight and style
- Professional, modern aesthetic
- Suitable for video overlays
- 1920x1080 canvas with icons arranged in a row
"""

        return {
            "success": True,
            "prompt": prompt,
            "needs_mcp_call": True,
            "mcp_tool": "mcp__zapier__google_ai_studio_gemini_generate_image"
        }

    def generate_ui_mockup(self, description: str, app_type: str = "dashboard", output_path: Path = None) -> dict:
        """Generate a UI mockup illustration."""
        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would generate UI mockup: {description[:50]}...")
            return {"success": True, "dry_run": True}

        prompt = f"""Create a stylized {app_type} UI mockup:

Description: {description}

Requirements:
- Modern, clean interface design
- Dark theme with purple (#8B5CF6) accents
- Blurred/abstract data (no readable text)
- Shows general layout and functionality concept
- Professional SaaS aesthetic
- 16:9 aspect ratio for video
"""

        return {
            "success": True,
            "prompt": prompt,
            "needs_mcp_call": True,
            "mcp_tool": "mcp__zapier__google_ai_studio_gemini_generate_image"
        }


# ============================================================================
# Screen Capture Handler
# ============================================================================

class ScreenCaptureHandler:
    """Handle screen capture requirements that need manual recording."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def flag_for_recording(self, description: str, section: str = "", context: str = "") -> dict:
        """Flag a visual cue as needing manual screen recording."""
        # Extract key instructions from the description
        instructions = self._parse_recording_instructions(description, context)

        self.logger.info(f"Flagged for recording: {description[:60]}...")

        return {
            "success": True,
            "needs_recording": True,
            "description": description,
            "section": section,
            "recording_instructions": instructions,
            "placeholder_text": f"[SCREEN CAPTURE NEEDED]\n\n{description}",
            "suggested_duration": self._estimate_duration(description)
        }

    def _parse_recording_instructions(self, description: str, context: str) -> dict:
        """Parse recording instructions from visual cue description."""
        instructions = {
            "what_to_show": description,
            "steps": [],
            "key_elements": [],
            "notes": []
        }

        # Extract any command-line instructions
        command_pattern = re.compile(r'(?:type|run|enter|command):\s*([^\n]+)', re.IGNORECASE)
        commands = command_pattern.findall(context)
        if commands:
            instructions["steps"] = [f"Type/run: {cmd}" for cmd in commands]

        # Extract specific UI elements to show
        if "terminal" in description.lower():
            instructions["key_elements"].append("Terminal window with command")
            instructions["notes"].append("Ensure terminal font is readable at 1080p")

        if "browser" in description.lower():
            instructions["key_elements"].append("Browser window")
            instructions["notes"].append("Hide bookmarks bar, use clean browser profile")

        if "login" in description.lower() or "authentication" in description.lower():
            instructions["key_elements"].append("Login/authentication flow")
            instructions["notes"].append("Use test credentials, blur any sensitive data")

        return instructions

    def _estimate_duration(self, description: str) -> str:
        """Estimate recording duration based on description."""
        # Simple heuristic based on keywords
        if any(word in description.lower() for word in ["quick", "simple", "brief"]):
            return "3-5 seconds"
        elif any(word in description.lower() for word in ["walkthrough", "demo", "tutorial"]):
            return "15-30 seconds"
        elif any(word in description.lower() for word in ["installation", "setup", "process"]):
            return "30-60 seconds"
        return "5-10 seconds"

    def generate_placeholder(self, description: str, output_path: Path) -> dict:
        """Generate a placeholder image for screen captures."""
        # Create a simple placeholder with instructions
        placeholder_data = {
            "type": "placeholder",
            "description": description,
            "message": "Screen capture required - see recording_instructions.md",
            "background_color": BRAND_SECONDARY,
            "text_color": BRAND_PRIMARY,
            "dimensions": {"width": 1920, "height": 1080}
        }

        return {
            "success": True,
            "placeholder": True,
            "data": placeholder_data,
            "output_path": str(output_path)
        }


# ============================================================================
# Asset Manifest
# ============================================================================

class AssetManifest:
    """Manages the asset manifest for a script."""

    def __init__(self, script_id: str, output_dir: Path):
        self.script_id = script_id
        self.output_dir = output_dir
        self.manifest_path = output_dir / "manifest.json"
        self.data = self._load_or_create()

    def _load_or_create(self) -> dict:
        """Load existing manifest or create new one."""
        if self.manifest_path.exists():
            with open(self.manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)

        return {
            "script_id": self.script_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": None,
            "total_assets": 0,
            "assets": [],
            "recording_required": [],
            "statistics": {
                "completed": 0,
                "pending": 0,
                "failed": 0,
                "needs_recording": 0
            }
        }

    def add_asset(self, asset_info: dict) -> None:
        """Add an asset to the manifest."""
        self.data["assets"].append(asset_info)
        self.data["total_assets"] = len(self.data["assets"])
        self._update_statistics()
        self.save()

    def add_recording_requirement(self, recording_info: dict) -> None:
        """Add a recording requirement."""
        self.data["recording_required"].append(recording_info)
        self._update_statistics()
        self.save()

    def _update_statistics(self) -> None:
        """Update manifest statistics."""
        stats = {"completed": 0, "pending": 0, "failed": 0, "needs_recording": 0}

        for asset in self.data["assets"]:
            status = asset.get("status", "pending")
            if status == "completed":
                stats["completed"] += 1
            elif status == "failed":
                stats["failed"] += 1
            elif status == "needs_recording":
                stats["needs_recording"] += 1
            else:
                stats["pending"] += 1

        stats["needs_recording"] += len(self.data["recording_required"])
        self.data["statistics"] = stats

    def save(self) -> None:
        """Save manifest to file."""
        self.data["updated_at"] = datetime.now().isoformat()
        self.output_dir.mkdir(parents=True, exist_ok=True)

        with open(self.manifest_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def get_summary(self) -> dict:
        """Get a summary of the manifest."""
        return {
            "script_id": self.script_id,
            "total_assets": self.data["total_assets"],
            "statistics": self.data["statistics"],
            "recording_count": len(self.data["recording_required"])
        }


# ============================================================================
# Recording Instructions Generator
# ============================================================================

class RecordingInstructionsGenerator:
    """Generate recording instructions markdown file."""

    def __init__(self, script_id: str, output_dir: Path):
        self.script_id = script_id
        self.output_dir = output_dir
        self.instructions_path = output_dir / "recording_instructions.md"
        self.recordings = []

    def add_recording(self, index: int, description: str, instructions: dict, section: str = "") -> None:
        """Add a recording requirement."""
        self.recordings.append({
            "index": index,
            "description": description,
            "instructions": instructions,
            "section": section
        })

    def generate(self) -> str:
        """Generate the recording instructions markdown."""
        if not self.recordings:
            return ""

        lines = [
            f"# Recording Instructions: {self.script_id}",
            "",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "This document contains instructions for screen recordings that need to be captured manually.",
            "",
            "## General Guidelines",
            "",
            "- **Resolution:** 1920x1080 (1080p)",
            "- **Frame Rate:** 30 fps minimum",
            "- **Audio:** None (narration added separately)",
            "- **Browser:** Use a clean profile without extensions visible",
            "- **Terminal:** Use a dark theme with readable font (14px+)",
            "- **Cursor:** Keep cursor movements smooth and deliberate",
            "",
            "---",
            "",
            "## Required Recordings",
            ""
        ]

        for rec in sorted(self.recordings, key=lambda x: x["index"]):
            lines.extend([
                f"### Recording {rec['index']:03d}",
                ""
            ])

            if rec["section"]:
                lines.append(f"**Section:** {rec['section']}")
                lines.append("")

            lines.extend([
                f"**Description:** {rec['description']}",
                ""
            ])

            if rec["instructions"].get("steps"):
                lines.append("**Steps:**")
                for step in rec["instructions"]["steps"]:
                    lines.append(f"1. {step}")
                lines.append("")

            if rec["instructions"].get("key_elements"):
                lines.append("**Key Elements to Capture:**")
                for elem in rec["instructions"]["key_elements"]:
                    lines.append(f"- {elem}")
                lines.append("")

            if rec["instructions"].get("notes"):
                lines.append("**Notes:**")
                for note in rec["instructions"]["notes"]:
                    lines.append(f"- {note}")
                lines.append("")

            duration = rec["instructions"].get("suggested_duration", "5-10 seconds")
            lines.extend([
                f"**Suggested Duration:** {duration}",
                "",
                "---",
                ""
            ])

        content = "\n".join(lines)

        # Write to file
        self.output_dir.mkdir(parents=True, exist_ok=True)
        with open(self.instructions_path, "w", encoding="utf-8") as f:
            f.write(content)

        return content


# ============================================================================
# Video Asset Generator (Main Orchestrator)
# ============================================================================

class VideoAssetGenerator:
    """Main orchestrator for generating video assets."""

    def __init__(self, verbose: bool = False, dry_run: bool = False):
        self.logger = setup_logging(verbose)
        self.dry_run = dry_run

        # Initialize generators
        self.parser = ScriptParser(self.logger)
        self.canva = CanvaGenerator(self.logger, dry_run)
        self.gemini = GeminiImageGenerator(self.logger, dry_run)
        self.screen_handler = ScreenCaptureHandler(self.logger)

        # Ensure output directories exist
        OUTPUT_BASE.mkdir(parents=True, exist_ok=True)
        PARSED_SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    def parse_script(self, script_path: Path) -> ParsedScript:
        """Parse a markdown script into structured JSON."""
        self.logger.info(f"Parsing script: {script_path.name}")
        parsed = self.parser.parse_markdown(script_path)

        # Save parsed script
        output_path = PARSED_SCRIPTS_DIR / f"{parsed.script_id}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(parsed.to_dict(), f, indent=2)

        self.logger.info(f"Saved parsed script to: {output_path}")
        return parsed

    def load_parsed_script(self, json_path: Path) -> dict:
        """Load a pre-parsed script JSON."""
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def generate_assets_for_script(self, script_data: dict, asset_types: list = None) -> dict:
        """Generate all assets for a parsed script."""
        script_id = script_data["script_id"]
        output_dir = OUTPUT_BASE / script_id
        output_dir.mkdir(parents=True, exist_ok=True)

        self.logger.info(f"Generating assets for: {script_id}")
        self.logger.info(f"Output directory: {output_dir}")

        # Initialize manifest and recording instructions
        manifest = AssetManifest(script_id, output_dir)
        recording_gen = RecordingInstructionsGenerator(script_id, output_dir)

        # Process each visual cue - support both formats
        # Format 1: visual_cues list (from internal parsing)
        # Format 2: segments list (from video-script-parser.py)
        visual_cues = script_data.get("visual_cues", [])
        if not visual_cues and script_data.get("segments"):
            # Map parser visual_type to asset generator AssetType
            type_mapping = {
                "animated_title": "title_card",
                "text_overlay": "content_slide",
                "comparison_table": "comparison_table",
                "flowchart": "flowchart",
                "screen_capture": "screen_capture",
                "illustration": "illustration",
                "calculator": "ui_mockup",
                "split_view": "comparison_table",
            }
            # Convert segments format to visual_cues format
            visual_cues = []
            for seg in script_data["segments"]:
                if seg.get("visual_cue"):
                    parser_type = seg.get("visual_type", "illustration")
                    asset_type = type_mapping.get(parser_type, "illustration")
                    visual_cues.append({
                        "index": seg.get("segment_id", len(visual_cues) + 1),
                        "description": seg["visual_cue"],
                        "asset_type": asset_type,
                        "filename": f"segment_{seg.get('segment_id', len(visual_cues)+1):03d}_{asset_type}.png",
                        "section": "",
                        "start_time": seg.get("start_time", 0),
                        "end_time": seg.get("end_time", 0)
                    })

        results = {"generated": [], "failed": [], "needs_recording": []}
        total_cues = len(visual_cues)

        for idx, cue in enumerate(visual_cues, 1):
            asset_type = AssetType(cue.get("asset_type", "unknown"))

            # Filter by asset type if specified
            if asset_types and asset_type.value not in asset_types:
                self.logger.debug(f"Skipping {cue['filename']} (type filter)")
                continue

            self.logger.info(f"[{idx}/{total_cues}] Processing: {cue['description'][:60]}...")

            output_path = output_dir / cue["filename"]

            try:
                result = self._generate_asset(cue, asset_type, output_path)

                if result.get("needs_recording"):
                    results["needs_recording"].append(cue["filename"])
                    recording_gen.add_recording(
                        cue["index"],
                        cue["description"],
                        result.get("recording_instructions", {}),
                        cue.get("section", "")
                    )
                    manifest.add_recording_requirement({
                        "index": cue["index"],
                        "filename": cue["filename"],
                        "description": cue["description"],
                        "section": cue.get("section", "")
                    })
                else:
                    results["generated"].append(cue["filename"])
                    manifest.add_asset({
                        "index": cue["index"],
                        "filename": cue["filename"],
                        "asset_type": asset_type.value,
                        "description": cue["description"],
                        "status": "completed" if not self.dry_run else "pending",
                        "output_path": str(output_path),
                        "generation_result": result
                    })

            except Exception as e:
                self.logger.error(f"Failed to generate {cue['filename']}: {e}")
                results["failed"].append({
                    "filename": cue["filename"],
                    "error": str(e)
                })
                manifest.add_asset({
                    "index": cue["index"],
                    "filename": cue["filename"],
                    "asset_type": asset_type.value,
                    "status": "failed",
                    "error": str(e)
                })

        # Generate recording instructions markdown
        if results["needs_recording"]:
            recording_gen.generate()
            self.logger.info(f"Generated recording instructions: {recording_gen.instructions_path}")

        # Save final manifest
        manifest.save()

        # Log summary
        self.logger.info("\n" + "="*50)
        self.logger.info("ASSET GENERATION SUMMARY")
        self.logger.info("="*50)
        self.logger.info(f"Script: {script_id}")
        self.logger.info(f"Total visual cues: {total_cues}")
        self.logger.info(f"Generated: {len(results['generated'])}")
        self.logger.info(f"Needs recording: {len(results['needs_recording'])}")
        self.logger.info(f"Failed: {len(results['failed'])}")
        self.logger.info(f"Output: {output_dir}")
        self.logger.info("="*50 + "\n")

        return {
            "script_id": script_id,
            "output_dir": str(output_dir),
            "manifest_path": str(manifest.manifest_path),
            "results": results,
            "summary": manifest.get_summary()
        }

    def _generate_asset(self, cue: dict, asset_type: AssetType, output_path: Path) -> dict:
        """Generate a single asset based on its type."""
        description = cue.get("description", "")

        # Route to appropriate generator
        if asset_type == AssetType.SCREEN_CAPTURE:
            return self.screen_handler.flag_for_recording(
                description,
                cue.get("section", ""),
                cue.get("context", "")
            )

        elif asset_type == AssetType.TITLE_CARD:
            # Parse title and subtitle from description
            title = description
            subtitle = ""
            if " with " in description.lower():
                parts = description.split(" with ", 1)
                title = parts[0]
                subtitle = parts[1] if len(parts) > 1 else ""
            return self.canva.create_title_card(title, subtitle, output_path)

        elif asset_type == AssetType.END_CARD:
            # Extract next lesson from description
            next_match = re.search(r'next:?\s*(.+)', description, re.IGNORECASE)
            next_lesson = next_match.group(1) if next_match else description
            return self.canva.create_end_card(next_lesson, output_path=output_path)

        elif asset_type in [AssetType.BULLET_POINTS, AssetType.CONTENT_SLIDE]:
            # Extract header and potential bullet points
            header = description
            bullets = []
            if "appearing" in description.lower():
                header = description.split("appearing")[0].strip()
            return self.canva.create_content_slide(header, bullets, output_path)

        elif asset_type == AssetType.COMPARISON_TABLE:
            return self.canva.create_comparison_table(description, [], output_path)

        elif asset_type == AssetType.FLOWCHART:
            return self.gemini.generate_flowchart(description, output_path=output_path)

        elif asset_type == AssetType.ILLUSTRATION:
            return self.gemini.generate_illustration(description, output_path=output_path)

        elif asset_type == AssetType.UI_MOCKUP:
            return self.gemini.generate_ui_mockup(description, output_path=output_path)

        elif asset_type == AssetType.ICON_SET:
            return self.gemini.generate_icon_set(description, output_path=output_path)

        elif asset_type == AssetType.QUOTE_CALLOUT:
            return self.canva.create_content_slide(description, [], output_path)

        elif asset_type == AssetType.LOGO_ANIMATION:
            # Logo animations need special handling - flag for manual
            return self.screen_handler.flag_for_recording(
                "Logo animation - create in After Effects or use existing asset",
                cue.get("section", ""),
                ""
            )

        else:
            # Default to content slide for unknown types
            return self.canva.create_content_slide(description, [], output_path)

    def process_all_scripts(self, scripts_dir: Path = None, asset_types: list = None) -> list:
        """Process all parsed script JSON files."""
        if scripts_dir is None:
            scripts_dir = PARSED_SCRIPTS_DIR

        results = []
        json_files = list(scripts_dir.glob("*.json"))

        if not json_files:
            self.logger.warning(f"No parsed scripts found in {scripts_dir}")
            self.logger.info("Run with --parse-only first to parse markdown scripts")
            return results

        for json_file in sorted(json_files):
            self.logger.info(f"\nProcessing: {json_file.name}")
            script_data = self.load_parsed_script(json_file)
            result = self.generate_assets_for_script(script_data, asset_types)
            results.append(result)

        return results

    def parse_all_raw_scripts(self, scripts_dir: Path = None) -> list:
        """Parse all raw markdown scripts."""
        if scripts_dir is None:
            scripts_dir = RAW_SCRIPTS_DIR

        results = []
        md_files = list(scripts_dir.glob("*.md"))

        self.logger.info(f"Found {len(md_files)} markdown scripts in {scripts_dir}")

        for md_file in sorted(md_files):
            try:
                parsed = self.parse_script(md_file)
                results.append({
                    "script_id": parsed.script_id,
                    "title": parsed.title,
                    "visual_cues": len(parsed.visual_cues)
                })
            except Exception as e:
                self.logger.error(f"Failed to parse {md_file.name}: {e}")
                results.append({
                    "script_id": md_file.stem,
                    "error": str(e)
                })

        return results


# ============================================================================
# CLI Interface
# ============================================================================

def create_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Video Asset Generator - Generate visual assets from parsed video scripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --parse-only                         Parse all markdown scripts to JSON
  %(prog)s --parse-only script-0.1-welcome.md   Parse a specific script
  %(prog)s --script script-0.1.json             Generate assets for one script
  %(prog)s --all                                Generate assets for all parsed scripts
  %(prog)s --type title_cards                   Generate only title cards
  %(prog)s --type screen_capture --dry-run      Preview screen capture requirements

Asset Types:
  title_card, content_slide, comparison_table, bullet_points, end_card,
  illustration, flowchart, icon_set, ui_mockup, screen_capture, logo_animation
        """
    )

    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--script",
        type=str,
        help="Path to parsed script JSON file"
    )
    input_group.add_argument(
        "--all",
        action="store_true",
        help="Process all parsed scripts"
    )
    input_group.add_argument(
        "--parse-only",
        type=str,
        nargs="?",
        const="all",
        metavar="SCRIPT.md",
        help="Parse markdown script(s) to JSON without generating assets"
    )

    # Filtering options
    parser.add_argument(
        "--type",
        type=str,
        action="append",
        dest="types",
        help="Filter by asset type (can be specified multiple times)"
    )

    # Output options
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Custom output directory"
    )

    # Behavior options
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without making API calls"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    return parser


def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Initialize generator
    generator = VideoAssetGenerator(
        verbose=args.verbose,
        dry_run=args.dry_run
    )

    try:
        # Handle parse-only mode
        if args.parse_only:
            if args.parse_only == "all":
                results = generator.parse_all_raw_scripts()
                print(f"\nParsed {len(results)} scripts")
                for r in results:
                    if "error" in r:
                        print(f"  [FAIL] {r['script_id']}: {r['error']}")
                    else:
                        print(f"  [OK] {r['script_id']}: {r['visual_cues']} visual cues")
            else:
                # Parse single script
                script_path = Path(args.parse_only)
                if not script_path.is_absolute():
                    script_path = RAW_SCRIPTS_DIR / script_path

                if not script_path.exists():
                    print(f"Script not found: {script_path}")
                    return 1

                parsed = generator.parse_script(script_path)
                print(f"\nParsed: {parsed.title}")
                print(f"Visual cues: {len(parsed.visual_cues)}")
                print(f"Output: {PARSED_SCRIPTS_DIR / f'{parsed.script_id}.json'}")

            return 0

        # Handle asset generation
        if args.script:
            script_path = Path(args.script)
            if not script_path.is_absolute():
                script_path = PARSED_SCRIPTS_DIR / script_path

            if not script_path.exists():
                print(f"Script not found: {script_path}")
                return 1

            script_data = generator.load_parsed_script(script_path)
            result = generator.generate_assets_for_script(script_data, args.types)

            print(f"\nGeneration complete!")
            print(f"Output: {result['output_dir']}")
            print(f"Manifest: {result['manifest_path']}")

        elif args.all:
            results = generator.process_all_scripts(asset_types=args.types)

            print(f"\nProcessed {len(results)} scripts")
            for r in results:
                summary = r["summary"]
                print(f"\n  {r['script_id']}:")
                print(f"    Total: {summary['total_assets']}")
                print(f"    Completed: {summary['statistics']['completed']}")
                print(f"    Needs recording: {summary['statistics']['needs_recording']}")

        else:
            parser.print_help()
            return 0

        return 0

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return 130
    except Exception as e:
        generator.logger.exception("Unexpected error")
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
