#!/usr/bin/env python3
"""
Slide Asset Generator
=====================
Creates professional slide images for video composition using PIL/Pillow.
Generates dark-themed slides with purple accents matching Support Forge branding.
"""

import json
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont


# Branding colors
DARK_PURPLE = (30, 27, 75)      # #1E1B4B
ACCENT_PURPLE = (139, 92, 246)  # #8B5CF6
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (80, 80, 80)

# Dimensions
WIDTH = 1920
HEIGHT = 864  # Matches compositor visual area


def get_font(size: int, bold: bool = False):
    """Get a font, falling back to default if custom fonts aren't available."""
    font_paths = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else None,
    ]

    for path in font_paths:
        if path and os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue

    # Fall back to default
    return ImageFont.load_default()


def create_gradient_background(width: int, height: int) -> Image.Image:
    """Create a gradient background from dark purple."""
    img = Image.new('RGB', (width, height), DARK_PURPLE)
    draw = ImageDraw.Draw(img)

    # Add subtle gradient
    for y in range(height):
        factor = y / height * 0.3
        r = int(DARK_PURPLE[0] + factor * 20)
        g = int(DARK_PURPLE[1] + factor * 20)
        b = int(DARK_PURPLE[2] + factor * 40)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img


def draw_accent_lines(draw: ImageDraw.Draw, width: int, height: int):
    """Draw decorative accent lines."""
    # Top accent line
    draw.line([(0, 3), (width, 3)], fill=ACCENT_PURPLE, width=6)

    # Corner accents
    draw.line([(50, 50), (50, 100)], fill=ACCENT_PURPLE, width=3)
    draw.line([(50, 50), (100, 50)], fill=ACCENT_PURPLE, width=3)

    draw.line([(width - 50, 50), (width - 50, 100)], fill=ACCENT_PURPLE, width=3)
    draw.line([(width - 50, 50), (width - 100, 50)], fill=ACCENT_PURPLE, width=3)


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.Draw) -> list[str]:
    """Wrap text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def create_title_slide(title: str, subtitle: str = "", output_path: Path = None) -> Image.Image:
    """Create a title slide with large centered text."""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw, WIDTH, HEIGHT)

    # Title font
    title_font = get_font(72, bold=True)
    subtitle_font = get_font(36)

    # Draw title centered
    title_lines = wrap_text(title.upper(), title_font, WIDTH - 200, draw)
    total_height = len(title_lines) * 90
    if subtitle:
        total_height += 60

    start_y = (HEIGHT - total_height) // 2

    for i, line in enumerate(title_lines):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = start_y + i * 90
        draw.text((x, y), line, fill=WHITE, font=title_font)

    # Draw subtitle
    if subtitle:
        bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = start_y + len(title_lines) * 90 + 30
        draw.text((x, y), subtitle, fill=ACCENT_PURPLE, font=subtitle_font)

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_content_slide(title: str, bullet_points: list[str] = None, output_path: Path = None) -> Image.Image:
    """Create a content slide with title and bullet points."""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw, WIDTH, HEIGHT)

    # Fonts
    title_font = get_font(48, bold=True)
    bullet_font = get_font(32)

    # Draw title at top
    title_y = 80
    draw.text((100, title_y), title, fill=WHITE, font=title_font)

    # Draw underline
    bbox = draw.textbbox((100, title_y), title, font=title_font)
    draw.line([(100, bbox[3] + 10), (bbox[2], bbox[3] + 10)], fill=ACCENT_PURPLE, width=4)

    # Draw bullet points
    if bullet_points:
        y = 200
        for point in bullet_points:
            # Bullet
            draw.ellipse([(100, y + 12), (116, y + 28)], fill=ACCENT_PURPLE)

            # Text
            lines = wrap_text(point, bullet_font, WIDTH - 300, draw)
            for line in lines:
                draw.text((140, y), line, fill=LIGHT_GRAY, font=bullet_font)
                y += 50
            y += 20

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_diagram_slide(title: str, elements: list[dict], output_path: Path = None) -> Image.Image:
    """Create a slide with diagram elements (boxes with connections)."""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw, WIDTH, HEIGHT)

    # Fonts
    title_font = get_font(42, bold=True)
    element_font = get_font(24)

    # Draw title
    bbox = draw.textbbox((0, 0), title, font=title_font)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    draw.text((x, 50), title, fill=WHITE, font=title_font)

    # Draw elements as boxes in a flow
    if elements:
        num_elements = len(elements)
        box_width = 250
        box_height = 100
        spacing = 50
        total_width = num_elements * box_width + (num_elements - 1) * spacing
        start_x = (WIDTH - total_width) // 2
        y = (HEIGHT - box_height) // 2 + 50

        for i, elem in enumerate(elements):
            x = start_x + i * (box_width + spacing)

            # Draw box
            draw.rounded_rectangle(
                [(x, y), (x + box_width, y + box_height)],
                radius=10,
                fill=(50, 45, 95),
                outline=ACCENT_PURPLE,
                width=2
            )

            # Draw text
            text = elem.get('text', f'Step {i+1}')
            lines = wrap_text(text, element_font, box_width - 20, draw)
            text_y = y + (box_height - len(lines) * 30) // 2
            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=element_font)
                text_x = x + (box_width - (bbox[2] - bbox[0])) // 2
                draw.text((text_x, text_y), line, fill=WHITE, font=element_font)
                text_y += 30

            # Draw arrow to next element
            if i < num_elements - 1:
                arrow_x = x + box_width + 5
                arrow_y = y + box_height // 2
                draw.line([(arrow_x, arrow_y), (arrow_x + spacing - 10, arrow_y)], fill=ACCENT_PURPLE, width=3)
                # Arrow head
                draw.polygon([
                    (arrow_x + spacing - 10, arrow_y - 8),
                    (arrow_x + spacing, arrow_y),
                    (arrow_x + spacing - 10, arrow_y + 8)
                ], fill=ACCENT_PURPLE)

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def create_highlight_slide(main_text: str, highlight: str, output_path: Path = None) -> Image.Image:
    """Create a slide with highlighted text for emphasis."""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_accent_lines(draw, WIDTH, HEIGHT)

    # Fonts
    main_font = get_font(56, bold=True)
    highlight_font = get_font(72, bold=True)

    # Draw main text
    lines = wrap_text(main_text, main_font, WIDTH - 200, draw)
    y = 200
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=main_font)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, y), line, fill=LIGHT_GRAY, font=main_font)
        y += 70

    # Draw highlighted text
    bbox = draw.textbbox((0, 0), highlight, font=highlight_font)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = HEIGHT // 2 + 50

    # Background for highlight
    padding = 20
    draw.rounded_rectangle(
        [(x - padding, y - padding), (x + (bbox[2] - bbox[0]) + padding, y + (bbox[3] - bbox[1]) + padding)],
        radius=15,
        fill=ACCENT_PURPLE
    )
    draw.text((x, y), highlight, fill=WHITE, font=highlight_font)

    if output_path:
        img.save(output_path)
        print(f"Created: {output_path}")

    return img


def generate_assets_for_script(script_path: Path, output_dir: Path):
    """Generate all visual assets for a parsed script."""
    with open(script_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    output_dir.mkdir(parents=True, exist_ok=True)

    script_id = data.get('script_id', 'unknown')
    print(f"\nGenerating assets for: {data.get('title', script_id)}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)

    for seg in data.get('segments', []):
        seg_id = seg.get('segment_id', 0)
        visual_type = seg.get('visual_type', 'text_overlay')
        visual_cue = seg.get('visual_cue', '')

        output_path = output_dir / f"segment_{seg_id:03d}.png"

        # Parse the visual cue to determine content
        cue_lower = visual_cue.lower()

        if visual_type == 'animated_title' or 'title' in cue_lower:
            # Extract title from visual cue
            title = visual_cue.split(' - ')[-1] if ' - ' in visual_cue else visual_cue
            title = title.replace('"', '').strip()[:60]
            create_title_slide(title, output_path=output_path)

        elif visual_type == 'flowchart' or 'diagram' in cue_lower or 'architecture' in cue_lower:
            # Create a flowchart slide
            title = visual_cue[:50] + "..." if len(visual_cue) > 50 else visual_cue
            elements = [
                {'text': 'Input'},
                {'text': 'Process'},
                {'text': 'AI Agent'},
                {'text': 'Output'}
            ]
            create_diagram_slide(title, elements, output_path=output_path)

        elif 'bullet' in cue_lower or 'list' in cue_lower or visual_type == 'text_overlay':
            # Create content slide
            title = visual_cue[:60] if len(visual_cue) <= 60 else visual_cue[:57] + "..."
            # Generate generic bullet points based on context
            bullets = []
            if 'trigger' in cue_lower:
                bullets = ["Webhook receives data", "Form submission detected", "Automation starts"]
            elif 'ai' in cue_lower or 'agent' in cue_lower:
                bullets = ["AI analyzes input", "Generates response", "Applies business rules"]
            elif 'automation' in cue_lower:
                bullets = ["Connect services", "Execute workflow", "Handle results"]

            if bullets:
                create_content_slide(title, bullets, output_path=output_path)
            else:
                create_title_slide(title, output_path=output_path)

        else:
            # Default: create a simple title slide with the visual cue
            title = visual_cue[:60] if len(visual_cue) <= 60 else visual_cue[:57] + "..."
            create_title_slide(title, output_path=output_path)

        print(f"  Segment {seg_id}: {visual_type} -> {output_path.name}")

    print(f"\nGenerated {len(data.get('segments', []))} assets")
    return output_dir


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate slide assets for video composition")
    parser.add_argument("--script", type=Path, help="Path to parsed script JSON")
    parser.add_argument("--output", type=Path, help="Output directory for assets")
    parser.add_argument("--demo", action="store_true", help="Generate demo slides")

    args = parser.parse_args()

    if args.demo:
        # Generate demo slides
        output_dir = Path("output/demo-assets")
        output_dir.mkdir(parents=True, exist_ok=True)

        print("Generating demo slides...")
        create_title_slide("CAPSTONE PROJECT", "Module 8.1: Your First Agent Workflow", output_dir / "demo_title.png")
        create_content_slide("Key Concepts", [
            "Automated client onboarding",
            "AI-powered data processing",
            "Seamless integrations",
            "Real-time notifications"
        ], output_dir / "demo_content.png")
        create_diagram_slide("System Architecture", [
            {'text': 'Trigger'},
            {'text': 'AI Agent'},
            {'text': 'Automation'},
            {'text': 'Output'}
        ], output_dir / "demo_diagram.png")
        create_highlight_slide("Transform Your Business", "10-20 HOURS SAVED PER WEEK", output_dir / "demo_highlight.png")
        print(f"\nDemo slides saved to: {output_dir}")

    elif args.script:
        output_dir = args.output or Path("output/generated-assets") / args.script.stem
        generate_assets_for_script(args.script, output_dir)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
