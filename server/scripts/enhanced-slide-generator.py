#!/usr/bin/env python3
"""
Enhanced Slide Generator
========================
Professional full-screen presentation generator (1920x1080) with multiple layouts,
visual elements, and typography features using PIL/Pillow.

Layouts:
- Title slides (large centered text with subtitle)
- Content slides (title + bullet points)
- Image slides (full-bleed image with text overlay)
- Architecture/flowchart slides (boxes connected with arrows)
- Split slides (image on left/right, text on opposite side)
- Checklist slides (items with checkboxes)
- Quote/highlight slides (emphasized text)

Features:
- Background images (stretched/centered)
- Icon placeholders (colored shapes)
- Progress bars / step indicators
- Gradient backgrounds
- Text shadows for readability
- Auto-wrap text
"""

import json
import os
import sys
from pathlib import Path
from typing import Optional, List, Dict, Tuple, Union
from dataclasses import dataclass
from enum import Enum

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
except ImportError:
    print("Installing Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance


# =============================================================================
# CONSTANTS & CONFIGURATION
# =============================================================================

# Dimensions - Full HD
WIDTH = 1920
HEIGHT = 1080

# Color Palette
class Colors:
    DARK_PURPLE = (30, 27, 75)       # #1E1B4B - Primary background
    MEDIUM_PURPLE = (45, 40, 100)    # Slightly lighter purple
    ACCENT_PURPLE = (139, 92, 246)   # #8B5CF6 - Accent color
    LIGHT_PURPLE = (167, 139, 250)   # Lighter accent
    WHITE = (255, 255, 255)
    OFF_WHITE = (245, 245, 250)
    LIGHT_GRAY = (200, 200, 200)
    MEDIUM_GRAY = (128, 128, 128)
    DARK_GRAY = (60, 60, 60)
    BLACK = (0, 0, 0)
    SUCCESS_GREEN = (34, 197, 94)
    WARNING_YELLOW = (250, 204, 21)
    ERROR_RED = (239, 68, 68)
    INFO_BLUE = (59, 130, 246)

# Typography sizes
class FontSizes:
    TITLE = 72
    SUBTITLE = 48
    HEADING = 56
    SUBHEADING = 42
    BODY = 36
    BODY_SMALL = 28
    CAPTION = 24
    SMALL = 20

# Layout types
class LayoutType(Enum):
    TITLE = "title"
    CONTENT = "content"
    IMAGE = "image"
    ARCHITECTURE = "architecture"
    SPLIT_LEFT = "split_left"      # Image left, text right
    SPLIT_RIGHT = "split_right"    # Text left, image right
    CHECKLIST = "checklist"
    QUOTE = "quote"
    HIGHLIGHT = "highlight"
    COMPARISON = "comparison"
    STEPS = "steps"
    STATS = "stats"


# =============================================================================
# FONT MANAGEMENT
# =============================================================================

class FontManager:
    """Manages font loading with fallbacks."""

    _font_cache: Dict[Tuple[int, bool], ImageFont.FreeTypeFont] = {}

    FONT_PATHS = [
        # Windows fonts
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/segoeuil.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        # Linux fonts
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
        # macOS fonts
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]

    @classmethod
    def get_font(cls, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
        """Get a font with caching."""
        cache_key = (size, bold)
        if cache_key in cls._font_cache:
            return cls._font_cache[cache_key]

        # Prefer bold fonts when requested
        paths = cls.FONT_PATHS.copy()
        if bold:
            # Prioritize bold font paths
            bold_paths = [p for p in paths if 'bold' in p.lower() or p.endswith('b.ttf')]
            paths = bold_paths + paths

        for path in paths:
            if os.path.exists(path):
                try:
                    font = ImageFont.truetype(path, size)
                    cls._font_cache[cache_key] = font
                    return font
                except Exception:
                    continue

        # Ultimate fallback
        return ImageFont.load_default()


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.Draw) -> List[str]:
    """Wrap text to fit within max_width, returning list of lines."""
    if not text:
        return []

    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def draw_text_with_shadow(
    draw: ImageDraw.Draw,
    position: Tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: Tuple[int, int, int],
    shadow_color: Tuple[int, int, int, int] = (0, 0, 0, 180),
    shadow_offset: Tuple[int, int] = (3, 3)
) -> None:
    """Draw text with a shadow for better readability."""
    x, y = position
    sx, sy = shadow_offset

    # Draw shadow
    shadow_rgb = shadow_color[:3] if len(shadow_color) > 3 else shadow_color
    draw.text((x + sx, y + sy), text, fill=shadow_rgb, font=font)

    # Draw main text
    draw.text((x, y), text, fill=fill, font=font)


def get_text_size(draw: ImageDraw.Draw, text: str, font: ImageFont.FreeTypeFont) -> Tuple[int, int]:
    """Get width and height of text."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def center_text_x(draw: ImageDraw.Draw, text: str, font: ImageFont.FreeTypeFont, canvas_width: int) -> int:
    """Calculate x position to center text horizontally."""
    text_width, _ = get_text_size(draw, text, font)
    return (canvas_width - text_width) // 2


# =============================================================================
# BACKGROUND GENERATORS
# =============================================================================

def create_gradient_background(
    width: int = WIDTH,
    height: int = HEIGHT,
    start_color: Tuple[int, int, int] = Colors.DARK_PURPLE,
    end_color: Tuple[int, int, int] = None,
    direction: str = "vertical"  # vertical, horizontal, diagonal
) -> Image.Image:
    """Create a gradient background."""
    img = Image.new('RGB', (width, height), start_color)
    draw = ImageDraw.Draw(img)

    if end_color is None:
        # Default: slightly lighter version of start color
        end_color = tuple(min(255, c + 30) for c in start_color)

    if direction == "vertical":
        for y in range(height):
            factor = y / height
            r = int(start_color[0] + factor * (end_color[0] - start_color[0]))
            g = int(start_color[1] + factor * (end_color[1] - start_color[1]))
            b = int(start_color[2] + factor * (end_color[2] - start_color[2]))
            draw.line([(0, y), (width, y)], fill=(r, g, b))
    elif direction == "horizontal":
        for x in range(width):
            factor = x / width
            r = int(start_color[0] + factor * (end_color[0] - start_color[0]))
            g = int(start_color[1] + factor * (end_color[1] - start_color[1]))
            b = int(start_color[2] + factor * (end_color[2] - start_color[2]))
            draw.line([(x, 0), (x, height)], fill=(r, g, b))
    else:  # diagonal
        for y in range(height):
            for x in range(width):
                factor = (x + y) / (width + height)
                r = int(start_color[0] + factor * (end_color[0] - start_color[0]))
                g = int(start_color[1] + factor * (end_color[1] - start_color[1]))
                b = int(start_color[2] + factor * (end_color[2] - start_color[2]))
                draw.point((x, y), fill=(r, g, b))

    return img


def create_background_with_image(
    image_path: str,
    width: int = WIDTH,
    height: int = HEIGHT,
    mode: str = "cover",  # cover, contain, stretch, center
    overlay_opacity: float = 0.6,
    overlay_color: Tuple[int, int, int] = Colors.DARK_PURPLE
) -> Image.Image:
    """Create background with an image and optional overlay."""
    try:
        bg_img = Image.open(image_path).convert('RGB')
    except Exception as e:
        print(f"Warning: Could not load background image: {e}")
        return create_gradient_background(width, height)

    # Create base canvas
    canvas = Image.new('RGB', (width, height), Colors.DARK_PURPLE)

    if mode == "cover":
        # Scale to cover entire canvas, cropping as needed
        img_ratio = bg_img.width / bg_img.height
        canvas_ratio = width / height

        if img_ratio > canvas_ratio:
            # Image is wider, fit by height
            new_height = height
            new_width = int(height * img_ratio)
        else:
            # Image is taller, fit by width
            new_width = width
            new_height = int(width / img_ratio)

        bg_img = bg_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Center crop
        x = (new_width - width) // 2
        y = (new_height - height) // 2
        bg_img = bg_img.crop((x, y, x + width, y + height))
        canvas.paste(bg_img, (0, 0))

    elif mode == "contain":
        # Scale to fit within canvas, preserving aspect ratio
        bg_img.thumbnail((width, height), Image.Resampling.LANCZOS)
        x = (width - bg_img.width) // 2
        y = (height - bg_img.height) // 2
        canvas.paste(bg_img, (x, y))

    elif mode == "stretch":
        # Stretch to fill entire canvas
        bg_img = bg_img.resize((width, height), Image.Resampling.LANCZOS)
        canvas.paste(bg_img, (0, 0))

    else:  # center
        # Center without scaling
        x = (width - bg_img.width) // 2
        y = (height - bg_img.height) // 2
        canvas.paste(bg_img, (x, y))

    # Apply dark overlay for text readability
    if overlay_opacity > 0:
        overlay = Image.new('RGB', (width, height), overlay_color)
        canvas = Image.blend(canvas, overlay, overlay_opacity)

    return canvas


# =============================================================================
# DECORATIVE ELEMENTS
# =============================================================================

def draw_accent_lines(draw: ImageDraw.Draw, width: int = WIDTH, height: int = HEIGHT) -> None:
    """Draw decorative accent lines."""
    # Top accent bar
    draw.rectangle([(0, 0), (width, 6)], fill=Colors.ACCENT_PURPLE)

    # Corner accents
    corner_size = 60
    line_width = 3
    margin = 40

    # Top-left
    draw.line([(margin, margin), (margin, margin + corner_size)], fill=Colors.ACCENT_PURPLE, width=line_width)
    draw.line([(margin, margin), (margin + corner_size, margin)], fill=Colors.ACCENT_PURPLE, width=line_width)

    # Top-right
    draw.line([(width - margin, margin), (width - margin, margin + corner_size)], fill=Colors.ACCENT_PURPLE, width=line_width)
    draw.line([(width - margin, margin), (width - margin - corner_size, margin)], fill=Colors.ACCENT_PURPLE, width=line_width)

    # Bottom-left
    draw.line([(margin, height - margin), (margin, height - margin - corner_size)], fill=Colors.ACCENT_PURPLE, width=line_width)
    draw.line([(margin, height - margin), (margin + corner_size, height - margin)], fill=Colors.ACCENT_PURPLE, width=line_width)

    # Bottom-right
    draw.line([(width - margin, height - margin), (width - margin, height - margin - corner_size)], fill=Colors.ACCENT_PURPLE, width=line_width)
    draw.line([(width - margin, height - margin), (width - margin - corner_size, height - margin)], fill=Colors.ACCENT_PURPLE, width=line_width)


def draw_progress_bar(
    draw: ImageDraw.Draw,
    current: int,
    total: int,
    y: int = None,
    width: int = WIDTH,
    height: int = HEIGHT
) -> None:
    """Draw a progress bar at the bottom of the slide."""
    if y is None:
        y = height - 20

    bar_height = 8
    margin = 100
    bar_width = width - 2 * margin

    # Background bar
    draw.rectangle(
        [(margin, y), (margin + bar_width, y + bar_height)],
        fill=Colors.DARK_GRAY
    )

    # Progress fill
    progress_width = int(bar_width * (current / total))
    if progress_width > 0:
        draw.rectangle(
            [(margin, y), (margin + progress_width, y + bar_height)],
            fill=Colors.ACCENT_PURPLE
        )


def draw_step_indicators(
    draw: ImageDraw.Draw,
    current: int,
    total: int,
    y: int = None,
    width: int = WIDTH,
    height: int = HEIGHT
) -> None:
    """Draw step indicators (dots) at the bottom."""
    if y is None:
        y = height - 50

    dot_radius = 8
    dot_spacing = 30
    total_width = (total - 1) * dot_spacing
    start_x = (width - total_width) // 2

    for i in range(total):
        x = start_x + i * dot_spacing
        color = Colors.ACCENT_PURPLE if i < current else Colors.DARK_GRAY
        draw.ellipse([(x - dot_radius, y - dot_radius), (x + dot_radius, y + dot_radius)], fill=color)


def draw_icon_placeholder(
    draw: ImageDraw.Draw,
    x: int,
    y: int,
    size: int = 80,
    color: Tuple[int, int, int] = Colors.ACCENT_PURPLE,
    shape: str = "circle",  # circle, square, hexagon
    icon_text: str = None
) -> None:
    """Draw an icon placeholder shape."""
    half = size // 2

    if shape == "circle":
        draw.ellipse([(x - half, y - half), (x + half, y + half)], fill=color)
    elif shape == "square":
        draw.rounded_rectangle(
            [(x - half, y - half), (x + half, y + half)],
            radius=size // 8,
            fill=color
        )
    elif shape == "hexagon":
        # Simple hexagon approximation
        points = []
        for i in range(6):
            import math
            angle = math.pi / 3 * i - math.pi / 6
            px = x + int(half * math.cos(angle))
            py = y + int(half * math.sin(angle))
            points.append((px, py))
        draw.polygon(points, fill=color)

    # Draw icon text/symbol if provided
    if icon_text:
        font = FontManager.get_font(size // 2, bold=True)
        text_width, text_height = get_text_size(draw, icon_text, font)
        draw.text(
            (x - text_width // 2, y - text_height // 2),
            icon_text,
            fill=Colors.WHITE,
            font=font
        )


# =============================================================================
# SLIDE LAYOUT GENERATORS
# =============================================================================

def create_title_slide(
    title: str,
    subtitle: str = "",
    background_image: str = None,
    output_path: Path = None
) -> Image.Image:
    """Create a title slide with large centered text."""
    # Create background
    if background_image and os.path.exists(background_image):
        img = create_background_with_image(background_image, overlay_opacity=0.65)
    else:
        img = create_gradient_background()

    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    title_font = FontManager.get_font(FontSizes.TITLE, bold=True)
    subtitle_font = FontManager.get_font(FontSizes.SUBTITLE)

    # Calculate title lines
    title_lines = wrap_text(title.upper(), title_font, WIDTH - 200, draw)
    line_height = FontSizes.TITLE + 20

    # Calculate vertical positioning
    total_height = len(title_lines) * line_height
    if subtitle:
        total_height += FontSizes.SUBTITLE + 40

    start_y = (HEIGHT - total_height) // 2

    # Draw title lines
    for i, line in enumerate(title_lines):
        x = center_text_x(draw, line, title_font, WIDTH)
        y = start_y + i * line_height

        if background_image:
            draw_text_with_shadow(draw, (x, y), line, title_font, Colors.WHITE)
        else:
            draw.text((x, y), line, fill=Colors.WHITE, font=title_font)

    # Draw subtitle
    if subtitle:
        subtitle_y = start_y + len(title_lines) * line_height + 30
        x = center_text_x(draw, subtitle, subtitle_font, WIDTH)

        if background_image:
            draw_text_with_shadow(draw, (x, subtitle_y), subtitle, subtitle_font, Colors.ACCENT_PURPLE)
        else:
            draw.text((x, subtitle_y), subtitle, fill=Colors.ACCENT_PURPLE, font=subtitle_font)

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_content_slide(
    title: str,
    bullet_points: List[str] = None,
    background_image: str = None,
    show_icons: bool = False,
    output_path: Path = None
) -> Image.Image:
    """Create a content slide with title and bullet points."""
    if background_image and os.path.exists(background_image):
        img = create_background_with_image(background_image, overlay_opacity=0.7)
    else:
        img = create_gradient_background()

    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    title_font = FontManager.get_font(FontSizes.HEADING, bold=True)
    bullet_font = FontManager.get_font(FontSizes.BODY)

    # Draw title
    title_y = 100
    if background_image:
        draw_text_with_shadow(draw, (120, title_y), title, title_font, Colors.WHITE)
    else:
        draw.text((120, title_y), title, fill=Colors.WHITE, font=title_font)

    # Draw title underline
    bbox = draw.textbbox((120, title_y), title, font=title_font)
    draw.line([(120, bbox[3] + 15), (bbox[2] + 20, bbox[3] + 15)], fill=Colors.ACCENT_PURPLE, width=4)

    # Draw bullet points
    if bullet_points:
        y = 220
        bullet_spacing = 70

        for i, point in enumerate(bullet_points):
            # Bullet indicator
            bullet_x = 120
            bullet_y = y + 15

            if show_icons:
                draw_icon_placeholder(draw, bullet_x + 20, bullet_y, size=40, shape="circle")
                text_x = 180
            else:
                draw.ellipse(
                    [(bullet_x, bullet_y - 8), (bullet_x + 16, bullet_y + 8)],
                    fill=Colors.ACCENT_PURPLE
                )
                text_x = 160

            # Wrap and draw text
            lines = wrap_text(point, bullet_font, WIDTH - text_x - 120, draw)
            for line in lines:
                if background_image:
                    draw_text_with_shadow(draw, (text_x, y), line, bullet_font, Colors.OFF_WHITE)
                else:
                    draw.text((text_x, y), line, fill=Colors.LIGHT_GRAY, font=bullet_font)
                y += FontSizes.BODY + 8
            y += 25  # Extra spacing between bullets

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_image_slide(
    image_path: str,
    title: str = "",
    subtitle: str = "",
    text_position: str = "bottom",  # top, bottom, center
    output_path: Path = None
) -> Image.Image:
    """Create a full-bleed image slide with text overlay."""
    img = create_background_with_image(image_path, mode="cover", overlay_opacity=0.4)
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = FontManager.get_font(FontSizes.HEADING, bold=True)
    subtitle_font = FontManager.get_font(FontSizes.SUBHEADING)

    # Calculate text position
    if text_position == "top":
        title_y = 100
    elif text_position == "center":
        title_y = HEIGHT // 2 - 50
    else:  # bottom
        title_y = HEIGHT - 250

    # Draw semi-transparent text background
    if title or subtitle:
        padding = 40
        text_height = 0
        if title:
            text_height += FontSizes.HEADING + 20
        if subtitle:
            text_height += FontSizes.SUBHEADING + 20

        # Create gradient overlay for text area
        overlay_y = title_y - padding
        overlay_height = text_height + 2 * padding

        for y in range(int(overlay_y), int(overlay_y + overlay_height)):
            alpha = int(160 * (1 - abs(y - (overlay_y + overlay_height/2)) / (overlay_height/2)))
            draw.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, alpha)[:3])

    # Draw title
    if title:
        x = center_text_x(draw, title, title_font, WIDTH)
        draw_text_with_shadow(draw, (x, title_y), title, title_font, Colors.WHITE, shadow_offset=(4, 4))

    # Draw subtitle
    if subtitle:
        subtitle_y = title_y + FontSizes.HEADING + 20
        x = center_text_x(draw, subtitle, subtitle_font, WIDTH)
        draw_text_with_shadow(draw, (x, subtitle_y), subtitle, subtitle_font, Colors.LIGHT_GRAY)

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_architecture_slide(
    title: str,
    elements: List[Dict],
    connection_style: str = "arrow",  # arrow, line, dashed
    layout: str = "horizontal",  # horizontal, vertical, grid
    output_path: Path = None
) -> Image.Image:
    """Create an architecture/flowchart slide with connected boxes."""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    title_font = FontManager.get_font(FontSizes.SUBHEADING, bold=True)
    element_font = FontManager.get_font(FontSizes.BODY_SMALL)

    # Draw title
    title_x = center_text_x(draw, title, title_font, WIDTH)
    draw.text((title_x, 60), title, fill=Colors.WHITE, font=title_font)

    if not elements:
        return img

    # Box dimensions
    box_width = 220
    box_height = 100
    box_radius = 12
    spacing = 60

    num_elements = len(elements)

    if layout == "horizontal":
        total_width = num_elements * box_width + (num_elements - 1) * spacing
        start_x = (WIDTH - total_width) // 2
        center_y = HEIGHT // 2 + 30

        for i, elem in enumerate(elements):
            x = start_x + i * (box_width + spacing)
            y = center_y - box_height // 2

            # Draw box shadow
            shadow_offset = 6
            draw.rounded_rectangle(
                [(x + shadow_offset, y + shadow_offset), (x + box_width + shadow_offset, y + box_height + shadow_offset)],
                radius=box_radius,
                fill=(20, 18, 50)
            )

            # Draw box
            box_color = elem.get('color', Colors.MEDIUM_PURPLE)
            if isinstance(box_color, str):
                # Convert hex to RGB if needed
                box_color = Colors.MEDIUM_PURPLE

            draw.rounded_rectangle(
                [(x, y), (x + box_width, y + box_height)],
                radius=box_radius,
                fill=box_color,
                outline=Colors.ACCENT_PURPLE,
                width=2
            )

            # Draw icon if specified
            icon = elem.get('icon')
            if icon:
                draw_icon_placeholder(draw, x + 40, y + box_height // 2, size=50, icon_text=icon)
                text_x_offset = 70
            else:
                text_x_offset = 0

            # Draw text
            text = elem.get('text', f'Step {i+1}')
            lines = wrap_text(text, element_font, box_width - 40 - text_x_offset, draw)
            text_y = y + (box_height - len(lines) * (FontSizes.BODY_SMALL + 5)) // 2

            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=element_font)
                text_x = x + text_x_offset + (box_width - text_x_offset - (bbox[2] - bbox[0])) // 2
                draw.text((text_x, text_y), line, fill=Colors.WHITE, font=element_font)
                text_y += FontSizes.BODY_SMALL + 5

            # Draw connection to next element
            if i < num_elements - 1:
                arrow_start_x = x + box_width + 5
                arrow_end_x = x + box_width + spacing - 5
                arrow_y = center_y

                if connection_style == "dashed":
                    dash_length = 10
                    for dx in range(0, int(spacing - 10), dash_length * 2):
                        draw.line(
                            [(arrow_start_x + dx, arrow_y), (arrow_start_x + dx + dash_length, arrow_y)],
                            fill=Colors.ACCENT_PURPLE,
                            width=3
                        )
                else:
                    draw.line([(arrow_start_x, arrow_y), (arrow_end_x - 10, arrow_y)], fill=Colors.ACCENT_PURPLE, width=3)

                if connection_style == "arrow":
                    # Arrow head
                    arrow_size = 10
                    draw.polygon([
                        (arrow_end_x - arrow_size, arrow_y - arrow_size),
                        (arrow_end_x, arrow_y),
                        (arrow_end_x - arrow_size, arrow_y + arrow_size)
                    ], fill=Colors.ACCENT_PURPLE)

    elif layout == "grid":
        # Arrange in 2 rows
        cols = (num_elements + 1) // 2
        rows = 2 if num_elements > 1 else 1

        total_width = cols * box_width + (cols - 1) * spacing
        start_x = (WIDTH - total_width) // 2
        start_y = 180
        row_spacing = 150

        for i, elem in enumerate(elements):
            row = i // cols
            col = i % cols
            x = start_x + col * (box_width + spacing)
            y = start_y + row * (box_height + row_spacing)

            # Draw box
            draw.rounded_rectangle(
                [(x, y), (x + box_width, y + box_height)],
                radius=box_radius,
                fill=Colors.MEDIUM_PURPLE,
                outline=Colors.ACCENT_PURPLE,
                width=2
            )

            text = elem.get('text', f'Step {i+1}')
            lines = wrap_text(text, element_font, box_width - 30, draw)
            text_y = y + (box_height - len(lines) * (FontSizes.BODY_SMALL + 5)) // 2

            for line in lines:
                text_x = x + (box_width - get_text_size(draw, line, element_font)[0]) // 2
                draw.text((text_x, text_y), line, fill=Colors.WHITE, font=element_font)
                text_y += FontSizes.BODY_SMALL + 5

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_split_slide(
    title: str,
    content: List[str],
    image_path: str = None,
    image_side: str = "left",  # left or right
    output_path: Path = None
) -> Image.Image:
    """Create a split slide with image on one side and text on the other."""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)

    split_point = WIDTH // 2

    # Determine image and text sides
    if image_side == "left":
        img_area = (0, 0, split_point, HEIGHT)
        text_x_start = split_point + 60
        text_width = WIDTH - split_point - 120
    else:
        img_area = (split_point, 0, WIDTH, HEIGHT)
        text_x_start = 80
        text_width = split_point - 140

    # Load and paste image
    if image_path and os.path.exists(image_path):
        try:
            side_img = Image.open(image_path).convert('RGB')
            area_width = img_area[2] - img_area[0]
            area_height = img_area[3] - img_area[1]

            # Scale to fill
            img_ratio = side_img.width / side_img.height
            area_ratio = area_width / area_height

            if img_ratio > area_ratio:
                new_height = area_height
                new_width = int(area_height * img_ratio)
            else:
                new_width = area_width
                new_height = int(area_width / img_ratio)

            side_img = side_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Center crop
            crop_x = (new_width - area_width) // 2
            crop_y = (new_height - area_height) // 2
            side_img = side_img.crop((crop_x, crop_y, crop_x + area_width, crop_y + area_height))

            img.paste(side_img, (img_area[0], img_area[1]))
        except Exception as e:
            print(f"Warning: Could not load split image: {e}")
    else:
        # Draw placeholder
        placeholder_color = Colors.MEDIUM_PURPLE
        draw.rectangle(img_area, fill=placeholder_color)
        draw_icon_placeholder(
            draw,
            (img_area[0] + img_area[2]) // 2,
            HEIGHT // 2,
            size=120,
            color=Colors.ACCENT_PURPLE,
            icon_text="IMG"
        )

    # Draw divider line
    if image_side == "left":
        draw.line([(split_point, 80), (split_point, HEIGHT - 80)], fill=Colors.ACCENT_PURPLE, width=3)
    else:
        draw.line([(split_point, 80), (split_point, HEIGHT - 80)], fill=Colors.ACCENT_PURPLE, width=3)

    # Fonts
    title_font = FontManager.get_font(FontSizes.SUBHEADING, bold=True)
    content_font = FontManager.get_font(FontSizes.BODY)

    # Draw title
    title_y = 120
    title_lines = wrap_text(title, title_font, text_width, draw)
    for line in title_lines:
        draw.text((text_x_start, title_y), line, fill=Colors.WHITE, font=title_font)
        title_y += FontSizes.SUBHEADING + 10

    # Draw underline
    draw.line([(text_x_start, title_y + 5), (text_x_start + 150, title_y + 5)], fill=Colors.ACCENT_PURPLE, width=3)

    # Draw content
    if content:
        y = title_y + 50
        for item in content:
            # Bullet
            draw.ellipse(
                [(text_x_start, y + 10), (text_x_start + 12, y + 22)],
                fill=Colors.ACCENT_PURPLE
            )

            # Text
            lines = wrap_text(item, content_font, text_width - 40, draw)
            for line in lines:
                draw.text((text_x_start + 30, y), line, fill=Colors.LIGHT_GRAY, font=content_font)
                y += FontSizes.BODY + 5
            y += 20

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_checklist_slide(
    title: str,
    items: List[Dict],  # {'text': str, 'checked': bool}
    output_path: Path = None
) -> Image.Image:
    """Create a checklist slide with checkbox items."""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    title_font = FontManager.get_font(FontSizes.HEADING, bold=True)
    item_font = FontManager.get_font(FontSizes.BODY)

    # Draw title
    title_x = center_text_x(draw, title, title_font, WIDTH)
    draw.text((title_x, 80), title, fill=Colors.WHITE, font=title_font)

    # Draw items
    start_y = 200
    item_height = 70
    checkbox_size = 32

    for i, item in enumerate(items):
        y = start_y + i * item_height
        x = 200

        # Draw checkbox
        draw.rounded_rectangle(
            [(x, y), (x + checkbox_size, y + checkbox_size)],
            radius=6,
            outline=Colors.ACCENT_PURPLE,
            width=3
        )

        # Draw checkmark if checked
        if item.get('checked', False):
            draw.rectangle([(x + 6, y + 6), (x + checkbox_size - 6, y + checkbox_size - 6)], fill=Colors.SUCCESS_GREEN)
            # Simple checkmark
            draw.line([(x + 8, y + 16), (x + 14, y + 24)], fill=Colors.WHITE, width=3)
            draw.line([(x + 14, y + 24), (x + 26, y + 10)], fill=Colors.WHITE, width=3)

        # Draw text
        text = item.get('text', '')
        text_color = Colors.WHITE if item.get('checked', False) else Colors.LIGHT_GRAY
        lines = wrap_text(text, item_font, WIDTH - x - checkbox_size - 250, draw)
        text_y = y + (checkbox_size - len(lines) * FontSizes.BODY) // 2 - 5

        for line in lines:
            draw.text((x + checkbox_size + 20, text_y), line, fill=text_color, font=item_font)
            text_y += FontSizes.BODY + 5

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_quote_slide(
    quote: str,
    author: str = "",
    background_image: str = None,
    output_path: Path = None
) -> Image.Image:
    """Create a quote slide with emphasized text."""
    if background_image and os.path.exists(background_image):
        img = create_background_with_image(background_image, overlay_opacity=0.75)
    else:
        img = create_gradient_background()

    draw = ImageDraw.Draw(img)

    # Fonts
    quote_font = FontManager.get_font(FontSizes.SUBHEADING)
    author_font = FontManager.get_font(FontSizes.BODY)

    # Draw quotation marks
    quote_mark_font = FontManager.get_font(120, bold=True)
    draw.text((150, 200), '"', fill=Colors.ACCENT_PURPLE, font=quote_mark_font)

    # Draw quote text
    quote_lines = wrap_text(quote, quote_font, WIDTH - 400, draw)
    y = 300
    for line in quote_lines:
        x = center_text_x(draw, line, quote_font, WIDTH)
        if background_image:
            draw_text_with_shadow(draw, (x, y), line, quote_font, Colors.WHITE)
        else:
            draw.text((x, y), line, fill=Colors.WHITE, font=quote_font)
        y += FontSizes.SUBHEADING + 15

    # Draw closing quote mark
    draw.text((WIDTH - 250, y - 50), '"', fill=Colors.ACCENT_PURPLE, font=quote_mark_font)

    # Draw author
    if author:
        author_text = f"- {author}"
        author_x = center_text_x(draw, author_text, author_font, WIDTH)
        draw.text((author_x, y + 50), author_text, fill=Colors.ACCENT_PURPLE, font=author_font)

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_highlight_slide(
    main_text: str,
    highlight_text: str,
    background_image: str = None,
    output_path: Path = None
) -> Image.Image:
    """Create a slide with highlighted/emphasized text."""
    if background_image and os.path.exists(background_image):
        img = create_background_with_image(background_image, overlay_opacity=0.7)
    else:
        img = create_gradient_background()

    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    main_font = FontManager.get_font(FontSizes.SUBHEADING)
    highlight_font = FontManager.get_font(FontSizes.TITLE, bold=True)

    # Draw main text
    main_lines = wrap_text(main_text, main_font, WIDTH - 200, draw)
    y = 250
    for line in main_lines:
        x = center_text_x(draw, line, main_font, WIDTH)
        draw.text((x, y), line, fill=Colors.LIGHT_GRAY, font=main_font)
        y += FontSizes.SUBHEADING + 10

    # Draw highlight box
    highlight_lines = wrap_text(highlight_text, highlight_font, WIDTH - 200, draw)
    highlight_height = len(highlight_lines) * (FontSizes.TITLE + 15)
    highlight_y = HEIGHT // 2 + 50

    # Get max line width
    max_line_width = max(get_text_size(draw, line, highlight_font)[0] for line in highlight_lines)

    # Draw background box
    padding = 30
    box_x = (WIDTH - max_line_width) // 2 - padding
    box_y = highlight_y - padding
    box_width = max_line_width + 2 * padding
    box_height = highlight_height + 2 * padding

    draw.rounded_rectangle(
        [(box_x, box_y), (box_x + box_width, box_y + box_height)],
        radius=15,
        fill=Colors.ACCENT_PURPLE
    )

    # Draw highlight text
    for line in highlight_lines:
        x = center_text_x(draw, line, highlight_font, WIDTH)
        draw.text((x, highlight_y), line, fill=Colors.WHITE, font=highlight_font)
        highlight_y += FontSizes.TITLE + 15

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_stats_slide(
    title: str,
    stats: List[Dict],  # {'value': str, 'label': str, 'color': tuple}
    output_path: Path = None
) -> Image.Image:
    """Create a slide showcasing statistics."""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    title_font = FontManager.get_font(FontSizes.HEADING, bold=True)
    value_font = FontManager.get_font(FontSizes.TITLE, bold=True)
    label_font = FontManager.get_font(FontSizes.BODY_SMALL)

    # Draw title
    title_x = center_text_x(draw, title, title_font, WIDTH)
    draw.text((title_x, 80), title, fill=Colors.WHITE, font=title_font)

    # Draw stats
    if stats:
        num_stats = len(stats)
        stat_width = 300
        spacing = 80
        total_width = num_stats * stat_width + (num_stats - 1) * spacing
        start_x = (WIDTH - total_width) // 2
        center_y = HEIGHT // 2 + 50

        for i, stat in enumerate(stats):
            x = start_x + i * (stat_width + spacing) + stat_width // 2

            # Draw value
            value = stat.get('value', '0')
            color = stat.get('color', Colors.ACCENT_PURPLE)
            value_x = x - get_text_size(draw, value, value_font)[0] // 2
            draw.text((value_x, center_y - 80), value, fill=color, font=value_font)

            # Draw underline
            value_width = get_text_size(draw, value, value_font)[0]
            draw.line(
                [(x - value_width // 2 - 20, center_y), (x + value_width // 2 + 20, center_y)],
                fill=color,
                width=3
            )

            # Draw label
            label = stat.get('label', '')
            label_lines = wrap_text(label, label_font, stat_width, draw)
            label_y = center_y + 30
            for line in label_lines:
                label_x = x - get_text_size(draw, line, label_font)[0] // 2
                draw.text((label_x, label_y), line, fill=Colors.LIGHT_GRAY, font=label_font)
                label_y += FontSizes.BODY_SMALL + 5

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_steps_slide(
    title: str,
    steps: List[Dict],  # {'number': int, 'title': str, 'description': str}
    output_path: Path = None
) -> Image.Image:
    """Create a slide showing numbered steps."""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw)

    # Fonts
    title_font = FontManager.get_font(FontSizes.HEADING, bold=True)
    number_font = FontManager.get_font(FontSizes.SUBTITLE, bold=True)
    step_title_font = FontManager.get_font(FontSizes.BODY, bold=True)
    desc_font = FontManager.get_font(FontSizes.BODY_SMALL)

    # Draw title
    title_x = center_text_x(draw, title, title_font, WIDTH)
    draw.text((title_x, 60), title, fill=Colors.WHITE, font=title_font)

    if steps:
        num_steps = len(steps)
        start_y = 180
        step_height = (HEIGHT - start_y - 100) // min(num_steps, 4)

        for i, step in enumerate(steps[:4]):  # Max 4 steps
            y = start_y + i * step_height

            # Draw number circle
            circle_x = 180
            circle_y = y + 25
            circle_radius = 35

            draw.ellipse(
                [(circle_x - circle_radius, circle_y - circle_radius),
                 (circle_x + circle_radius, circle_y + circle_radius)],
                fill=Colors.ACCENT_PURPLE
            )

            number = str(step.get('number', i + 1))
            num_x = circle_x - get_text_size(draw, number, number_font)[0] // 2
            num_y = circle_y - get_text_size(draw, number, number_font)[1] // 2 - 5
            draw.text((num_x, num_y), number, fill=Colors.WHITE, font=number_font)

            # Draw connecting line to next step
            if i < num_steps - 1 and i < 3:
                line_y_start = circle_y + circle_radius + 10
                line_y_end = start_y + (i + 1) * step_height + 25 - circle_radius - 10
                draw.line([(circle_x, line_y_start), (circle_x, line_y_end)], fill=Colors.DARK_GRAY, width=2)

            # Draw step title
            step_title = step.get('title', '')
            draw.text((250, y), step_title, fill=Colors.WHITE, font=step_title_font)

            # Draw description
            desc = step.get('description', '')
            if desc:
                desc_lines = wrap_text(desc, desc_font, WIDTH - 350, draw)
                desc_y = y + FontSizes.BODY + 10
                for line in desc_lines:
                    draw.text((250, desc_y), line, fill=Colors.LIGHT_GRAY, font=desc_font)
                    desc_y += FontSizes.BODY_SMALL + 3

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


# =============================================================================
# MAIN GENERATION FUNCTION
# =============================================================================

def generate_slide_from_config(config: Dict, output_path: Path = None) -> Image.Image:
    """Generate a slide from a configuration dictionary."""
    layout = config.get('layout', 'title')

    # Common parameters
    title = config.get('title', '')
    subtitle = config.get('subtitle', '')
    background_image = config.get('background_image')

    if layout == 'title':
        return create_title_slide(title, subtitle, background_image, output_path)

    elif layout == 'content':
        bullets = config.get('bullets', config.get('content', []))
        show_icons = config.get('show_icons', False)
        return create_content_slide(title, bullets, background_image, show_icons, output_path)

    elif layout == 'image':
        image_path = config.get('image_path', background_image)
        text_position = config.get('text_position', 'bottom')
        return create_image_slide(image_path, title, subtitle, text_position, output_path)

    elif layout == 'architecture':
        elements = config.get('elements', [])
        connection_style = config.get('connection_style', 'arrow')
        grid_layout = config.get('grid_layout', 'horizontal')
        return create_architecture_slide(title, elements, connection_style, grid_layout, output_path)

    elif layout in ('split_left', 'split_right'):
        content = config.get('content', [])
        image_path = config.get('image_path')
        image_side = 'left' if layout == 'split_left' else 'right'
        return create_split_slide(title, content, image_path, image_side, output_path)

    elif layout == 'checklist':
        items = config.get('items', [])
        return create_checklist_slide(title, items, output_path)

    elif layout == 'quote':
        quote = config.get('quote', config.get('text', ''))
        author = config.get('author', '')
        return create_quote_slide(quote, author, background_image, output_path)

    elif layout == 'highlight':
        main_text = config.get('main_text', '')
        highlight_text = config.get('highlight_text', config.get('highlight', ''))
        return create_highlight_slide(main_text, highlight_text, background_image, output_path)

    elif layout == 'stats':
        stats = config.get('stats', [])
        return create_stats_slide(title, stats, output_path)

    elif layout == 'steps':
        steps = config.get('steps', [])
        return create_steps_slide(title, steps, output_path)

    else:
        # Default to title slide
        return create_title_slide(title, subtitle, background_image, output_path)


def generate_slides_from_script(script_data: Union[str, Path, Dict], output_dir: Path) -> List[Path]:
    """Generate all slides from a parsed script JSON."""
    # Load script data
    if isinstance(script_data, (str, Path)):
        with open(script_data, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = script_data

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    generated_files = []
    slides = data.get('slides', [])

    print(f"\nGenerating {len(slides)} slides to: {output_dir}")
    print("=" * 60)

    for i, slide_config in enumerate(slides):
        slide_num = slide_config.get('slide_number', i + 1)
        output_path = output_dir / f"slide_{slide_num:03d}.png"

        try:
            generate_slide_from_config(slide_config, output_path)
            generated_files.append(output_path)
            print(f"  Slide {slide_num}: {slide_config.get('layout', 'title')} -> {output_path.name}")
        except Exception as e:
            print(f"  ERROR on slide {slide_num}: {e}")

    print(f"\nGenerated {len(generated_files)} slides")
    return generated_files


# =============================================================================
# DEMO & CLI
# =============================================================================

def generate_demo_slides(output_dir: Path):
    """Generate demo slides to test all layouts."""
    output_dir.mkdir(parents=True, exist_ok=True)

    demo_slides = [
        {
            "slide_number": 1,
            "layout": "title",
            "title": "Enhanced Slide Generator",
            "subtitle": "Professional Presentations Made Easy"
        },
        {
            "slide_number": 2,
            "layout": "content",
            "title": "Key Features",
            "bullets": [
                "Multiple professional slide layouts",
                "Support for background images",
                "Icon placeholders and visual elements",
                "Gradient backgrounds with brand colors",
                "Auto-wrapping text with proper typography"
            ]
        },
        {
            "slide_number": 3,
            "layout": "architecture",
            "title": "System Architecture",
            "elements": [
                {"text": "Input", "icon": "1"},
                {"text": "Process", "icon": "2"},
                {"text": "AI Agent", "icon": "3"},
                {"text": "Output", "icon": "4"}
            ]
        },
        {
            "slide_number": 4,
            "layout": "checklist",
            "title": "Project Checklist",
            "items": [
                {"text": "Design system architecture", "checked": True},
                {"text": "Implement core features", "checked": True},
                {"text": "Add visual elements", "checked": True},
                {"text": "Write documentation", "checked": False},
                {"text": "Deploy to production", "checked": False}
            ]
        },
        {
            "slide_number": 5,
            "layout": "quote",
            "quote": "The best way to predict the future is to create it.",
            "author": "Peter Drucker"
        },
        {
            "slide_number": 6,
            "layout": "highlight",
            "main_text": "Transform your business with automation",
            "highlight_text": "SAVE 10-20 HOURS PER WEEK"
        },
        {
            "slide_number": 7,
            "layout": "stats",
            "title": "Impact Metrics",
            "stats": [
                {"value": "85%", "label": "Time Saved on Repetitive Tasks", "color": (34, 197, 94)},
                {"value": "3X", "label": "Faster Client Onboarding", "color": (139, 92, 246)},
                {"value": "24/7", "label": "Automated Availability", "color": (59, 130, 246)}
            ]
        },
        {
            "slide_number": 8,
            "layout": "steps",
            "title": "Getting Started",
            "steps": [
                {"number": 1, "title": "Install Dependencies", "description": "Run pip install Pillow to get started"},
                {"number": 2, "title": "Create Configuration", "description": "Define your slides in JSON format"},
                {"number": 3, "title": "Generate Slides", "description": "Run the script to create PNG files"},
                {"number": 4, "title": "Use in Presentations", "description": "Import slides into your video or slideshow"}
            ]
        },
        {
            "slide_number": 9,
            "layout": "split_left",
            "title": "Split Layout Demo",
            "content": [
                "Image on the left side",
                "Text content on the right",
                "Great for product showcases",
                "Or before/after comparisons"
            ]
        },
        {
            "slide_number": 10,
            "layout": "title",
            "title": "Thank You!",
            "subtitle": "Questions? Let's discuss."
        }
    ]

    print("\n" + "=" * 60)
    print("GENERATING DEMO SLIDES")
    print("=" * 60)

    for slide_config in demo_slides:
        slide_num = slide_config['slide_number']
        output_path = output_dir / f"demo_slide_{slide_num:02d}.png"
        generate_slide_from_config(slide_config, output_path)

    print(f"\nDemo slides saved to: {output_dir}")
    print("=" * 60)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Enhanced Slide Generator - Create professional presentations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate demo slides
  python enhanced-slide-generator.py --demo

  # Generate from JSON config
  python enhanced-slide-generator.py --script slides.json --output ./output

  # Generate single slide from command line
  python enhanced-slide-generator.py --layout title --title "My Title" --subtitle "My Subtitle"
        """
    )

    parser.add_argument("--demo", action="store_true", help="Generate demo slides")
    parser.add_argument("--script", type=Path, help="Path to slides JSON config")
    parser.add_argument("--output", type=Path, default=Path("output/slides"), help="Output directory")

    # Single slide options
    parser.add_argument("--layout", type=str, help="Slide layout type")
    parser.add_argument("--title", type=str, help="Slide title")
    parser.add_argument("--subtitle", type=str, help="Slide subtitle")
    parser.add_argument("--background", type=str, help="Background image path")

    args = parser.parse_args()

    if args.demo:
        generate_demo_slides(args.output / "demo")

    elif args.script:
        generate_slides_from_script(args.script, args.output)

    elif args.layout:
        config = {
            "layout": args.layout,
            "title": args.title or "Untitled",
            "subtitle": args.subtitle or "",
            "background_image": args.background
        }
        args.output.mkdir(parents=True, exist_ok=True)
        output_path = args.output / f"{args.layout}_slide.png"
        generate_slide_from_config(config, output_path)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
