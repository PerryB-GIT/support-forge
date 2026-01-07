#!/usr/bin/env python3
"""
Generate slides for 7.1 Credential Security
"""

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output/credential-slides"
SCRIPT_PATH = SCRIPT_DIR / "output/parsed-scripts/7.1-credential-security.json"
BACKGROUNDS_DIR = SCRIPT_DIR / "output/slide-images/backgrounds"
LOGOS_DIR = SCRIPT_DIR / "output/slide-images/logos"
ICONS_DIR = SCRIPT_DIR / "output/slide-images/icons"

# Brand colors
DARK_PURPLE = (30, 27, 75)
ACCENT_PURPLE = (139, 92, 246)
DARK_RED = (127, 29, 29)  # Security warning color
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
WARNING_YELLOW = (234, 179, 8)

WIDTH, HEIGHT = 1920, 1080

# Background mapping
VISUAL_BACKGROUNDS = {
    "text_overlay": "technology.jpg",
    "animated_title": "ai_abstract.jpg",
    "illustration": "collaboration.jpg",
    "screen_capture": "workspace.jpg",
    "code_display": "technology.jpg",
}

# Security-related logos
SEGMENT_LOGOS = {
    4: ["zapier"],
    5: ["n8n"],
}


def get_font(size, bold=False):
    fonts = ["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"]
    if bold:
        fonts = ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"] + fonts
    for font_path in fonts:
        try:
            return ImageFont.truetype(font_path, size)
        except:
            continue
    return ImageFont.load_default()


def load_background(name):
    path = BACKGROUNDS_DIR / name
    if path.exists():
        img = Image.open(path).convert('RGB')
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        overlay = Image.new('RGB', (WIDTH, HEIGHT), DARK_PURPLE)
        return Image.blend(img, overlay, 0.7)
    return Image.new('RGB', (WIDTH, HEIGHT), DARK_PURPLE)


def load_logo(name, size=100):
    for variant in [f"{name}.png", f"{name}_styled.png"]:
        path = LOGOS_DIR / variant
        if path.exists():
            logo = Image.open(path).convert('RGBA')
            ratio = min(size / logo.width, size / logo.height)
            new_size = (int(logo.width * ratio), int(logo.height * ratio))
            return logo.resize(new_size, Image.Resampling.LANCZOS)
    path = ICONS_DIR / f"{name}.png"
    if path.exists():
        icon = Image.open(path).convert('RGBA')
        return icon.resize((size, size), Image.Resampling.LANCZOS)
    return None


def wrap_text(text, font, max_width, draw):
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


def clean_text(text):
    """Remove narrator directions like [Pause], [Beat], etc."""
    import re
    # Remove bracketed directions
    text = re.sub(r'\[Pause\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[Beat\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[.*?pause.*?\]', '', text, flags=re.IGNORECASE)
    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_heading(text):
    text = clean_text(text)
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('###'):
            return line.replace('###', '').strip()
        if line.startswith('##'):
            return line.replace('##', '').strip()
        if line.startswith('#'):
            return line.replace('#', '').strip()
    first_line = text.split('.')[0].strip()
    if len(first_line) > 60:
        first_line = first_line[:57] + "..."
    return first_line


def extract_bullet_points(text, max_points=5):
    text = clean_text(text)
    points = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('-') or line.startswith('*') or line.startswith('•'):
            point = line.lstrip('-*• ').strip()
            if point and len(point) > 3:
                points.append(point)
    if not points:
        sentences = text.replace('\n', ' ').split('.')
        for sent in sentences[:max_points]:
            sent = sent.strip()
            if len(sent) > 10 and len(sent) < 100:
                points.append(sent)
    return points[:max_points]


def create_slide(segment, segment_num):
    visual_type = segment.get('visual_type', 'text_overlay')
    visual_cue = segment.get('visual_cue', '')
    spoken_text = segment.get('spoken_text', '')

    # Security topic - use darker/warning theme for certain segments
    is_warning = any(word in spoken_text.lower() for word in ['breach', 'exposed', 'leaked', 'danger', 'risk'])

    bg_name = VISUAL_BACKGROUNDS.get(visual_type, "technology.jpg")
    img = load_background(bg_name)

    # Add red tint for warning slides
    if is_warning:
        warning_overlay = Image.new('RGB', (WIDTH, HEIGHT), DARK_RED)
        img = Image.blend(img, warning_overlay, 0.3)

    draw = ImageDraw.Draw(img)

    title_font = get_font(64, bold=True)
    body_font = get_font(36)
    small_font = get_font(28)

    heading = extract_heading(spoken_text)
    if not heading and visual_cue:
        heading = visual_cue.split(' - ')[0] if ' - ' in visual_cue else visual_cue[:60]

    # Draw heading
    if heading:
        lines = wrap_text(heading, title_font, WIDTH - 200, draw)
        y = 120
        for line in lines[:2]:
            bbox = draw.textbbox((0, 0), line, font=title_font)
            x = (WIDTH - (bbox[2] - bbox[0])) // 2
            color = WARNING_YELLOW if is_warning else WHITE
            draw.text((x, y), line, font=title_font, fill=color)
            y += 80

    # Draw content
    if visual_type == "code_display" or "```" in spoken_text:
        code_lines = []
        in_code = False
        for line in spoken_text.split('\n'):
            if '```' in line:
                in_code = not in_code
                continue
            if in_code:
                code_lines.append(line)
        if code_lines:
            code_font = get_font(24)
            y = 280
            draw.rectangle([100, 260, WIDTH - 100, HEIGHT - 200], fill=(20, 20, 40))
            for line in code_lines[:15]:
                draw.text((130, y), line[:80], font=code_font, fill=(100, 255, 100))
                y += 35
    else:
        points = extract_bullet_points(spoken_text)
        if points:
            y = 320
            for point in points:
                lines = wrap_text(point, body_font, WIDTH - 300, draw)
                for line in lines[:2]:
                    draw.text((180, y), f"• {line}", font=body_font, fill=LIGHT_GRAY)
                    y += 50
                y += 20

    # Add logos
    logos = SEGMENT_LOGOS.get(segment_num, [])
    if logos:
        x_pos = WIDTH - 150
        for logo_name in logos:
            logo = load_logo(logo_name, 80)
            if logo:
                img.paste(logo, (x_pos, HEIGHT - 120), logo)
                x_pos -= 100

    # Segment number
    draw.text((50, HEIGHT - 60), f"7.1 | Segment {segment_num}", font=small_font, fill=(100, 100, 120))

    return img


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Generating Slides for 7.1 - Credential Security")
    print("=" * 60)

    with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data.get('segments', [])
    print(f"Processing {len(segments)} segments")

    for seg in segments:
        seg_id = seg.get('segment_id', 0)
        print(f"Creating slide {seg_id}...", end=' ')
        slide = create_slide(seg, seg_id)
        output_path = OUTPUT_DIR / f"slide_{seg_id:02d}.png"
        slide.save(output_path, 'PNG')
        print("saved")

    print(f"\nGenerated {len(segments)} slides in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
