"""
Create professional interface mockup screenshots using PIL
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Output directory
OUTPUT_DIR = "C:/Users/Jakeb/support-forge/server/scripts/output/slide-images/screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Resolution
WIDTH = 1920
HEIGHT = 1080

# Try to load fonts
def get_font(size, bold=False):
    """Get a font, falling back to default if necessary"""
    font_paths = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    return ImageFont.load_default()

def get_mono_font(size):
    """Get a monospace font"""
    mono_paths = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    for path in mono_paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    return ImageFont.load_default()


def draw_rounded_rect(draw, coords, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = coords

    # Ensure radius isn't too large for the rectangle
    rect_width = x2 - x1
    rect_height = y2 - y1
    radius = min(radius, rect_width // 2, rect_height // 2)

    if radius <= 0:
        # Just draw a regular rectangle
        if fill:
            draw.rectangle([x1, y1, x2, y2], fill=fill)
        if outline:
            draw.rectangle([x1, y1, x2, y2], outline=outline, width=width)
        return

    if fill:
        # Draw the main rectangle body
        if x1 + radius < x2 - radius:
            draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

        # Draw corners
        draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill)
        draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill)
        draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill)
        draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill)

    if outline:
        # Draw outline arcs and lines
        draw.arc([x1, y1, x1 + 2*radius, y1 + 2*radius], 180, 270, fill=outline, width=width)
        draw.arc([x2 - 2*radius, y1, x2, y1 + 2*radius], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2 - 2*radius, x1 + 2*radius, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2 - 2*radius, y2 - 2*radius, x2, y2], 0, 90, fill=outline, width=width)

        if x1 + radius < x2 - radius:
            draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline, width=width)
            draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline, width=width)
        draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline, width=width)
        draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline, width=width)


def create_n8n_canvas():
    """Create n8n workflow canvas screenshot"""
    img = Image.new('RGB', (WIDTH, HEIGHT), '#1a1a2e')
    draw = ImageDraw.Draw(img)

    font_large = get_font(24, bold=True)
    font_medium = get_font(18)
    font_small = get_font(14)

    # Left sidebar
    sidebar_width = 280
    draw.rectangle([0, 0, sidebar_width, HEIGHT], fill='#16213e')

    # Sidebar header
    draw.rectangle([0, 0, sidebar_width, 60], fill='#0f3460')
    draw.text((20, 18), "n8n", font=font_large, fill='#ff6b35')
    draw.text((70, 20), "Workflow Automation", font=font_small, fill='#a0a0a0')

    # Search box
    draw_rounded_rect(draw, [15, 80, sidebar_width - 15, 115], 8, fill='#1a1a2e')
    draw.text((25, 88), "Search nodes...", font=font_small, fill='#666666')

    # Node categories
    categories = [
        ("Triggers", "#ff6b35", ["Webhook", "Schedule", "Manual"]),
        ("Actions", "#4ecdc4", ["HTTP Request", "Code", "Set"]),
        ("Flow", "#a855f7", ["IF", "Switch", "Merge"]),
        ("Data", "#3b82f6", ["Google Sheets", "MySQL", "MongoDB"]),
    ]

    y_pos = 140
    for cat_name, color, items in categories:
        draw.text((20, y_pos), cat_name, font=font_medium, fill=color)
        y_pos += 35
        for item in items:
            draw_rounded_rect(draw, [25, y_pos, sidebar_width - 25, y_pos + 32], 6, fill='#1a1a2e')
            draw.ellipse([35, y_pos + 8, 51, y_pos + 24], fill=color)
            draw.text((60, y_pos + 6), item, font=font_small, fill='#ffffff')
            y_pos += 42
        y_pos += 15

    # Top toolbar
    toolbar_height = 56
    draw.rectangle([sidebar_width, 0, WIDTH, toolbar_height], fill='#0f3460')

    # Toolbar buttons
    buttons = [
        ("Play", "#22c55e", sidebar_width + 20),
        ("Save", "#3b82f6", sidebar_width + 100),
        ("Settings", "#6b7280", sidebar_width + 180),
    ]
    for btn_text, btn_color, btn_x in buttons:
        draw_rounded_rect(draw, [btn_x, 12, btn_x + 70, 44], 6, fill=btn_color)
        draw.text((btn_x + 15, 18), btn_text, font=font_small, fill='#ffffff')

    # Workflow name
    draw.text((WIDTH - 300, 18), "Customer Onboarding", font=font_medium, fill='#ffffff')

    # Canvas grid (subtle)
    canvas_start = sidebar_width
    for x in range(canvas_start, WIDTH, 40):
        draw.line([(x, toolbar_height), (x, HEIGHT)], fill='#252550', width=1)
    for y in range(toolbar_height, HEIGHT, 40):
        draw.line([(canvas_start, y), (WIDTH, y)], fill='#252550', width=1)

    # Workflow nodes
    nodes = [
        ("Webhook", 450, 300, "#ff6b35", "When called"),
        ("HTTP Request", 700, 300, "#4ecdc4", "Fetch user data"),
        ("IF", 950, 300, "#a855f7", "Check status"),
        ("Google Sheets", 1200, 200, "#34a853", "Add to success"),
        ("Google Sheets", 1200, 400, "#ea4335", "Add to failed"),
    ]

    node_width = 180
    node_height = 80

    # Draw connection lines first
    line_color = '#4ecdc4'
    # Webhook to HTTP
    draw.line([(450 + node_width, 300 + node_height//2), (700, 300 + node_height//2)], fill=line_color, width=3)
    # HTTP to IF
    draw.line([(700 + node_width, 300 + node_height//2), (950, 300 + node_height//2)], fill=line_color, width=3)
    # IF to top sheet
    draw.line([(950 + node_width, 300 + 20), (1100, 200 + node_height//2)], fill='#22c55e', width=3)
    draw.line([(1100, 200 + node_height//2), (1200, 200 + node_height//2)], fill='#22c55e', width=3)
    # IF to bottom sheet
    draw.line([(950 + node_width, 300 + node_height - 20), (1100, 400 + node_height//2)], fill='#ef4444', width=3)
    draw.line([(1100, 400 + node_height//2), (1200, 400 + node_height//2)], fill='#ef4444', width=3)

    # Draw nodes
    for name, x, y, color, subtitle in nodes:
        # Node shadow
        draw_rounded_rect(draw, [x + 4, y + 4, x + node_width + 4, y + node_height + 4], 12, fill='#0a0a15')
        # Node body
        draw_rounded_rect(draw, [x, y, x + node_width, y + node_height], 12, fill='#262650')
        # Color bar on left
        draw_rounded_rect(draw, [x, y, x + 8, y + node_height], 12, fill=color)
        draw.rectangle([x + 4, y, x + 8, y + node_height], fill=color)
        # Node text
        draw.text((x + 20, y + 15), name, font=font_medium, fill='#ffffff')
        draw.text((x + 20, y + 45), subtitle, font=font_small, fill='#888888')
        # Connection dots
        draw.ellipse([x - 8, y + node_height//2 - 8, x + 8, y + node_height//2 + 8], fill='#4ecdc4', outline='#1a1a2e', width=2)
        draw.ellipse([x + node_width - 8, y + node_height//2 - 8, x + node_width + 8, y + node_height//2 + 8], fill='#4ecdc4', outline='#1a1a2e', width=2)

    # Status bar
    draw.rectangle([sidebar_width, HEIGHT - 40, WIDTH, HEIGHT], fill='#0f3460')
    draw.text((sidebar_width + 20, HEIGHT - 30), "Workflow saved", font=font_small, fill='#22c55e')
    draw.text((WIDTH - 200, HEIGHT - 30), "Last run: 2 min ago", font=font_small, fill='#888888')

    img.save(os.path.join(OUTPUT_DIR, "n8n_canvas.png"), quality=95)
    print("Created n8n_canvas.png")


def create_claude_chat():
    """Create Claude chat interface screenshot"""
    img = Image.new('RGB', (WIDTH, HEIGHT), '#faf9f6')
    draw = ImageDraw.Draw(img)

    font_large = get_font(28, bold=True)
    font_medium = get_font(18)
    font_small = get_font(14)
    font_code = get_mono_font(14)

    # Left sidebar
    sidebar_width = 300
    draw.rectangle([0, 0, sidebar_width, HEIGHT], fill='#f5f4f0')

    # Sidebar header
    draw.rectangle([0, 0, sidebar_width, 70], fill='#d97706')
    draw.text((20, 22), "Claude", font=font_large, fill='#ffffff')

    # New chat button
    draw_rounded_rect(draw, [20, 90, sidebar_width - 20, 130], 8, fill='#d97706')
    draw.text((sidebar_width // 2 - 40, 100), "New Chat", font=font_medium, fill='#ffffff')

    # Chat history
    chats = [
        ("Automation workflow help", "Today"),
        ("API integration question", "Today"),
        ("Python script review", "Yesterday"),
        ("Database design", "Yesterday"),
        ("AWS deployment", "Dec 15"),
    ]

    y_pos = 160
    for i, (title, date) in enumerate(chats):
        bg_color = '#ebe9e4' if i == 0 else '#f5f4f0'
        draw_rounded_rect(draw, [15, y_pos, sidebar_width - 15, y_pos + 60], 8, fill=bg_color)
        draw.text((25, y_pos + 10), title, font=font_small, fill='#1f1f1f')
        draw.text((25, y_pos + 32), date, font=font_small, fill='#888888')
        y_pos += 70

    # Main chat area
    chat_area_start = sidebar_width

    # Header
    draw.rectangle([chat_area_start, 0, WIDTH, 70], fill='#ffffff')
    draw.line([(chat_area_start, 70), (WIDTH, 70)], fill='#e5e5e5', width=1)
    draw.text((chat_area_start + 30, 22), "Claude 3.5 Sonnet", font=font_medium, fill='#1f1f1f')

    # Chat messages
    messages = [
        ("user", "Help me create an automation workflow that monitors a Google Sheet and sends Slack notifications when new rows are added."),
        ("claude", None),  # Special handling for Claude response with code
    ]

    y_pos = 120
    max_width = WIDTH - sidebar_width - 120

    # User message
    user_msg = messages[0][1]
    draw_rounded_rect(draw, [WIDTH - 500, y_pos, WIDTH - 60, y_pos + 80], 16, fill='#d97706')
    # Wrap text manually
    draw.text((WIDTH - 480, y_pos + 15), "Help me create an automation workflow", font=font_medium, fill='#ffffff')
    draw.text((WIDTH - 480, y_pos + 40), "that monitors a Google Sheet and sends", font=font_medium, fill='#ffffff')
    draw.text((WIDTH - 480, y_pos + 60), "Slack notifications when new rows are added.", font=font_small, fill='#ffffff')

    y_pos += 120

    # Claude avatar
    draw.ellipse([chat_area_start + 30, y_pos, chat_area_start + 70, y_pos + 40], fill='#d97706')
    draw.text((chat_area_start + 42, y_pos + 8), "C", font=font_medium, fill='#ffffff')

    # Claude response
    claude_y = y_pos + 10
    draw.text((chat_area_start + 90, claude_y), "I'll help you create that automation workflow! Here's how to set it up:", font=font_medium, fill='#1f1f1f')
    claude_y += 40

    # Steps
    steps = [
        "1. Set up a Google Sheets trigger to watch for new rows",
        "2. Configure a Slack action to send formatted messages",
        "3. Map the spreadsheet columns to your notification template",
    ]
    for step in steps:
        draw.text((chat_area_start + 90, claude_y), step, font=font_small, fill='#444444')
        claude_y += 28

    claude_y += 20
    draw.text((chat_area_start + 90, claude_y), "Here's a sample n8n workflow configuration:", font=font_medium, fill='#1f1f1f')
    claude_y += 35

    # Code block
    code_lines = [
        '{',
        '  "name": "Sheet to Slack Notifier",',
        '  "nodes": [',
        '    {',
        '      "name": "Google Sheets Trigger",',
        '      "type": "googleSheetsTrigger",',
        '      "parameters": {',
        '        "pollInterval": 1,',
        '        "sheetId": "your-sheet-id"',
        '      }',
        '    },',
        '    {',
        '      "name": "Slack",',
        '      "type": "slack",',
        '      "parameters": {',
        '        "channel": "#notifications"',
        '      }',
        '    }',
        '  ]',
        '}',
    ]

    code_block_height = len(code_lines) * 22 + 30
    draw_rounded_rect(draw, [chat_area_start + 90, claude_y, WIDTH - 100, claude_y + code_block_height], 12, fill='#1e1e1e')

    code_y = claude_y + 15
    for line in code_lines:
        draw.text((chat_area_start + 110, code_y), line, font=font_code, fill='#d4d4d4')
        code_y += 22

    # Input box at bottom
    input_y = HEIGHT - 100
    draw_rounded_rect(draw, [chat_area_start + 40, input_y, WIDTH - 40, input_y + 60], 12, fill='#ffffff', outline='#d1d1d1', width=2)
    draw.text((chat_area_start + 60, input_y + 18), "Message Claude...", font=font_medium, fill='#999999')

    # Send button
    draw_rounded_rect(draw, [WIDTH - 100, input_y + 10, WIDTH - 55, input_y + 50], 8, fill='#d97706')
    draw.polygon([(WIDTH - 85, input_y + 20), (WIDTH - 85, input_y + 40), (WIDTH - 65, input_y + 30)], fill='#ffffff')

    img.save(os.path.join(OUTPUT_DIR, "claude_chat.png"), quality=95)
    print("Created claude_chat.png")


def create_zapier_editor():
    """Create Zapier editor screenshot"""
    img = Image.new('RGB', (WIDTH, HEIGHT), '#ffffff')
    draw = ImageDraw.Draw(img)

    font_large = get_font(32, bold=True)
    font_medium = get_font(20)
    font_small = get_font(16)

    # Top navigation
    nav_height = 70
    draw.rectangle([0, 0, WIDTH, nav_height], fill='#ff4a00')
    draw.text((30, 20), "zapier", font=font_large, fill='#ffffff')

    # Nav items
    nav_items = ["Home", "Zaps", "Apps", "Templates"]
    x_pos = 200
    for item in nav_items:
        draw.text((x_pos, 24), item, font=font_medium, fill='#ffffff')
        x_pos += 120

    # Create button
    draw_rounded_rect(draw, [WIDTH - 180, 15, WIDTH - 30, 55], 8, fill='#ffffff')
    draw.text((WIDTH - 150, 23), "Create Zap", font=font_medium, fill='#ff4a00')

    # Breadcrumb area
    draw.rectangle([0, nav_height, WIDTH, nav_height + 50], fill='#f5f5f5')
    draw.text((30, nav_height + 12), "My Zaps  >  New Customer Notification", font=font_small, fill='#666666')

    # Main content area
    content_start = nav_height + 50

    # Zap title
    draw.text((WIDTH // 2 - 200, content_start + 30), "New Customer Notification", font=font_large, fill='#2d2e2e')

    # Trigger block
    trigger_y = content_start + 100
    block_width = 500
    block_height = 180
    trigger_x = WIDTH // 2 - block_width // 2

    # Trigger container
    draw_rounded_rect(draw, [trigger_x, trigger_y, trigger_x + block_width, trigger_y + block_height], 16, fill='#fff8f5', outline='#ff4a00', width=3)

    # Trigger header
    draw.rectangle([trigger_x, trigger_y, trigger_x + block_width, trigger_y + 50], fill='#ff4a00')
    draw_rounded_rect(draw, [trigger_x, trigger_y, trigger_x + block_width, trigger_y + 30], 16, fill='#ff4a00')
    draw.text((trigger_x + 20, trigger_y + 12), "1. Trigger", font=font_medium, fill='#ffffff')
    draw.text((trigger_x + 150, trigger_y + 14), "When this happens...", font=font_small, fill='#ffccbb')

    # Google Sheets icon placeholder
    draw_rounded_rect(draw, [trigger_x + 30, trigger_y + 70, trigger_x + 90, trigger_y + 130], 12, fill='#34a853')
    draw.text((trigger_x + 45, trigger_y + 90), "G", font=font_large, fill='#ffffff')

    # Trigger details
    draw.text((trigger_x + 110, trigger_y + 75), "Google Sheets", font=font_medium, fill='#2d2e2e')
    draw.text((trigger_x + 110, trigger_y + 105), "New Spreadsheet Row", font=font_small, fill='#666666')
    draw.text((trigger_x + 110, trigger_y + 130), "Customer Signups Sheet", font=font_small, fill='#999999')

    # Connection line
    line_x = WIDTH // 2
    draw.line([(line_x, trigger_y + block_height), (line_x, trigger_y + block_height + 60)], fill='#ff4a00', width=4)
    # Arrow
    draw.polygon([(line_x - 12, trigger_y + block_height + 45), (line_x + 12, trigger_y + block_height + 45), (line_x, trigger_y + block_height + 65)], fill='#ff4a00')

    # Add step circle
    circle_y = trigger_y + block_height + 30
    draw.ellipse([line_x - 20, circle_y - 5, line_x + 20, circle_y + 35], fill='#ffffff', outline='#ff4a00', width=2)
    draw.text((line_x - 7, circle_y + 3), "+", font=font_medium, fill='#ff4a00')

    # Action block
    action_y = trigger_y + block_height + 80

    # Action container
    draw_rounded_rect(draw, [trigger_x, action_y, trigger_x + block_width, action_y + block_height], 16, fill='#f0f9ff', outline='#3b82f6', width=3)

    # Action header
    draw.rectangle([trigger_x, action_y, trigger_x + block_width, action_y + 50], fill='#3b82f6')
    draw_rounded_rect(draw, [trigger_x, action_y, trigger_x + block_width, action_y + 30], 16, fill='#3b82f6')
    draw.text((trigger_x + 20, action_y + 12), "2. Action", font=font_medium, fill='#ffffff')
    draw.text((trigger_x + 150, action_y + 14), "Then do this...", font=font_small, fill='#bfdbfe')

    # Slack icon placeholder
    draw_rounded_rect(draw, [trigger_x + 30, action_y + 70, trigger_x + 90, action_y + 130], 12, fill='#4a154b')
    draw.text((trigger_x + 45, action_y + 90), "S", font=font_large, fill='#ffffff')

    # Action details
    draw.text((trigger_x + 110, action_y + 75), "Slack", font=font_medium, fill='#2d2e2e')
    draw.text((trigger_x + 110, action_y + 105), "Send Channel Message", font=font_small, fill='#666666')
    draw.text((trigger_x + 110, action_y + 130), "#new-customers", font=font_small, fill='#999999')

    # Publish button
    publish_y = action_y + block_height + 40
    draw_rounded_rect(draw, [WIDTH // 2 - 80, publish_y, WIDTH // 2 + 80, publish_y + 50], 8, fill='#ff4a00')
    draw.text((WIDTH // 2 - 40, publish_y + 12), "Publish", font=font_medium, fill='#ffffff')

    # Side panel hint
    draw.rectangle([WIDTH - 350, content_start, WIDTH, HEIGHT], fill='#fafafa')
    draw.line([(WIDTH - 350, content_start), (WIDTH - 350, HEIGHT)], fill='#e5e5e5', width=1)
    draw.text((WIDTH - 330, content_start + 20), "Setup", font=font_medium, fill='#2d2e2e')

    setup_items = ["Trigger configured", "Action configured", "Test your Zap", "Turn on Zap"]
    setup_y = content_start + 60
    for i, item in enumerate(setup_items):
        check_color = '#22c55e' if i < 2 else '#d1d5db'
        draw.ellipse([WIDTH - 330, setup_y, WIDTH - 310, setup_y + 20], fill=check_color)
        if i < 2:
            draw.text((WIDTH - 325, setup_y + 2), "✓", font=font_small, fill='#ffffff')
        draw.text((WIDTH - 295, setup_y), item, font=font_small, fill='#666666')
        setup_y += 40

    img.save(os.path.join(OUTPUT_DIR, "zapier_editor.png"), quality=95)
    print("Created zapier_editor.png")


def create_aws_console():
    """Create AWS Console screenshot"""
    img = Image.new('RGB', (WIDTH, HEIGHT), '#f5f5f5')
    draw = ImageDraw.Draw(img)

    font_large = get_font(28, bold=True)
    font_medium = get_font(18)
    font_small = get_font(14)

    # Top navigation bar
    nav_height = 50
    draw.rectangle([0, 0, WIDTH, nav_height], fill='#232f3e')

    # AWS Logo
    draw_rounded_rect(draw, [15, 10, 90, 40], 4, fill='#ff9900')
    draw.text((25, 14), "aws", font=font_medium, fill='#232f3e')

    # Nav items
    draw.text((120, 15), "Services", font=font_small, fill='#ffffff')
    draw.text((200, 15), "Search", font=font_small, fill='#aaaaaa')
    draw_rounded_rect(draw, [260, 8, 600, 42], 4, fill='#1a2634')
    draw.text((280, 15), "Search for services, features, and more...", font=font_small, fill='#666666')

    # Right side nav
    draw.text((WIDTH - 300, 15), "us-east-1", font=font_small, fill='#ffffff')
    draw.text((WIDTH - 180, 15), "jakeb@example.com", font=font_small, fill='#ffffff')

    # Secondary nav
    secondary_nav_y = nav_height
    draw.rectangle([0, secondary_nav_y, WIDTH, secondary_nav_y + 45], fill='#37475a')
    draw.text((30, secondary_nav_y + 12), "AWS Management Console", font=font_medium, fill='#ffffff')

    # Breadcrumb
    draw.text((WIDTH - 400, secondary_nav_y + 14), "Console Home > Services", font=font_small, fill='#aaaaaa')

    # Main content
    content_y = secondary_nav_y + 45 + 20

    # Welcome section
    draw_rounded_rect(draw, [30, content_y, WIDTH - 30, content_y + 120], 8, fill='#ffffff')
    draw.text((50, content_y + 20), "Welcome to AWS Console", font=font_large, fill='#16191f')
    draw.text((50, content_y + 60), "Build, deploy, and manage applications on AWS cloud infrastructure", font=font_medium, fill='#545b64')
    draw.text((50, content_y + 90), "Get started with our most popular services below", font=font_small, fill='#879596')

    content_y += 140

    # Recently visited section
    draw.text((30, content_y), "Recently Visited Services", font=font_medium, fill='#16191f')
    content_y += 40

    # Service cards
    services = [
        ("AWS Amplify", "Build and deploy full-stack apps", "#ff9900", "5 apps deployed"),
        ("Amazon S3", "Object storage built to retrieve data", "#569a31", "12 buckets"),
        ("CloudFront", "Fast, secure content delivery", "#8c4fff", "8 distributions"),
        ("Route 53", "Scalable domain name system", "#8c4fff", "15 hosted zones"),
        ("Lambda", "Run code without servers", "#ff9900", "23 functions"),
        ("DynamoDB", "Fast, flexible NoSQL database", "#3b48cc", "6 tables"),
    ]

    card_width = (WIDTH - 90) // 3
    card_height = 160

    for i, (name, desc, color, stat) in enumerate(services):
        row = i // 3
        col = i % 3
        card_x = 30 + col * (card_width + 15)
        card_y = content_y + row * (card_height + 15)

        # Card background
        draw_rounded_rect(draw, [card_x, card_y, card_x + card_width, card_y + card_height], 8, fill='#ffffff')

        # Color accent bar
        draw.rectangle([card_x, card_y, card_x + 6, card_y + card_height], fill=color)
        draw_rounded_rect(draw, [card_x, card_y, card_x + 8, card_y + 20], 8, fill=color)
        draw_rounded_rect(draw, [card_x, card_y + card_height - 20, card_x + 8, card_y + card_height], 8, fill=color)

        # Service icon placeholder
        draw_rounded_rect(draw, [card_x + 25, card_y + 20, card_x + 65, card_y + 60], 8, fill=color)
        draw.text((card_x + 35, card_y + 28), name[0], font=font_medium, fill='#ffffff')

        # Service name and description
        draw.text((card_x + 80, card_y + 25), name, font=font_medium, fill='#16191f')

        # Wrap description
        draw.text((card_x + 25, card_y + 75), desc[:35], font=font_small, fill='#545b64')
        if len(desc) > 35:
            draw.text((card_x + 25, card_y + 95), desc[35:], font=font_small, fill='#545b64')

        # Stats
        draw.text((card_x + 25, card_y + 125), stat, font=font_small, fill=color)

    content_y += 2 * (card_height + 15) + 30

    # Quick actions section
    draw.text((30, content_y), "Quick Actions", font=font_medium, fill='#16191f')
    content_y += 40

    actions = [
        ("Launch EC2 Instance", "#ff9900"),
        ("Create S3 Bucket", "#569a31"),
        ("Deploy Amplify App", "#ff9900"),
        ("Configure CloudFront", "#8c4fff"),
    ]

    action_x = 30
    for action, color in actions:
        action_width = 230
        draw_rounded_rect(draw, [action_x, content_y, action_x + action_width, content_y + 45], 6, fill='#ffffff', outline=color, width=2)
        draw.text((action_x + 15, content_y + 12), action, font=font_small, fill=color)
        action_x += action_width + 15

    # Footer
    draw.rectangle([0, HEIGHT - 40, WIDTH, HEIGHT], fill='#232f3e')
    draw.text((30, HEIGHT - 28), "2024 Amazon Web Services, Inc.", font=font_small, fill='#aaaaaa')
    draw.text((WIDTH - 200, HEIGHT - 28), "Privacy | Terms | Feedback", font=font_small, fill='#aaaaaa')

    img.save(os.path.join(OUTPUT_DIR, "aws_console.png"), quality=95)
    print("Created aws_console.png")


if __name__ == "__main__":
    print("Creating interface mockup screenshots...")
    print(f"Output directory: {OUTPUT_DIR}")
    print("-" * 50)

    create_n8n_canvas()
    create_claude_chat()
    create_zapier_editor()
    create_aws_console()

    print("-" * 50)
    print("All mockups created successfully!")
