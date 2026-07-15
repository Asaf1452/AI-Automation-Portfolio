# File Organizer

A small Python tool that cleans up messy folders. Point it at any folder
(for example your Downloads folder) and it sorts every file into tidy
subfolders like `Images/`, `Documents/`, `Videos/`, and so on.

Built with the Python standard library only — **nothing to install**.

## What it does

Before:

```
Downloads/
├── invoice_march.pdf
├── vacation.jpg
├── setup.exe
├── report.xlsx
└── song.mp3
```

After:

```
Downloads/
├── Documents/
│   └── invoice_march.pdf
├── Images/
│   └── vacation.jpg
├── Installers/
│   └── setup.exe
├── Spreadsheets/
│   └── report.xlsx
└── Audio/
    └── song.mp3
```

## Requirements

- Python 3.8 or newer — that's it. No pip packages needed.

## How to use

1. Download or clone this folder.
2. Open a terminal in the `file-organizer` folder.
3. **Preview first** (recommended) — shows what would happen without
   moving anything:

   ```
   python organizer.py "C:\Users\YourName\Downloads" --dry-run
   ```

4. When the preview looks right, run it for real:

   ```
   python organizer.py "C:\Users\YourName\Downloads"
   ```

## Safety features

- `--dry-run` lets you preview every move before anything happens.
- Files are **moved, never deleted**.
- If a file with the same name already exists in the destination,
  the new file is renamed (`report.pdf` → `report (1).pdf`) —
  nothing is ever overwritten.
- Subfolders and hidden files are left untouched.

## Customizing the categories

All the sorting rules live in [config.json](config.json). Each entry is a
folder name and the list of file extensions that belong in it:

```json
{
  "Images": [".jpg", ".png"],
  "Documents": [".pdf", ".docx"]
}
```

Add, rename, or remove categories freely — no code changes needed.
Any extension not listed in the config goes into an `Other/` folder.

## Project structure

```
file-organizer/
├── organizer.py   # the tool (single file, ~120 lines)
├── config.json    # sorting rules (edit this to customize)
└── README.md      # this file
```
