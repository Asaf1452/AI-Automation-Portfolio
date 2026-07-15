# AI & Python Automation Portfolio

Small, practical Python tools that save real time on repetitive work.
Each tool is a standalone project with its own README, instructions,
and clean, well-commented code — ready to run as-is or to be customized
for your business.

## Tools

### 📁 [File Organizer](file-organizer/)

Cleans up messy folders in seconds. Point it at any folder (like
Downloads) and it sorts every file into tidy subfolders — Images,
Documents, Videos, and more.

- Safe by design: preview mode, never deletes, never overwrites
- Sorting rules live in a simple config file — no coding needed to customize
- Zero dependencies: pure Python standard library

```
python organizer.py "C:\Users\You\Downloads" --dry-run
```

### 📊 [CSV Report Generator](csv-report-generator/)

Turns raw CSV exports (from a shop system, CRM, or accounting tool)
into polished Excel reports — styled headers, filters, formatted
numbers, a totals row, and an optional per-group summary sheet.

- Numeric columns detected automatically, no configuration
- One command replaces the weekly copy-paste-and-format routine
- One lightweight dependency (`openpyxl`)

```
python report.py sales.csv --group-by Region
```

## How these projects are built

- **Simple on purpose** — each tool is a single readable script a
  client's own team could maintain
- **Safe defaults** — preview modes, validation, and helpful error
  messages instead of crashes
- **Minimal dependencies** — standard library first; external packages
  only when truly required
- **Documented** — every tool ships with a README and step-by-step
  usage instructions

## Need something like this for your business?

These tools started as answers to common pain points, and each one can
be adapted to your exact workflow — different categories, different
report layouts, scheduled runs, email delivery, and more.

📫 **Contact:** asafyosef95@gmail.com
