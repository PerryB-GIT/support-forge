#!/usr/bin/env python3
"""
Download Slide Images
=====================
Downloads free images from Unsplash and creates tool icons for the capstone video slides.
"""

import os
import sys
import json
import urllib.request
from pathlib import Path
from typing import Optional

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont

# Output directory
OUTPUT_DIR = Path("output/slide-images")
ICONS_DIR = OUTPUT_DIR / "icons"
PHOTOS_DIR = OUTPUT_DIR / "photos"

# Brand colors
COLORS = {
    "n8n": (234, 76, 137),       # #EA4C89 - Pink/magenta
    "claude": (218, 119, 86),    # #DA7756 - Terra cotta
    "google_drive": (66, 133, 244),   # #4285F4 - Blue
    "google_sheets": (52, 168, 83),   # #34A853 - Green
    "google_calendar": (66, 133, 244),  # #4285F4 - Blue
    "gmail": (234, 67, 53),      # #EA4335 - Red
    "slack": (74, 21, 75),       # #4A154B - Purple
    "webhook": (59, 130, 246),   # #3B82F6 - Blue
    "automation": (139, 92, 246),  # #8B5CF6 - Purple (brand)
    "ai": (139, 92, 246),        # Purple
}

# Unsplash image IDs (direct URLs work without API key)
UNSPLASH_IMAGES = {
    "automation": "photo-1518770660439-4636190af475",  # Circuit board / tech
    "workflow": "photo-1551288049-bebda4e38f71",  # Dashboard / analytics
    "business": "photo-1560472355-536de3962603",  # Business meeting
    "onboarding": "photo-1552664730-d307ca884978",  # Team collaboration
    "tech_abstract": "photo-1526374965328-7f61d4dc18c5",  # Matrix code
    "laptop_work": "photo-1498050108023-c5249f4df085",  # Laptop coding
    "success": "photo-1533227268428-f9ed0900fb3b",  # Thumbs up / success
    "teamwork": "photo-1522071820081-009f0129c71c",  # Team working
    "calendar": "photo-1506784983877-45594efa4cbe",  # Calendar planning
    "email": "photo-1596526131083-e8c633c948d2",  # Email / communication
    "data": "photo-1551288049-bebda4e38f71",  # Data dashboard
    "cloud": "photo-1544197150-b99a580bb7a8",  # Cloud computing
    "celebrate": "photo-1531206715517-5c0ba140b2b8",  # Celebration
    "handshake": "photo-1521791136064-7986c2920216",  # Business handshake
    "rocket": "photo-1517976487492-5750f3195933",  # Rocket launch
}


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Get a font with fallbacks."""
    font_paths = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]

    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue

    return ImageFont.load_default()


def download_unsplash_image(image_id: str, output_path: Path, width: int = 1920) -> bool:
    """Download an image from Unsplash using direct URL."""
    url = f"https://images.unsplash.com/{image_id}?w={width}&q=80&fit=crop"

    try:
        print(f"  Downloading: {image_id}...")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=30) as response:
            with open(output_path, 'wb') as f:
                f.write(response.read())

        print(f"  Saved: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error downloading {image_id}: {e}")
        return False


def create_tool_icon(
    name: str,
    color: tuple,
    output_path: Path,
    size: int = 400,
    icon_text: str = None
) -> bool:
    """Create a simple tool/brand icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw rounded rectangle background
        margin = size // 10
        radius = size // 5

        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=radius,
            fill=color
        )

        # Draw icon text/letter
        text = icon_text or name[0].upper()
        font_size = size // 3
        font = get_font(font_size, bold=True)

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (size - text_width) // 2
        y = (size - text_height) // 2 - size // 20

        draw.text((x, y), text, fill=(255, 255, 255), font=font)

        # Save as PNG
        img.save(output_path, 'PNG')
        print(f"  Created icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating icon {name}: {e}")
        return False


def create_n8n_icon(output_path: Path, size: int = 400) -> bool:
    """Create n8n-style workflow icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Background
        margin = size // 10
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 5,
            fill=COLORS["n8n"]
        )

        # Draw workflow nodes (3 connected circles)
        node_radius = size // 10
        center_y = size // 2

        positions = [
            (size // 4, center_y),
            (size // 2, center_y - size // 6),
            (3 * size // 4, center_y),
        ]

        # Draw connections
        for i in range(len(positions) - 1):
            draw.line([positions[i], positions[i + 1]], fill=(255, 255, 255), width=size // 30)

        # Draw nodes
        for x, y in positions:
            draw.ellipse(
                [(x - node_radius, y - node_radius), (x + node_radius, y + node_radius)],
                fill=(255, 255, 255)
            )

        img.save(output_path, 'PNG')
        print(f"  Created n8n icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating n8n icon: {e}")
        return False


def create_claude_icon(output_path: Path, size: int = 400) -> bool:
    """Create Claude AI icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Background circle
        margin = size // 10
        draw.ellipse(
            [(margin, margin), (size - margin, size - margin)],
            fill=COLORS["claude"]
        )

        # Simple "C" for Claude
        font = get_font(size // 2, bold=True)
        bbox = draw.textbbox((0, 0), "C", font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (size - text_width) // 2
        y = (size - text_height) // 2 - size // 15

        draw.text((x, y), "C", fill=(255, 255, 255), font=font)

        img.save(output_path, 'PNG')
        print(f"  Created Claude icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating Claude icon: {e}")
        return False


def create_google_icon(service: str, output_path: Path, size: int = 400) -> bool:
    """Create Google service icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        color = COLORS.get(f"google_{service}", COLORS["google_drive"])

        # Background
        margin = size // 10
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 6,
            fill=color
        )

        # Service-specific icon
        if service == "drive":
            # Triangle for Drive
            center = size // 2
            tri_size = size // 4
            points = [
                (center, center - tri_size),
                (center - tri_size, center + tri_size // 2),
                (center + tri_size, center + tri_size // 2),
            ]
            draw.polygon(points, fill=(255, 255, 255))

        elif service == "sheets":
            # Grid for Sheets
            center = size // 2
            grid_size = size // 4
            cell_size = grid_size // 2
            for i in range(2):
                for j in range(2):
                    x = center - grid_size // 2 + i * cell_size + 2
                    y = center - grid_size // 2 + j * cell_size + 2
                    draw.rectangle(
                        [(x, y), (x + cell_size - 4, y + cell_size - 4)],
                        fill=(255, 255, 255)
                    )

        elif service == "calendar":
            # Calendar icon
            center = size // 2
            cal_size = size // 3
            # Calendar body
            draw.rectangle(
                [(center - cal_size // 2, center - cal_size // 3),
                 (center + cal_size // 2, center + cal_size // 2)],
                fill=(255, 255, 255)
            )
            # Calendar header
            draw.rectangle(
                [(center - cal_size // 2, center - cal_size // 2),
                 (center + cal_size // 2, center - cal_size // 3)],
                fill=(200, 200, 200)
            )
        else:
            # Default: letter
            font = get_font(size // 3, bold=True)
            letter = service[0].upper()
            bbox = draw.textbbox((0, 0), letter, font=font)
            x = (size - (bbox[2] - bbox[0])) // 2
            y = (size - (bbox[3] - bbox[1])) // 2 - size // 15
            draw.text((x, y), letter, fill=(255, 255, 255), font=font)

        img.save(output_path, 'PNG')
        print(f"  Created Google {service} icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating Google {service} icon: {e}")
        return False


def create_slack_icon(output_path: Path, size: int = 400) -> bool:
    """Create Slack-style icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Background
        margin = size // 10
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 5,
            fill=COLORS["slack"]
        )

        # Slack-like # symbol
        center = size // 2
        hash_size = size // 4
        line_width = size // 15

        # Horizontal lines
        draw.rectangle(
            [(center - hash_size, center - hash_size // 3 - line_width // 2),
             (center + hash_size, center - hash_size // 3 + line_width // 2)],
            fill=(255, 255, 255)
        )
        draw.rectangle(
            [(center - hash_size, center + hash_size // 3 - line_width // 2),
             (center + hash_size, center + hash_size // 3 + line_width // 2)],
            fill=(255, 255, 255)
        )

        # Vertical lines
        draw.rectangle(
            [(center - hash_size // 3 - line_width // 2, center - hash_size),
             (center - hash_size // 3 + line_width // 2, center + hash_size)],
            fill=(255, 255, 255)
        )
        draw.rectangle(
            [(center + hash_size // 3 - line_width // 2, center - hash_size),
             (center + hash_size // 3 + line_width // 2, center + hash_size)],
            fill=(255, 255, 255)
        )

        img.save(output_path, 'PNG')
        print(f"  Created Slack icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating Slack icon: {e}")
        return False


def create_webhook_icon(output_path: Path, size: int = 400) -> bool:
    """Create webhook/API icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Background
        margin = size // 10
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 5,
            fill=COLORS["webhook"]
        )

        # Hook shape
        center = size // 2
        hook_width = size // 6

        # Vertical line
        draw.rectangle(
            [(center - hook_width // 4, center - size // 4),
             (center + hook_width // 4, center + size // 8)],
            fill=(255, 255, 255)
        )

        # Hook curve (simplified as arc)
        draw.arc(
            [(center - hook_width, center),
             (center + hook_width, center + size // 4)],
            180, 0,
            fill=(255, 255, 255),
            width=size // 15
        )

        # Arrow
        arrow_y = center - size // 4
        draw.polygon([
            (center, arrow_y - size // 10),
            (center - size // 10, arrow_y + size // 20),
            (center + size // 10, arrow_y + size // 20),
        ], fill=(255, 255, 255))

        img.save(output_path, 'PNG')
        print(f"  Created webhook icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating webhook icon: {e}")
        return False


def create_gmail_icon(output_path: Path, size: int = 400) -> bool:
    """Create Gmail-style icon."""
    try:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Background
        margin = size // 10
        draw.rounded_rectangle(
            [(margin, margin), (size - margin, size - margin)],
            radius=size // 6,
            fill=COLORS["gmail"]
        )

        # Envelope shape
        center = size // 2
        env_w = size // 3
        env_h = size // 4

        # Envelope body
        draw.rectangle(
            [(center - env_w, center - env_h // 2),
             (center + env_w, center + env_h)],
            fill=(255, 255, 255)
        )

        # Envelope flap (triangle pointing down)
        draw.polygon([
            (center - env_w, center - env_h // 2),
            (center, center + env_h // 4),
            (center + env_w, center - env_h // 2),
        ], fill=(220, 220, 220))

        img.save(output_path, 'PNG')
        print(f"  Created Gmail icon: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating Gmail icon: {e}")
        return False


def create_architecture_diagram(output_path: Path, width: int = 1920, height: int = 1080) -> bool:
    """Create a custom architecture diagram for the workflow."""
    try:
        # Colors
        bg_color = (30, 27, 75)  # Dark purple
        accent = (139, 92, 246)  # Purple accent
        white = (255, 255, 255)
        light_gray = (200, 200, 200)

        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)

        # Title
        title_font = get_font(48, bold=True)
        title = "Client Onboarding Agent Architecture"
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_x = (width - (bbox[2] - bbox[0])) // 2
        draw.text((title_x, 40), title, fill=white, font=title_font)

        # Define nodes
        node_font = get_font(24, bold=True)
        small_font = get_font(18)

        nodes = [
            {"name": "Form\nSubmission", "x": 150, "y": 300, "color": (59, 130, 246)},
            {"name": "Webhook\nTrigger", "x": 350, "y": 300, "color": (59, 130, 246)},
            {"name": "n8n\nWorkflow", "x": 600, "y": 300, "color": (234, 76, 137)},
            {"name": "Claude\nAI", "x": 850, "y": 200, "color": (218, 119, 86)},
            {"name": "Google\nDrive", "x": 1100, "y": 150, "color": (66, 133, 244)},
            {"name": "Google\nSheets", "x": 1100, "y": 300, "color": (52, 168, 83)},
            {"name": "Google\nCalendar", "x": 1100, "y": 450, "color": (66, 133, 244)},
            {"name": "Gmail", "x": 1350, "y": 225, "color": (234, 67, 53)},
            {"name": "Slack", "x": 1350, "y": 375, "color": (74, 21, 75)},
            {"name": "Client\nReady!", "x": 1600, "y": 300, "color": (34, 197, 94)},
        ]

        node_width = 120
        node_height = 80

        # Draw connections
        connections = [
            (0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (2, 6),
            (3, 4), (3, 5), (4, 7), (5, 7), (6, 8), (7, 9), (8, 9)
        ]

        for start, end in connections:
            sx = nodes[start]["x"] + node_width // 2
            sy = nodes[start]["y"] + node_height // 2
            ex = nodes[end]["x"] + node_width // 2
            ey = nodes[end]["y"] + node_height // 2

            # Adjust for better routing
            if sx < ex:
                sx += node_width // 2 - 10
                ex -= node_width // 2 - 10

            draw.line([(sx, sy), (ex, ey)], fill=accent, width=3)

        # Draw nodes
        for node in nodes:
            x, y = node["x"], node["y"]
            color = node["color"]
            name = node["name"]

            # Shadow
            draw.rounded_rectangle(
                [(x + 4, y + 4), (x + node_width + 4, y + node_height + 4)],
                radius=10,
                fill=(20, 18, 50)
            )

            # Node
            draw.rounded_rectangle(
                [(x, y), (x + node_width, y + node_height)],
                radius=10,
                fill=color,
                outline=accent,
                width=2
            )

            # Text
            lines = name.split('\n')
            text_y = y + (node_height - len(lines) * 28) // 2
            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=node_font)
                text_x = x + (node_width - (bbox[2] - bbox[0])) // 2
                draw.text((text_x, text_y), line, fill=white, font=node_font)
                text_y += 28

        # Add legend
        legend_y = height - 100
        legend_items = [
            ("Trigger", (59, 130, 246)),
            ("Processing", (234, 76, 137)),
            ("AI", (218, 119, 86)),
            ("Google", (52, 168, 83)),
            ("Notifications", (74, 21, 75)),
        ]

        legend_x = 100
        for label, color in legend_items:
            draw.rounded_rectangle(
                [(legend_x, legend_y), (legend_x + 20, legend_y + 20)],
                radius=5,
                fill=color
            )
            draw.text((legend_x + 30, legend_y), label, fill=light_gray, font=small_font)
            legend_x += 180

        img.save(output_path)
        print(f"  Created architecture diagram: {output_path.name}")
        return True

    except Exception as e:
        print(f"  Error creating architecture diagram: {e}")
        return False


def main():
    """Download all images and create icons."""
    print("=" * 60)
    print("Downloading Slide Images")
    print("=" * 60)

    # Create directories
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ICONS_DIR.mkdir(parents=True, exist_ok=True)
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

    # Download Unsplash photos
    print("\n[1/3] Downloading photos from Unsplash...")
    for name, image_id in UNSPLASH_IMAGES.items():
        output_path = PHOTOS_DIR / f"{name}.jpg"
        if not output_path.exists():
            download_unsplash_image(image_id, output_path)
        else:
            print(f"  Skipping {name} (already exists)")

    # Create tool icons
    print("\n[2/3] Creating tool icons...")
    create_n8n_icon(ICONS_DIR / "n8n.png")
    create_claude_icon(ICONS_DIR / "claude.png")
    create_google_icon("drive", ICONS_DIR / "google_drive.png")
    create_google_icon("sheets", ICONS_DIR / "google_sheets.png")
    create_google_icon("calendar", ICONS_DIR / "google_calendar.png")
    create_gmail_icon(ICONS_DIR / "gmail.png")
    create_slack_icon(ICONS_DIR / "slack.png")
    create_webhook_icon(ICONS_DIR / "webhook.png")

    # Generic icons
    create_tool_icon("automation", COLORS["automation"], ICONS_DIR / "automation.png", icon_text="A")
    create_tool_icon("ai", COLORS["ai"], ICONS_DIR / "ai.png", icon_text="AI")

    # Create architecture diagram
    print("\n[3/3] Creating architecture diagram...")
    create_architecture_diagram(PHOTOS_DIR / "architecture_diagram.png")

    print("\n" + "=" * 60)
    print(f"Images saved to: {OUTPUT_DIR}")
    print(f"  - Icons: {len(list(ICONS_DIR.glob('*.png')))} files")
    print(f"  - Photos: {len(list(PHOTOS_DIR.glob('*')))} files")
    print("=" * 60)

    # Create index file
    index = {
        "icons": {p.stem: str(p) for p in ICONS_DIR.glob("*.png")},
        "photos": {p.stem: str(p) for p in PHOTOS_DIR.glob("*.*")},
    }

    with open(OUTPUT_DIR / "image-index.json", 'w') as f:
        json.dump(index, f, indent=2)

    print(f"Image index saved to: {OUTPUT_DIR / 'image-index.json'}")


if __name__ == "__main__":
    main()
