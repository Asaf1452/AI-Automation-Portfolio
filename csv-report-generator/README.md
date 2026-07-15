# CSV Report Generator

A small Python tool that turns a plain CSV file into a polished,
ready-to-send Excel report — styled headers, filters, auto-sized
columns, formatted numbers, a totals row, and an optional summary
sheet (e.g. total sales per region).

Perfect for anyone who exports CSVs from a shop system, CRM, or
accounting tool and wastes time formatting them in Excel every week.

## What it does

Give it this (`sales.csv`):

```
Date,Product,Region,Units Sold,Revenue
2026-06-01,Laptop Stand,North,12,539.88
2026-06-02,USB Hub,South,30,449.70
...
```

Get back `sales_report.xlsx` with:

- **Data sheet** — the full table with a styled blue header row,
  dropdown filters, frozen header, thousand-separated numbers,
  and a bold **TOTAL** row at the bottom.
- **Summary sheet** (optional) — one row per group with totals,
  e.g. Units Sold and Revenue per Region.

## Requirements

- Python 3.8 or newer
- One library: `openpyxl` (needed to create real .xlsx files)

Install it with:

```
pip install -r requirements.txt
```

## How to use

Basic report:

```
python report.py sample_data.csv
```

Report **plus** a summary sheet grouped by a column:

```
python report.py sample_data.csv --group-by Region
```

Choose the output file name:

```
python report.py sample_data.csv --output june_report.xlsx
```

A `sample_data.csv` file is included so you can try it right away.

## Nice details

- Numeric columns are detected automatically — no configuration needed.
- Values like `1,250` (with thousand separators) are read correctly.
- Whole numbers show as `42`, money-like values as `539.88`.
- The `--group-by` column name is validated, with a helpful error
  listing the available columns if you mistype it.
- Works with any CSV, not just sales data.

## Project structure

```
csv-report-generator/
├── report.py          # the tool (single file, well commented)
├── sample_data.csv    # example data to test with
├── requirements.txt   # the one dependency (openpyxl)
└── README.md          # this file
```
