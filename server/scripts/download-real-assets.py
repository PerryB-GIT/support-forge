#!/usr/bin/env python3
"""
Download real brand logos and tool screenshots for AI Launchpad Academy slides.
"""

import os
import requests
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import io

# Output directories
OUTPUT_DIR = Path(__file__).parent / "output" / "slide-images"
LOGOS_DIR = OUTPUT_DIR / "logos"
SCREENSHOTS_DIR = OUTPUT_DIR / "screenshots"

# Create directories
LOGOS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

# Real logo URLs from official sources and CDNs
LOGO_SOURCES = {
    # n8n - official logo
    "n8n": "https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png",
    "n8n_alt": "https://n8n.io/n8n-logo.png",

    # Anthropic/Claude - from their brand assets
    "claude": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Anthropic_logo.svg/512px-Anthropic_logo.svg.png",

    # Google products - from Google's official icon sources
    "google_drive": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Google_Drive_icon_%282020%29.svg/512px-Google_Drive_icon_%282020%29.svg.png",
    "google_sheets": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Google_Sheets_logo_%282014-2020%29.svg/512px-Google_Sheets_logo_%282014-2020%29.svg.png",
    "google_calendar": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Calendar_icon_%282020%29.svg/512px-Google_Calendar_icon_%282020%29.svg.png",
    "gmail": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/512px-Gmail_icon_%282020%29.svg.png",

    # Slack
    "slack": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Slack_icon_2019.svg/512px-Slack_icon_2019.svg.png",

    # Webhook - use a custom design
    "webhook": None,  # We'll create this

    # Zapier
    "zapier": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Zapier_logo.svg/512px-Zapier_logo.svg.png",
}

# Screenshot URLs - product pages and documentation
SCREENSHOT_SOURCES = {
    # n8n workflow editor
    "n8n_workflow": "https://n8nio.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5e2a4b8f-3f36-4b22-a1c1-5b4a8e2f3b1a%2Fn8n-workflow.png",
    "n8n_editor": "https://docs.n8n.io/assets/images/n8n-workflow-b0c8d6e7e8b0c8d6e7e8b0c8d6e7e8b0.png",

    # Google Sheets
    "google_sheets_interface": "https://www.gstatic.com/images/branding/product/2x/sheets_2020q4_48dp.png",

    # Slack notifications
    "slack_notification": "https://a.slack-edge.com/80588/marketing/img/features/hero-apps.jpg",
}


def download_image(url: str, output_path: Path, timeout: int = 30) -> bool:
    """Download an image from URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        # Try to open as image to validate
        img = Image.open(io.BytesIO(response.content))

        # Convert to RGBA if needed
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Save as PNG
        img.save(output_path, 'PNG')
        print(f"  Downloaded: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Failed to download {url}: {e}")
        return False


def create_webhook_icon(output_path: Path, size: int = 512):
    """Create a webhook icon."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Purple background circle
    margin = size // 8
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        fill=(139, 92, 246)  # Purple
    )

    # Draw webhook hook shape
    center = size // 2
    hook_color = (255, 255, 255)
    line_width = size // 12

    # Arrow pointing right with hook
    points = [
        (size * 0.25, center),
        (size * 0.55, center),
        (size * 0.55, center - size * 0.15),
        (size * 0.75, center),
        (size * 0.55, center + size * 0.15),
        (size * 0.55, center),
    ]
    draw.line([(size * 0.25, center), (size * 0.55, center)], fill=hook_color, width=line_width)
    draw.polygon([
        (size * 0.55, center - size * 0.12),
        (size * 0.72, center),
        (size * 0.55, center + size * 0.12),
    ], fill=hook_color)

    img.save(output_path, 'PNG')
    print(f"  Created: {output_path.name}")


def create_n8n_logo(output_path: Path, size: int = 512):
    """Create n8n logo if download fails."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # n8n brand color - coral/salmon
    n8n_color = (234, 79, 61)  # #EA4F3D

    # Background rounded square
    margin = size // 10
    radius = size // 5
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=radius,
        fill=n8n_color
    )

    # Draw "n8n" text
    try:
        font_size = size // 4
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text = "n8n"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size - text_width) // 2
    y = (size - text_height) // 2

    draw.text((x, y), text, fill=(255, 255, 255), font=font)

    img.save(output_path, 'PNG')
    print(f"  Created fallback: {output_path.name}")


def create_claude_logo(output_path: Path, size: int = 512):
    """Create Claude/Anthropic logo if download fails."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Anthropic tan/brown color
    claude_color = (204, 153, 102)  # Tan

    # Background circle
    margin = size // 10
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        fill=claude_color
    )

    # Draw "C" for Claude
    try:
        font_size = size // 2
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text = "C"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size - text_width) // 2
    y = (size - text_height) // 2 - size // 20

    draw.text((x, y), text, fill=(255, 255, 255), font=font)

    img.save(output_path, 'PNG')
    print(f"  Created fallback: {output_path.name}")


def download_from_simpleicons(name: str, output_path: Path, color: str = "white"):
    """Download SVG from Simple Icons and convert to PNG."""
    # Simple Icons provides brand SVGs
    url = f"https://cdn.simpleicons.org/{name}/{color}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            # Save SVG and convert would require cairosvg
            # For now, just note it worked
            print(f"  SimpleIcons available for: {name}")
            return True
    except:
        pass
    return False


def create_google_style_icon(name: str, output_path: Path, colors: list, size: int = 512):
    """Create Google-style product icon."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Map names to colors and shapes
    icon_configs = {
        'google_drive': {
            'colors': [(66, 133, 244), (52, 168, 83), (251, 188, 4)],  # Blue, Green, Yellow
            'shape': 'triangle'
        },
        'google_sheets': {
            'colors': [(52, 168, 83)],  # Green
            'shape': 'grid'
        },
        'google_calendar': {
            'colors': [(66, 133, 244), (234, 67, 53), (251, 188, 4), (52, 168, 83)],
            'shape': 'calendar'
        },
        'gmail': {
            'colors': [(234, 67, 53), (66, 133, 244)],  # Red, Blue
            'shape': 'envelope'
        },
        'slack': {
            'colors': [(224, 30, 90), (44, 186, 168), (236, 178, 46), (54, 197, 240)],
            'shape': 'hash'
        }
    }

    config = icon_configs.get(name, {'colors': [(100, 100, 100)], 'shape': 'square'})

    margin = size // 8

    if config['shape'] == 'grid':
        # Google Sheets style - green with grid
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 10,
            fill=config['colors'][0]
        )
        # Grid lines
        line_color = (255, 255, 255, 180)
        for i in range(1, 4):
            y = margin + (size - 2*margin) * i // 4
            draw.line([(margin + size//10, y), (size - margin - size//10, y)], fill=line_color, width=3)
        for i in range(1, 3):
            x = margin + (size - 2*margin) * i // 3
            draw.line([(x, margin + size//10), (x, size - margin - size//10)], fill=line_color, width=3)

    elif config['shape'] == 'calendar':
        # Calendar style
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 12,
            fill=(255, 255, 255)
        )
        # Top bar (red)
        draw.rectangle(
            [(margin, margin), (size - margin, margin + size//5)],
            fill=(66, 133, 244)
        )
        # Date number
        try:
            font = ImageFont.truetype("arial.ttf", size // 3)
        except:
            font = ImageFont.load_default()
        draw.text((size//2 - size//8, size//2 - size//10), "31", fill=(60, 60, 60), font=font)

    elif config['shape'] == 'envelope':
        # Gmail envelope
        draw.rounded_rectangle(
            [(margin, margin + size//6), (size - margin, size - margin - size//8)],
            radius=size // 15,
            fill=(255, 255, 255)
        )
        # M shape
        draw.polygon([
            (margin + size//10, margin + size//5),
            (size//2, size//2 + size//10),
            (size - margin - size//10, margin + size//5),
            (size - margin - size//10, margin + size//4),
            (size//2, size//2 + size//6),
            (margin + size//10, margin + size//4),
        ], fill=(234, 67, 53))

    elif config['shape'] == 'hash':
        # Slack hashtag
        bg_color = (74, 21, 75)  # Slack purple
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 8,
            fill=bg_color
        )
        # Colorful dots in 2x2 grid
        dot_size = size // 5
        positions = [
            (size * 0.3, size * 0.3, (224, 30, 90)),   # Red
            (size * 0.7, size * 0.3, (44, 186, 168)),  # Green
            (size * 0.3, size * 0.7, (236, 178, 46)),  # Yellow
            (size * 0.7, size * 0.7, (54, 197, 240)),  # Blue
        ]
        for x, y, color in positions:
            draw.ellipse([
                (x - dot_size//2, y - dot_size//2),
                (x + dot_size//2, y + dot_size//2)
            ], fill=color)
    else:
        # Default square
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 8,
            fill=config['colors'][0] if config['colors'] else (100, 100, 100)
        )

    img.save(output_path, 'PNG')
    print(f"  Created: {output_path.name}")


def create_n8n_screenshot(output_path: Path, width: int = 1920, height: int = 1080):
    """Create a mock n8n workflow screenshot."""
    img = Image.new('RGB', (width, height), (30, 30, 40))  # Dark background
    draw = ImageDraw.Draw(img)

    # Sidebar
    draw.rectangle([(0, 0), (60, height)], fill=(20, 20, 30))

    # Top bar
    draw.rectangle([(60, 0), (width, 50)], fill=(25, 25, 35))

    # Canvas area
    canvas_color = (35, 35, 45)
    draw.rectangle([(60, 50), (width, height)], fill=canvas_color)

    # Draw workflow nodes
    nodes = [
        {"x": 200, "y": 300, "color": (234, 79, 61), "label": "Webhook"},
        {"x": 450, "y": 300, "color": (139, 92, 246), "label": "Claude AI"},
        {"x": 700, "y": 200, "color": (52, 168, 83), "label": "Google Drive"},
        {"x": 700, "y": 400, "color": (52, 168, 83), "label": "Google Sheets"},
        {"x": 950, "y": 300, "color": (66, 133, 244), "label": "Gmail"},
        {"x": 1150, "y": 300, "color": (74, 21, 75), "label": "Slack"},
    ]

    try:
        font = ImageFont.truetype("arial.ttf", 14)
        small_font = ImageFont.truetype("arial.ttf", 11)
    except:
        font = ImageFont.load_default()
        small_font = font

    # Draw connections first
    for i in range(len(nodes) - 1):
        n1, n2 = nodes[i], nodes[i + 1]
        # Handle branching
        if i == 1:  # After Claude, branch to Drive and Sheets
            draw.line([(n1["x"] + 60, n1["y"]), (nodes[2]["x"], nodes[2]["y"])], fill=(100, 100, 120), width=2)
            draw.line([(n1["x"] + 60, n1["y"]), (nodes[3]["x"], nodes[3]["y"])], fill=(100, 100, 120), width=2)
        elif i == 2:  # Drive to Gmail
            draw.line([(n1["x"] + 60, n1["y"]), (nodes[4]["x"], nodes[4]["y"])], fill=(100, 100, 120), width=2)
        elif i == 3:  # Sheets to Gmail (merge)
            draw.line([(n1["x"] + 60, n1["y"]), (nodes[4]["x"], nodes[4]["y"])], fill=(100, 100, 120), width=2)
        elif i >= 4:
            draw.line([(n1["x"] + 60, n1["y"]), (n2["x"], n2["y"])], fill=(100, 100, 120), width=2)
        else:
            draw.line([(n1["x"] + 60, n1["y"]), (n2["x"], n2["y"])], fill=(100, 100, 120), width=2)

    # Draw nodes
    for node in nodes:
        x, y = node["x"], node["y"]
        # Node box
        draw.rounded_rectangle(
            [(x, y - 30), (x + 120, y + 30)],
            radius=8,
            fill=node["color"]
        )
        # Label
        bbox = draw.textbbox((0, 0), node["label"], font=font)
        text_width = bbox[2] - bbox[0]
        draw.text((x + 60 - text_width//2, y - 8), node["label"], fill=(255, 255, 255), font=font)

    # Title
    draw.text((80, 15), "Client Onboarding Workflow", fill=(200, 200, 200), font=font)

    # Add "n8n" branding
    draw.text((15, 15), "n8n", fill=(234, 79, 61), font=font)

    img.save(output_path, 'JPEG', quality=90)
    print(f"  Created: {output_path.name}")


def create_slack_notification_screenshot(output_path: Path, width: int = 800, height: int = 400):
    """Create a mock Slack notification screenshot."""
    img = Image.new('RGB', (width, height), (26, 29, 33))  # Slack dark theme
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
        bold_font = ImageFont.truetype("arialbd.ttf", 16)
        small_font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
        bold_font = font
        small_font = font

    # Channel header
    draw.rectangle([(0, 0), (width, 50)], fill=(32, 36, 41))
    draw.text((20, 15), "# client-notifications", fill=(255, 255, 255), font=font)

    # Message
    y_pos = 80

    # Bot avatar (circle)
    draw.ellipse([(20, y_pos), (55, y_pos + 35)], fill=(139, 92, 246))
    draw.text((30, y_pos + 7), "AI", fill=(255, 255, 255), font=small_font)

    # Bot name and timestamp
    draw.text((70, y_pos), "Onboarding Agent", fill=(255, 255, 255), font=bold_font)
    draw.text((210, y_pos + 2), "2:34 PM", fill=(128, 128, 128), font=small_font)

    # Message content
    y_pos += 30
    draw.text((70, y_pos), "New client onboarded successfully!", fill=(220, 220, 220), font=font)

    # Attachment box
    y_pos += 40
    draw.rectangle([(70, y_pos), (width - 40, y_pos + 120)], fill=(36, 40, 45))
    draw.rectangle([(70, y_pos), (74, y_pos + 120)], fill=(52, 168, 83))  # Green bar

    # Attachment content
    draw.text((90, y_pos + 15), "Client: Acme Corporation", fill=(200, 200, 200), font=font)
    draw.text((90, y_pos + 40), "Email: contact@acme.com", fill=(160, 160, 160), font=small_font)
    draw.text((90, y_pos + 60), "Service: Premium Package", fill=(160, 160, 160), font=small_font)
    draw.text((90, y_pos + 80), "Folder created | Sheet updated | Welcome email sent", fill=(100, 180, 100), font=small_font)

    img.save(output_path, 'JPEG', quality=90)
    print(f"  Created: {output_path.name}")


def create_google_sheets_screenshot(output_path: Path, width: int = 1200, height: int = 700):
    """Create a mock Google Sheets screenshot."""
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 13)
        header_font = ImageFont.truetype("arialbd.ttf", 13)
        title_font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()
        header_font = font
        title_font = font

    # Green header bar
    draw.rectangle([(0, 0), (width, 60)], fill=(52, 168, 83))
    draw.text((70, 20), "Client Database", fill=(255, 255, 255), font=title_font)

    # Toolbar area
    draw.rectangle([(0, 60), (width, 110)], fill=(247, 249, 250))

    # Column headers
    headers = ["A", "B", "C", "D", "E", "F"]
    col_labels = ["Client Name", "Email", "Service", "Start Date", "Status", "Folder Link"]
    col_width = 180

    # Row numbers column
    draw.rectangle([(0, 110), (40, height)], fill=(247, 249, 250))

    # Header row
    for i, (h, label) in enumerate(zip(headers, col_labels)):
        x = 40 + i * col_width
        draw.rectangle([(x, 110), (x + col_width, 140)], fill=(247, 249, 250), outline=(218, 220, 224))
        draw.text((x + 10, 118), label, fill=(60, 60, 60), font=header_font)

    # Data rows
    data = [
        ["Acme Corp", "acme@example.com", "Premium", "2024-01-15", "Active", "View Folder"],
        ["TechStart Inc", "info@techstart.com", "Standard", "2024-01-14", "Active", "View Folder"],
        ["Global Services", "hello@global.com", "Enterprise", "2024-01-13", "Onboarding", "View Folder"],
        ["LocalBiz LLC", "contact@localbiz.com", "Basic", "2024-01-12", "Active", "View Folder"],
    ]

    for row_idx, row_data in enumerate(data):
        y = 140 + row_idx * 30
        # Row number
        draw.text((15, y + 5), str(row_idx + 2), fill=(100, 100, 100), font=font)

        for col_idx, cell in enumerate(row_data):
            x = 40 + col_idx * col_width
            # Cell border
            draw.rectangle([(x, y), (x + col_width, y + 30)], outline=(218, 220, 224))

            # Cell content
            color = (60, 60, 60)
            if col_idx == 4:  # Status column
                if cell == "Active":
                    color = (52, 168, 83)
                elif cell == "Onboarding":
                    color = (251, 188, 4)
            elif col_idx == 5:  # Link column
                color = (66, 133, 244)

            draw.text((x + 10, y + 7), cell, fill=color, font=font)

    # Grid for empty cells
    for row_idx in range(len(data), 15):
        y = 140 + row_idx * 30
        draw.text((15, y + 5), str(row_idx + 2), fill=(100, 100, 100), font=font)
        for col_idx in range(6):
            x = 40 + col_idx * col_width
            draw.rectangle([(x, y), (x + col_width, y + 30)], outline=(218, 220, 224))

    img.save(output_path, 'JPEG', quality=90)
    print(f"  Created: {output_path.name}")


def main():
    print("=" * 60)
    print("Downloading Real Brand Assets")
    print("=" * 60)

    # Try to download real logos
    print("\n1. Downloading brand logos...")

    downloaded_logos = {}

    for name, url in LOGO_SOURCES.items():
        output_path = LOGOS_DIR / f"{name}.png"

        if url is None:
            # Create custom icon
            if name == "webhook":
                create_webhook_icon(output_path)
                downloaded_logos[name] = True
            continue

        success = download_image(url, output_path)
        downloaded_logos[name] = success

        # If download failed, create fallback
        if not success:
            if name == "n8n" or name == "n8n_alt":
                create_n8n_logo(LOGOS_DIR / "n8n.png")
            elif name == "claude":
                create_claude_logo(output_path)
            elif name in ["google_drive", "google_sheets", "google_calendar", "gmail", "slack"]:
                create_google_style_icon(name, output_path, [])

    # Create high-quality Google-style icons as fallbacks/improvements
    print("\n2. Creating polished product icons...")
    for name in ["google_drive", "google_sheets", "google_calendar", "gmail", "slack"]:
        output_path = LOGOS_DIR / f"{name}_styled.png"
        create_google_style_icon(name, output_path, [])

    # Create screenshots
    print("\n3. Creating tool screenshots...")

    create_n8n_screenshot(SCREENSHOTS_DIR / "n8n_workflow.png")
    create_slack_notification_screenshot(SCREENSHOTS_DIR / "slack_notification.png")
    create_google_sheets_screenshot(SCREENSHOTS_DIR / "google_sheets.png")

    # Summary
    print("\n" + "=" * 60)
    print("Asset Download Complete!")
    print("=" * 60)
    print(f"\nLogos saved to: {LOGOS_DIR}")
    print(f"Screenshots saved to: {SCREENSHOTS_DIR}")

    # List all files
    print("\nLogo files:")
    for f in sorted(LOGOS_DIR.glob("*.png")):
        print(f"  - {f.name}")

    print("\nScreenshot files:")
    for f in sorted(SCREENSHOTS_DIR.glob("*")):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
