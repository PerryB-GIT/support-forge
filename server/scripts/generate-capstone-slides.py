#!/usr/bin/env python3
"""
Generate Capstone Slides with Real Logos and Screenshots
=========================================================
Creates enhanced slides for the capstone video using real brand assets.
"""

import json
import os
from pathlib import Path
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont


# =============================================================================
# CONSTANTS
# =============================================================================

WIDTH = 1920
HEIGHT = 1080
SCRIPT_DIR = Path(__file__).parent
IMAGES_DIR = SCRIPT_DIR / "output" / "slide-images"
ICONS_DIR = IMAGES_DIR / "icons"
LOGOS_DIR = IMAGES_DIR / "logos"
SCREENSHOTS_DIR = IMAGES_DIR / "screenshots"
PHOTOS_DIR = IMAGES_DIR / "photos"
OUTPUT_DIR = SCRIPT_DIR / "output" / "capstone-slides"

# Skip segment 25 - it's production notes, not spoken content
SKIP_SEGMENTS = [25]

class Colors:
    DARK_PURPLE = (30, 27, 75)
    MEDIUM_PURPLE = (45, 40, 100)
    ACCENT_PURPLE = (139, 92, 246)
    LIGHT_PURPLE = (167, 139, 250)
    WHITE = (255, 255, 255)
    OFF_WHITE = (245, 245, 250)
    LIGHT_GRAY = (200, 200, 200)
    SUCCESS_GREEN = (34, 197, 94)

SLIDE_BACKGROUNDS = {
    1: "tech_abstract", 2: "laptop_work", 3: "onboarding", 4: "workflow",
    5: "automation", 6: None, 7: None, 8: None, 9: None,
    10: "architecture_diagram", 11: "business", 12: "handshake", 13: "data",
    14: "success", 15: "workflow", 16: None, 17: "cloud", 18: None,
    19: "laptop_work", 20: None, 21: None, 22: None, 23: "celebrate", 24: "rocket",
}

SLIDE_LOGOS = {
    6: ["webhook"], 7: ["claude"], 8: ["google_drive", "google_sheets", "google_calendar"],
    9: ["gmail", "slack"], 18: ["n8n", "claude", "google_drive", "slack", "gmail"],
    20: ["n8n"], 21: [], 22: [],
}

SLIDE_SCREENSHOTS = {20: "n8n_workflow"}


def get_font(size, bold=False):
    paths = ["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"]
    if bold:
        paths = ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"] + paths
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()


def wrap_text(text, font, max_width, draw):
    if not text:
        return []
    words, lines, current = text.split(), [], []
    for word in words:
        test = ' '.join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))
    return lines


def draw_text_shadow(draw, pos, text, font, fill, offset=(3, 3)):
    draw.text((pos[0] + offset[0], pos[1] + offset[1]), text, fill=(0, 0, 0), font=font)
    draw.text(pos, text, fill=fill, font=font)


def load_background_image(name, overlay_opacity=0.6):
    for ext in ['.jpg', '.png']:
        path = PHOTOS_DIR / f"{name}{ext}"
        if path.exists():
            try:
                bg = Image.open(path).convert('RGB')
                ratio = bg.width / bg.height
                canvas_ratio = WIDTH / HEIGHT
                if ratio > canvas_ratio:
                    new_h, new_w = HEIGHT, int(HEIGHT * ratio)
                else:
                    new_w, new_h = WIDTH, int(WIDTH / ratio)
                bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
                x, y = (new_w - WIDTH) // 2, (new_h - HEIGHT) // 2
                bg = bg.crop((x, y, x + WIDTH, y + HEIGHT))
                overlay = Image.new('RGB', (WIDTH, HEIGHT), Colors.DARK_PURPLE)
                return Image.blend(bg, overlay, overlay_opacity)
            except Exception as e:
                print(f"    Warning: {name}: {e}")
    return None


def load_logo(name, size=120):
    for var in [f"{name}.png", f"{name}_styled.png"]:
        path = LOGOS_DIR / var
        if path.exists():
            try:
                logo = Image.open(path).convert('RGBA')
                ratio = min(size / logo.width, size / logo.height)
                logo = logo.resize((int(logo.width * ratio), int(logo.height * ratio)), Image.Resampling.LANCZOS)
                return logo
            except:
                pass
    path = ICONS_DIR / f"{name}.png"
    if path.exists():
        try:
            icon = Image.open(path).convert('RGBA')
            return icon.resize((size, size), Image.Resampling.LANCZOS)
        except:
            pass
    return None


def load_screenshot(name, max_w=1400, max_h=700):
    for ext in ['.png', '.jpg']:
        path = SCREENSHOTS_DIR / f"{name}{ext}"
        if path.exists():
            try:
                ss = Image.open(path).convert('RGBA')
                ratio = min(max_w / ss.width, max_h / ss.height)
                return ss.resize((int(ss.width * ratio), int(ss.height * ratio)), Image.Resampling.LANCZOS)
            except:
                pass
    return None


def create_gradient_background():
    img = Image.new('RGB', (WIDTH, HEIGHT), Colors.DARK_PURPLE)
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        f = y / HEIGHT * 0.3
        draw.line([(0, y), (WIDTH, y)], fill=(
            int(Colors.DARK_PURPLE[0] + f * 20),
            int(Colors.DARK_PURPLE[1] + f * 20),
            int(Colors.DARK_PURPLE[2] + f * 40)
        ))
    return img


def draw_accent_elements(draw):
    draw.rectangle([(0, 0), (WIDTH, 6)], fill=Colors.ACCENT_PURPLE)
    m, cs, w = 40, 60, 3
    draw.line([(m, m), (m, m + cs)], fill=Colors.ACCENT_PURPLE, width=w)
    draw.line([(m, m), (m + cs, m)], fill=Colors.ACCENT_PURPLE, width=w)
    draw.line([(WIDTH - m, m), (WIDTH - m, m + cs)], fill=Colors.ACCENT_PURPLE, width=w)
    draw.line([(WIDTH - m, m), (WIDTH - m - cs, m)], fill=Colors.ACCENT_PURPLE, width=w)


def paste_logos(img, logos, position="right", size=100):
    if not logos:
        return
    if position == "right":
        x_start, y_start, spacing = WIDTH - 180, 200, size + 30
        for i, name in enumerate(logos[:5]):
            logo = load_logo(name, size)
            if logo:
                img.paste(logo, (x_start - logo.width // 2, y_start + i * spacing), logo)
    elif position == "bottom":
        y = HEIGHT - 180
        total_w = len(logos) * size + (len(logos) - 1) * 40
        x_start = (WIDTH - total_w) // 2
        for i, name in enumerate(logos):
            logo = load_logo(name, size)
            if logo:
                img.paste(logo, (x_start + i * (size + 40) + (size - logo.width) // 2, y), logo)


def create_title_slide(title, subtitle="", bg_name=None, logos=None):
    img = load_background_image(bg_name, 0.65) if bg_name else None
    if img is None:
        img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_elements(draw)

    tf, sf = get_font(72, True), get_font(42)
    lines = wrap_text(title.upper(), tf, WIDTH - 200, draw)
    total_h = len(lines) * 90 + (70 if subtitle else 0)
    start_y = (HEIGHT - total_h) // 2

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=tf)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw_text_shadow(draw, (x, start_y + i * 90), line, tf, Colors.WHITE, (4, 4))

    if subtitle:
        y = start_y + len(lines) * 90 + 30
        bbox = draw.textbbox((0, 0), subtitle, font=sf)
        draw_text_shadow(draw, ((WIDTH - (bbox[2] - bbox[0])) // 2, y), subtitle, sf, Colors.ACCENT_PURPLE)

    if logos:
        paste_logos(img, logos, "bottom", 80)
    return img


def create_content_slide(title, bullets, bg_name=None, logos=None, screenshot=None):
    img = load_background_image(bg_name, 0.75) if bg_name else None
    if img is None:
        img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_elements(draw)

    tf, bf = get_font(56, True), get_font(32)
    draw_text_shadow(draw, (120, 100), title, tf, Colors.WHITE)
    bbox = draw.textbbox((120, 100), title, font=tf)
    draw.line([(120, bbox[3] + 15), (bbox[2] + 30, bbox[3] + 15)], fill=Colors.ACCENT_PURPLE, width=4)

    content_w = WIDTH - 400
    if screenshot:
        ss = load_screenshot(screenshot, 700, 500)
        if ss:
            img.paste(ss, (WIDTH - ss.width - 80, 220), ss)
            content_w = WIDTH - ss.width - 250
    elif logos:
        paste_logos(img, logos, "right", 100)
        content_w = WIDTH - 350

    y = 220
    for bullet in bullets:
        draw.ellipse([(120, y + 12), (136, y + 28)], fill=Colors.ACCENT_PURPLE)
        for line in wrap_text(bullet, bf, content_w, draw):
            draw_text_shadow(draw, (160, y), line, bf, Colors.OFF_WHITE, (2, 2))
            y += 45
        y += 20
    return img


def create_architecture_slide(title, elements, bg_name=None, screenshot=None):
    if bg_name == "architecture_diagram":
        path = PHOTOS_DIR / "architecture_diagram.png"
        if path.exists():
            return Image.open(path).convert('RGB')

    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_elements(draw)

    tf, ef = get_font(42, True), get_font(24)
    bbox = draw.textbbox((0, 0), title, font=tf)
    draw.text(((WIDTH - (bbox[2] - bbox[0])) // 2, 60), title, fill=Colors.WHITE, font=tf)

    if not elements:
        return img

    bw, bh, sp = 200, 80, 50
    num = len(elements)
    start_x = (WIDTH - num * bw - (num - 1) * sp) // 2
    cy = HEIGHT // 2 + 30

    for i, elem in enumerate(elements):
        x, y = start_x + i * (bw + sp), cy - bh // 2
        draw.rounded_rectangle([(x + 4, y + 4), (x + bw + 4, y + bh + 4)], radius=10, fill=(20, 18, 50))
        draw.rounded_rectangle([(x, y), (x + bw, y + bh)], radius=10, fill=Colors.MEDIUM_PURPLE, outline=Colors.ACCENT_PURPLE, width=2)

        text = elem.get('text', str(elem)) if isinstance(elem, dict) else str(elem)
        lines = wrap_text(text, ef, bw - 20, draw)
        ty = y + (bh - len(lines) * 30) // 2
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=ef)
            draw.text((x + (bw - (bbox[2] - bbox[0])) // 2, ty), line, fill=Colors.WHITE, font=ef)
            ty += 30

        if i < num - 1:
            ax = x + bw + 5
            draw.line([(ax, cy), (ax + sp - 10, cy)], fill=Colors.ACCENT_PURPLE, width=3)
            draw.polygon([(ax + sp - 10, cy - 8), (ax + sp, cy), (ax + sp - 10, cy + 8)], fill=Colors.ACCENT_PURPLE)
    return img


def create_highlight_slide(main_text, highlight, bg_name=None, logos=None):
    img = load_background_image(bg_name, 0.7) if bg_name else None
    if img is None:
        img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_elements(draw)

    mf, hf = get_font(42), get_font(64, True)
    y = 280
    for line in wrap_text(main_text, mf, WIDTH - 200, draw):
        bbox = draw.textbbox((0, 0), line, font=mf)
        draw.text(((WIDTH - (bbox[2] - bbox[0])) // 2, y), line, fill=Colors.LIGHT_GRAY, font=mf)
        y += 55

    h_lines = wrap_text(highlight, hf, WIDTH - 200, draw)
    if h_lines:
        max_w = max(draw.textbbox((0, 0), l, font=hf)[2] for l in h_lines)
        box_h = len(h_lines) * 80 + 40
        bx, by = (WIDTH - max_w) // 2 - 30, HEIGHT // 2 + 50
        draw.rounded_rectangle([(bx, by), (bx + max_w + 60, by + box_h)], radius=15, fill=Colors.ACCENT_PURPLE)
        hy = by + 20
        for line in h_lines:
            bbox = draw.textbbox((0, 0), line, font=hf)
            draw.text(((WIDTH - (bbox[2] - bbox[0])) // 2, hy), line, fill=Colors.WHITE, font=hf)
            hy += 80

    if logos:
        paste_logos(img, logos, "bottom", 80)
    return img


def create_checklist_slide(title, items, bg_name=None, logos=None):
    img = load_background_image(bg_name, 0.75) if bg_name else None
    if img is None:
        img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_elements(draw)

    tf, itf = get_font(48, True), get_font(28)
    bbox = draw.textbbox((0, 0), title, font=tf)
    draw.text(((WIDTH - (bbox[2] - bbox[0])) // 2, 60), title, fill=Colors.WHITE, font=tf)

    if logos:
        paste_logos(img, logos, "right", 80)

    num = len(items)
    cw, ih, sy = 650, 55, 160

    if num > 6:
        c1x, c2x = 150, 150 + cw + 50
        per_col = (num + 1) // 2
        for i, item in enumerate(items):
            col, row = i // per_col, i % per_col
            x, y = (c1x if col == 0 else c2x), sy + row * ih
            draw.rounded_rectangle([(x, y), (x + 28, y + 28)], radius=5, outline=Colors.ACCENT_PURPLE, width=2)
            item_data = item if isinstance(item, dict) else {'text': item, 'checked': True}
            if item_data.get('checked', True):
                draw.rectangle([(x + 5, y + 5), (x + 23, y + 23)], fill=Colors.SUCCESS_GREEN)
            text = item_data.get('text', str(item))
            for j, line in enumerate(wrap_text(text, itf, cw - 50, draw)):
                draw.text((x + 40, y + j * 30), line, fill=Colors.LIGHT_GRAY, font=itf)
    else:
        x = 200
        for i, item in enumerate(items):
            y = sy + i * ih * 1.2
            draw.rounded_rectangle([(x, y), (x + 32, y + 32)], radius=6, outline=Colors.ACCENT_PURPLE, width=3)
            item_data = item if isinstance(item, dict) else {'text': item, 'checked': True}
            if item_data.get('checked', True):
                draw.rectangle([(x + 6, y + 6), (x + 26, y + 26)], fill=Colors.SUCCESS_GREEN)
            draw.text((x + 50, y), item_data.get('text', str(item)), fill=Colors.WHITE, font=itf)
    return img


def create_steps_slide(title, steps, bg_name=None, logos=None):
    img = load_background_image(bg_name, 0.75) if bg_name else None
    if img is None:
        img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    draw_accent_elements(draw)

    tf = get_font(48, True)
    draw.text((120, 60), title, fill=Colors.WHITE, font=tf)

    if logos:
        paste_logos(img, logos, "right", 100)

    stf, sdf = get_font(32, True), get_font(24)
    y = 160
    for i, step in enumerate(steps[:5]):
        sd = step if isinstance(step, dict) else {'title': str(step)}
        cx, cy, r = 180, y + 30, 30
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=Colors.ACCENT_PURPLE)
        nf = get_font(32, True)
        num = str(sd.get('number', i + 1))
        bbox = draw.textbbox((0, 0), num, font=nf)
        draw.text((cx - (bbox[2] - bbox[0]) // 2, cy - (bbox[3] - bbox[1]) // 2 - 5), num, fill=Colors.WHITE, font=nf)
        draw.text((240, y), sd.get('title', ''), fill=Colors.WHITE, font=stf)
        desc = sd.get('description', '')
        if desc:
            for j, line in enumerate(wrap_text(desc, sdf, WIDTH - 450, draw)):
                draw.text((240, y + 45 + j * 30), line, fill=Colors.LIGHT_GRAY, font=sdf)
        y += 130
    return img


def generate_slide(config, slide_num):
    layout = config.get('layout', 'title')
    bg = SLIDE_BACKGROUNDS.get(slide_num)
    logos = SLIDE_LOGOS.get(slide_num, [])
    ss = SLIDE_SCREENSHOTS.get(slide_num)

    if layout == 'title':
        return create_title_slide(config.get('title', ''), config.get('subtitle', ''), bg, logos)
    elif layout == 'content':
        return create_content_slide(config.get('title', ''), config.get('bullets', config.get('content', [])), bg, logos, ss)
    elif layout == 'architecture':
        return create_architecture_slide(config.get('title', ''), config.get('elements', []), bg, ss)
    elif layout == 'highlight':
        return create_highlight_slide(config.get('main_text', ''), config.get('highlight_text', config.get('highlight', '')), bg, logos)
    elif layout == 'checklist':
        return create_checklist_slide(config.get('title', ''), config.get('items', []), bg, logos)
    elif layout == 'steps':
        return create_steps_slide(config.get('title', ''), config.get('steps', []), bg, logos)
    else:
        return create_title_slide(config.get('title', layout), config.get('subtitle', ''), bg, logos)


def convert_slide_plan_to_config(slide_plan):
    slides = []
    for slide in slide_plan.get('slides', []):
        seg_id = slide.get('segment_id', 0)
        if seg_id in SKIP_SEGMENTS:
            continue

        layout = slide.get('layout', 'title')
        content = slide.get('content', {})
        config = {'slide_number': seg_id, 'duration': slide.get('duration', 5.0)}

        if layout == 'hero_title':
            config.update({'layout': 'title', 'title': content.get('title', ''), 'subtitle': content.get('subtitle', '')})
        elif layout == 'title_card':
            m, t = content.get('module', ''), content.get('title', '')
            config.update({'layout': 'title', 'title': f"{m}: {t}" if m else t, 'subtitle': content.get('tagline', '')})
        elif layout == 'split_image_text':
            bullets = content.get('bullets', [])
            if content.get('emphasis'):
                bullets.append(content['emphasis'])
            config.update({'layout': 'content', 'title': content.get('title', ''), 'bullets': bullets})
        elif layout == 'transformation':
            config.update({'layout': 'highlight', 'main_text': f"From {content.get('before', '')} to...", 'highlight_text': content.get('after', '')})
        elif layout == 'section_intro':
            config.update({'layout': 'title', 'title': content.get('title', ''), 'subtitle': content.get('subtitle', '')})
        elif layout == 'architecture_step':
            sn, nm = content.get('step_number', ''), content.get('step_name', '')
            if content.get('bullets') or content.get('actions'):
                bullets = content.get('bullets', [])
                if content.get('actions'):
                    bullets = [a.get('text', '') for a in content['actions']]
                if content.get('emphasis'):
                    bullets.append(content['emphasis'])
                config.update({'layout': 'content', 'title': f"Step {sn}: {nm}", 'bullets': bullets})
            else:
                config.update({'layout': 'steps', 'title': f"Step {sn}: {nm}", 'steps': [{'number': sn, 'title': nm, 'description': content.get('description', '')}]})
        elif layout == 'full_architecture':
            config.update({'layout': 'architecture', 'title': content.get('title', ''), 'elements': [{'text': s} for s in content.get('flow', [])]})
        elif layout == 'reason_card':
            num, title = content.get('number', ''), content.get('title', '')
            if content.get('skills'):
                config.update({'layout': 'content', 'title': f"{num}. {title}", 'bullets': content['skills']})
            else:
                config.update({'layout': 'highlight', 'main_text': f"Reason {num}", 'highlight_text': title})
        elif layout == 'checklist':
            config.update({'layout': 'checklist', 'title': content.get('title', 'Checklist'), 'items': [{'text': i, 'checked': True} for i in content.get('items', [])]})
        elif layout == 'requirements':
            config.update({'layout': 'checklist', 'title': content.get('title', 'Requirements'), 'items': [{'text': r.get('text', ''), 'checked': False} for r in content.get('requirements', [])]})
        elif layout == 'module_card':
            m = content.get('module', '')
            bullets = []
            if content.get('description'):
                bullets.append(content['description'])
            if content.get('highlight'):
                bullets.append(content['highlight'])
            config.update({'layout': 'content', 'title': f"Module {m}: {content.get('title', '')}", 'bullets': bullets})
        elif layout == 'motivation':
            config.update({'layout': 'highlight', 'main_text': content.get('quote', ''), 'highlight_text': content.get('emphasis', '')})
        elif layout == 'call_to_action':
            config.update({'layout': 'title', 'title': content.get('title', ''), 'subtitle': f"Next: {content.get('next_module', '')}"})
        elif layout == 'end_card':
            config.update({'layout': 'title', 'title': content.get('logo', 'AI Launchpad Academy'), 'subtitle': f"{content.get('badge', '')} | {content.get('tagline', '')}"})
        else:
            config.update({'layout': 'title', 'title': content.get('title', str(content))})

        slides.append(config)
    return slides


def main():
    plan_path = SCRIPT_DIR / "output" / "capstone-slide-plan.json"
    print("=" * 60)
    print("Generating Capstone Slides with Real Assets")
    print("=" * 60)

    print(f"\nLoading slide plan: {plan_path}")
    with open(plan_path, 'r', encoding='utf-8') as f:
        slide_plan = json.load(f)

    print(f"Converting to slide configs (skipping segments: {SKIP_SEGMENTS})...")
    slides_config = convert_slide_plan_to_config(slide_plan)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nGenerating {len(slides_config)} slides...")
    print("-" * 60)

    for config in slides_config:
        slide_num = config.get('slide_number', 0)
        output_path = OUTPUT_DIR / f"slide_{slide_num:03d}.png"
        logos = SLIDE_LOGOS.get(slide_num, [])
        ss = SLIDE_SCREENSHOTS.get(slide_num)
        extras = []
        if logos:
            extras.append(f"logos:{len(logos)}")
        if ss:
            extras.append(f"ss:{ss}")

        print(f"  Slide {slide_num:2d}: {config.get('layout', '?'):12s} {('[' + ', '.join(extras) + ']') if extras else ''}", end="")
        try:
            img = generate_slide(config, slide_num)
            img.save(output_path)
            print(f" -> {output_path.name}")
        except Exception as e:
            print(f" ERROR: {e}")
            create_title_slide(f"Slide {slide_num}", str(e)[:40]).save(output_path)

    print("-" * 60)
    print(f"\nAll slides saved to: {OUTPUT_DIR}")
    print(f"Total: {len(slides_config)} slides (skipped: {len(SKIP_SEGMENTS)})")
    print("=" * 60)


if __name__ == "__main__":
    main()
