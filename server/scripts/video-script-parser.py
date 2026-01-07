#!/usr/bin/env python3
"""
Video Script Parser for AI Launchpad Academy

Parses video script markdown files and extracts:
- Visual cues [SCREEN: description]
- Spoken text between cues
- Estimated timestamps based on word count (150 wpm)
- Asset requirements categorization

Usage:
    python video-script-parser.py --script script-0.1-welcome.md
    python video-script-parser.py --all
    python video-script-parser.py --all --output ./parsed-scripts/
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional


# Configuration
WORDS_PER_MINUTE = 150
DEFAULT_SCRIPTS_DIR = Path(r"C:\Users\Jakeb\support-forge\docs\academy-content\video-scripts")
DEFAULT_OUTPUT_DIR = Path(r"C:\Users\Jakeb\support-forge\server\scripts\output\parsed-scripts")

# Visual type classification patterns
VISUAL_TYPE_PATTERNS = {
    "animated_title": [
        r"logo\s*animation", r"title\s*card", r"animated\s*title", r"lesson\s*title",
        r"module\s*\d+", r"phase.*title", r"branding", r"fade\s*to", r"intro",
        r"opening\s*animation", r"course\s*title", r"academy\s*logo"
    ],
    "comparison_table": [
        r"comparison\s*table", r"table\s*building", r"side\s*by\s*side.*(?:logo|platform)",
        r"versus", r"vs\.?\s", r"compare", r"comparing", r"comparison"
    ],
    "flowchart": [
        r"flowchart", r"diagram", r"decision\s*tree", r"workflow\s*diagram",
        r"decision\s*framework", r"process\s*flow", r"decision\s*flowchart"
    ],
    "screen_capture": [
        r"terminal", r"browser", r"console", r"command", r"powershell",
        r"ubuntu", r"code\s*editor", r"ide", r"interface", r"dashboard",
        r"settings", r"menu", r"window", r"application", r"app\s*screen",
        r"screenshot", r"login", r"install", r"npm", r"prompt"
    ],
    "text_overlay": [
        r"text\s*overlay", r"bullet\s*point", r"heading", r"quote",
        r"question\s*\d+", r"highlight", r"callout", r"tip\s*box",
        r"warning", r"note", r"step\s*\d+", r"summary", r"takeaway",
        r"key\s*point", r"checklist", r"prerequisite", r"requirement"
    ],
    "illustration": [
        r"icon", r"graphic", r"illustration", r"visual", r"image",
        r"checkmark", r"crossed.?out", r"penguin", r"logo\b(?!.*animation)",
        r"symbol", r"badge", r"certificate"
    ],
    "calculator": [
        r"calculator", r"interactive", r"formula", r"calculation",
        r"roi\s*visual", r"number", r"math", r"compute"
    ],
    "split_view": [
        r"split\s*view", r"side.by.side", r"left\s*side.*right\s*side",
        r"before.*after", r"two\s*column", r"dual\s*view"
    ],
}


@dataclass
class Segment:
    """Represents a single segment of video content."""
    segment_id: int
    start_time: float
    end_time: float
    visual_cue: str
    visual_type: str
    spoken_text: str
    word_count: int


@dataclass
class Asset:
    """Represents an asset needed for video production."""
    type: str
    description: str
    segment_ids: list = field(default_factory=list)


@dataclass
class ParsedScript:
    """Represents a fully parsed video script."""
    script_id: str
    title: str
    total_duration_seconds: float
    segments: list = field(default_factory=list)
    assets_needed: list = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


def classify_visual_type(visual_cue: str) -> str:
    """
    Classify the visual cue into a predefined category.

    Args:
        visual_cue: The visual cue description text

    Returns:
        The classified visual type
    """
    cue_lower = visual_cue.lower()

    # Check each category's patterns
    for visual_type, patterns in VISUAL_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, cue_lower):
                return visual_type

    # Default fallback
    return "text_overlay"


def count_words(text: str) -> int:
    """
    Count words in text, excluding markdown and stage directions.

    Args:
        text: The text to count words in

    Returns:
        Word count
    """
    # Remove markdown formatting
    clean_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold
    clean_text = re.sub(r'\*([^*]+)\*', r'\1', clean_text)  # Italic
    clean_text = re.sub(r'`([^`]+)`', r'\1', clean_text)  # Code

    # Remove [PAUSE] markers
    clean_text = re.sub(r'\[PAUSE\]', '', clean_text, flags=re.IGNORECASE)

    # Remove any remaining brackets content that might be stage directions
    clean_text = re.sub(r'\[[^\]]+\]', '', clean_text)

    # Count words
    words = clean_text.split()
    return len(words)


def calculate_duration(word_count: int, wpm: int = WORDS_PER_MINUTE) -> float:
    """
    Calculate duration in seconds based on word count.

    Args:
        word_count: Number of words
        wpm: Words per minute speaking rate

    Returns:
        Duration in seconds
    """
    return (word_count / wpm) * 60


def extract_title_from_content(content: str, filename: str) -> str:
    """
    Extract the title from the script content.

    Args:
        content: The markdown content
        filename: The script filename as fallback

    Returns:
        The extracted title
    """
    # Try to find H1 heading
    h1_match = re.search(r'^#\s+(?:Script\s+[\d.]+:\s*)?(.+)$', content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
        # Clean up any remaining script numbering
        title = re.sub(r'^[\d.]+\s*[-:]\s*', '', title)
        return title

    # Fallback to filename
    base_name = Path(filename).stem
    # Convert filename to title case
    title = base_name.replace('-', ' ').replace('_', ' ')
    return title.title()


def extract_script_id(filename: str) -> str:
    """
    Extract a clean script ID from the filename.

    Args:
        filename: The script filename

    Returns:
        The script ID
    """
    stem = Path(filename).stem
    # Clean up the stem for use as ID
    script_id = stem.lower().replace(' ', '-').replace('_', '-')
    return script_id


def extract_metadata(content: str) -> dict:
    """
    Extract metadata from the script header.

    Args:
        content: The markdown content

    Returns:
        Dictionary of metadata
    """
    metadata = {}

    # Duration
    duration_match = re.search(r'\*\*Duration:\*\*\s*(.+?)(?:\n|$)', content)
    if duration_match:
        metadata['stated_duration'] = duration_match.group(1).strip()

    # Lesson info
    lesson_match = re.search(r'\*\*Lesson:\*\*\s*(.+?)(?:\n|$)', content)
    if lesson_match:
        metadata['lesson'] = lesson_match.group(1).strip()

    # Purpose
    purpose_match = re.search(r'\*\*Purpose:\*\*\s*(.+?)(?:\n|$)', content)
    if purpose_match:
        metadata['purpose'] = purpose_match.group(1).strip()

    # Word count from footer
    word_count_match = re.search(r'\*Approximate word count:\s*([\d,]+)', content)
    if word_count_match:
        metadata['stated_word_count'] = word_count_match.group(1).strip()

    # Runtime estimate from footer
    runtime_match = re.search(r'\*Estimated runtime:\s*(.+?)\*', content)
    if runtime_match:
        metadata['stated_runtime'] = runtime_match.group(1).strip()

    return metadata


def parse_script(content: str, filename: str) -> ParsedScript:
    """
    Parse a video script markdown file into structured data.

    Args:
        content: The markdown content
        filename: The script filename

    Returns:
        ParsedScript object with all extracted data
    """
    script_id = extract_script_id(filename)
    title = extract_title_from_content(content, filename)
    metadata = extract_metadata(content)

    # Pattern to match [SCREEN: ...] visual cues
    screen_pattern = r'\[SCREEN:\s*(.+?)\]'

    # Find all visual cues and their positions
    cue_matches = list(re.finditer(screen_pattern, content, re.IGNORECASE | re.DOTALL))

    segments = []
    assets_by_type = {}  # Track assets for deduplication
    current_time = 0.0

    for i, match in enumerate(cue_matches):
        visual_cue = match.group(1).strip()
        visual_cue = re.sub(r'\s+', ' ', visual_cue)  # Normalize whitespace

        # Determine spoken text boundaries
        cue_end = match.end()

        if i + 1 < len(cue_matches):
            # Text until next cue
            next_cue_start = cue_matches[i + 1].start()
            spoken_text = content[cue_end:next_cue_start]
        else:
            # Text until end of content (before footer markers)
            remaining = content[cue_end:]
            # Find end markers
            end_markers = [
                remaining.find('---\n\n**END OF SCRIPT'),
                remaining.find('**END OF SCRIPT'),
                remaining.find('\n---\n\n*Approximate'),
                remaining.find('\n*Approximate word count'),
            ]
            valid_markers = [m for m in end_markers if m != -1]
            if valid_markers:
                spoken_text = remaining[:min(valid_markers)]
            else:
                spoken_text = remaining

        # Clean up spoken text
        spoken_text = spoken_text.strip()
        # Remove section headers (## HEADING)
        spoken_text = re.sub(r'^##\s+.+$', '', spoken_text, flags=re.MULTILINE)
        # Remove horizontal rules
        spoken_text = re.sub(r'^---+$', '', spoken_text, flags=re.MULTILINE)
        # Remove [PAUSE] for word counting but keep for reference
        spoken_text_for_count = re.sub(r'\[PAUSE\]', '', spoken_text, flags=re.IGNORECASE)
        # Normalize whitespace
        spoken_text = re.sub(r'\n{3,}', '\n\n', spoken_text).strip()
        spoken_text_for_count = spoken_text_for_count.strip()

        # Calculate timing
        word_count = count_words(spoken_text_for_count)
        # Add pause time (assume 1.5 seconds per [PAUSE])
        pause_count = len(re.findall(r'\[PAUSE\]', spoken_text, re.IGNORECASE))
        pause_time = pause_count * 1.5

        segment_duration = calculate_duration(word_count) + pause_time

        # Ensure minimum segment duration
        if segment_duration < 2:
            segment_duration = 2

        start_time = current_time
        end_time = current_time + segment_duration

        # Classify visual type
        visual_type = classify_visual_type(visual_cue)

        segment = Segment(
            segment_id=i + 1,
            start_time=round(start_time, 1),
            end_time=round(end_time, 1),
            visual_cue=visual_cue,
            visual_type=visual_type,
            spoken_text=spoken_text,
            word_count=word_count
        )
        segments.append(segment)

        # Track assets
        # Create a short description for the asset
        short_desc = visual_cue[:80] + "..." if len(visual_cue) > 80 else visual_cue
        asset_key = f"{visual_type}:{short_desc}"

        if asset_key not in assets_by_type:
            assets_by_type[asset_key] = Asset(
                type=visual_type,
                description=short_desc,
                segment_ids=[]
            )
        assets_by_type[asset_key].segment_ids.append(i + 1)

        current_time = end_time

    # Convert assets dict to list
    assets_needed = list(assets_by_type.values())

    # Sort assets by type for cleaner output
    assets_needed.sort(key=lambda a: (a.type, a.description))

    return ParsedScript(
        script_id=script_id,
        title=title,
        total_duration_seconds=round(current_time, 1),
        segments=segments,
        assets_needed=assets_needed,
        metadata=metadata
    )


def script_to_dict(parsed_script: ParsedScript) -> dict:
    """
    Convert ParsedScript to a JSON-serializable dictionary.

    Args:
        parsed_script: The parsed script object

    Returns:
        Dictionary representation
    """
    return {
        "script_id": parsed_script.script_id,
        "title": parsed_script.title,
        "total_duration_seconds": parsed_script.total_duration_seconds,
        "segments": [
            {
                "segment_id": s.segment_id,
                "start_time": s.start_time,
                "end_time": s.end_time,
                "visual_cue": s.visual_cue,
                "visual_type": s.visual_type,
                "spoken_text": s.spoken_text,
                "word_count": s.word_count
            }
            for s in parsed_script.segments
        ],
        "assets_needed": [
            {
                "type": a.type,
                "description": a.description,
                "segment_ids": a.segment_ids
            }
            for a in parsed_script.assets_needed
        ],
        "metadata": parsed_script.metadata,
        "parsed_at": datetime.now().isoformat()
    }


def parse_single_script(script_path: Path, output_dir: Optional[Path] = None) -> dict:
    """
    Parse a single script file and optionally save to output directory.

    Args:
        script_path: Path to the script file
        output_dir: Optional output directory for JSON file

    Returns:
        Parsed script as dictionary
    """
    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    print(f"Parsing: {script_path.name}")

    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parsed = parse_script(content, script_path.name)
    result = script_to_dict(parsed)

    # Print summary
    print(f"  Title: {result['title']}")
    print(f"  Segments: {len(result['segments'])}")
    print(f"  Duration: {result['total_duration_seconds']:.1f}s ({result['total_duration_seconds']/60:.1f} min)")
    print(f"  Assets needed: {len(result['assets_needed'])}")

    # Save if output directory specified
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{parsed.script_id}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"  Saved to: {output_file}")

    return result


def parse_all_scripts(scripts_dir: Path, output_dir: Optional[Path] = None) -> list:
    """
    Parse all script files in a directory.

    Args:
        scripts_dir: Directory containing script files
        output_dir: Optional output directory for JSON files

    Returns:
        List of parsed scripts as dictionaries
    """
    if not scripts_dir.exists():
        raise FileNotFoundError(f"Scripts directory not found: {scripts_dir}")

    script_files = sorted(scripts_dir.glob("*.md"))

    if not script_files:
        print(f"No .md files found in {scripts_dir}")
        return []

    print(f"Found {len(script_files)} script files\n")

    results = []
    for script_path in script_files:
        try:
            result = parse_single_script(script_path, output_dir)
            results.append(result)
            print()
        except Exception as e:
            print(f"  ERROR: {e}\n")

    # Create summary file if output directory specified
    if output_dir and results:
        summary = {
            "total_scripts": len(results),
            "total_segments": sum(len(r['segments']) for r in results),
            "total_duration_seconds": sum(r['total_duration_seconds'] for r in results),
            "total_duration_minutes": sum(r['total_duration_seconds'] for r in results) / 60,
            "scripts": [
                {
                    "script_id": r['script_id'],
                    "title": r['title'],
                    "segments": len(r['segments']),
                    "duration_seconds": r['total_duration_seconds'],
                    "assets": len(r['assets_needed'])
                }
                for r in results
            ],
            "generated_at": datetime.now().isoformat()
        }

        summary_file = output_dir / "_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"Summary saved to: {summary_file}")

        # Print overall summary
        print(f"\n{'='*50}")
        print(f"PARSING COMPLETE")
        print(f"{'='*50}")
        print(f"Total scripts parsed: {summary['total_scripts']}")
        print(f"Total segments: {summary['total_segments']}")
        print(f"Total duration: {summary['total_duration_minutes']:.1f} minutes")

    return results


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="Parse video script markdown files into structured JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python video-script-parser.py --script script-0.1-welcome.md
  python video-script-parser.py --all
  python video-script-parser.py --all --output ./parsed-scripts/
  python video-script-parser.py --script script-0.1-welcome.md --output ./output/
        """
    )

    parser.add_argument(
        "--script",
        type=str,
        help="Parse a single script file (filename or full path)"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Parse all scripts in the video-scripts directory"
    )

    parser.add_argument(
        "--scripts-dir",
        type=str,
        default=str(DEFAULT_SCRIPTS_DIR),
        help=f"Directory containing script files (default: {DEFAULT_SCRIPTS_DIR})"
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Output directory for JSON files (default: print to stdout for single, save for --all)"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON to stdout (useful for piping)"
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.script and not args.all:
        parser.error("Must specify either --script or --all")

    if args.script and args.all:
        parser.error("Cannot specify both --script and --all")

    scripts_dir = Path(args.scripts_dir)
    output_dir = Path(args.output) if args.output else None

    try:
        if args.script:
            # Parse single script
            script_path = Path(args.script)

            # If not absolute, look in scripts directory
            if not script_path.is_absolute():
                script_path = scripts_dir / args.script

            result = parse_single_script(script_path, output_dir)

            # Output JSON if requested
            if args.json:
                print(json.dumps(result, indent=2, ensure_ascii=False))

        else:
            # Parse all scripts
            if not output_dir:
                output_dir = DEFAULT_OUTPUT_DIR

            results = parse_all_scripts(scripts_dir, output_dir)

            if args.json:
                print(json.dumps(results, indent=2, ensure_ascii=False))

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
