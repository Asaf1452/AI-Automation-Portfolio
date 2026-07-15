"""
File Organizer
--------------
Sorts the files in a folder into categorized subfolders
(Images, Documents, Videos, etc.) based on file extension.

Categories are defined in config.json so they can be changed
without touching the code.

Usage:
    python organizer.py <folder>              # organize a folder
    python organizer.py <folder> --dry-run    # preview without moving anything

Requires: Python 3.8+ (standard library only, nothing to install)
"""

import argparse
import json
import shutil
from pathlib import Path

# config.json lives next to this script
CONFIG_FILE = Path(__file__).parent / "config.json"


def load_categories():
    """Read the category rules from config.json.

    Returns a dict that maps a file extension (like ".jpg")
    to a folder name (like "Images").
    """
    with open(CONFIG_FILE, encoding="utf-8") as f:
        config = json.load(f)

    # Flip the config around: {"Images": [".jpg", ".png"]}
    # becomes {".jpg": "Images", ".png": "Images"} for fast lookup.
    extension_map = {}
    for folder_name, extensions in config.items():
        for ext in extensions:
            extension_map[ext.lower()] = folder_name
    return extension_map


def pick_destination(file, extension_map):
    """Decide which subfolder a file belongs in."""
    extension = file.suffix.lower()
    # Files with an unknown extension go to "Other"
    return extension_map.get(extension, "Other")


def unique_path(destination):
    """If a file with the same name already exists at the destination,
    add a number to the name: report.pdf -> report (1).pdf
    """
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = f"{destination.stem} ({counter}){destination.suffix}"
        candidate = destination.with_name(new_name)
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder, dry_run=False):
    """Move every file in `folder` into its category subfolder.

    Returns the number of files moved (or that would be moved
    when dry_run is True).
    """
    extension_map = load_categories()
    moved = 0

    for file in sorted(folder.iterdir()):
        # Skip subfolders and hidden files (names starting with a dot)
        if file.is_dir() or file.name.startswith("."):
            continue

        category = pick_destination(file, extension_map)
        target_folder = folder / category
        target_file = unique_path(target_folder / file.name)

        if dry_run:
            print(f"[preview] {file.name}  ->  {category}/{target_file.name}")
        else:
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(target_file))
            print(f"[moved]   {file.name}  ->  {category}/{target_file.name}")

        moved += 1

    return moved


def main():
    parser = argparse.ArgumentParser(
        description="Organize a folder's files into categorized subfolders."
    )
    parser.add_argument("folder", help="Path of the folder to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving any files",
    )
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a folder.")
        return

    print(f"Organizing: {folder}")
    if args.dry_run:
        print("(dry run - no files will be moved)\n")

    count = organize(folder, dry_run=args.dry_run)

    if count == 0:
        print("Nothing to organize - the folder has no loose files.")
    elif args.dry_run:
        print(f"\n{count} file(s) would be moved. Run again without --dry-run to apply.")
    else:
        print(f"\nDone! {count} file(s) organized.")


if __name__ == "__main__":
    main()
