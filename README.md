# Data Entry Table

A simple Python program for entering, viewing and deleting records in a table. It runs in the terminal and saves everything to a CSV file, so your data is still there the next time you open it.

## Features
- Add a record (name, course and marks)
- View all records in a neat bordered table
- Delete a record by its ID
- Automatic saving to `records.csv` (can be opened in Excel)
- Input checks: marks must be a number from 0 to 100, and the name cannot be empty
- Automatic ID numbers for each new record

## Requirements
- Python 3.8 or newer
- No extra libraries needed (uses the built-in `csv` and `os` modules)

## How to run
1. Download or clone this repository.
2. Open the folder in VS Code or a terminal.
3. Run:
   ```
   py data_entry_table.py
   ```
   (On some systems use `python data_entry_table.py` instead.)

## How to use
When the program starts, you will see this menu:

```
=== DATA ENTRY TABLE ===
1. Add record
2. View table
3. Delete record
4. Exit
```

- Type `1` and press Enter, then enter the name, course and marks.
- Type `2` to see the table.
- Type `3` and enter an ID to delete that record.
- Type `4` to exit.

### Example output
```
+----+-------+--------+-------+
| ID | Name  | Course | Marks |
+----+-------+--------+-------+
| 1  | Alice | IT     | 78.0  |
| 2  | Bob   | BBA    | 65.0  |
+----+-------+--------+-------+
Total records: 2
```

## Files
| File | Description |
|------|-------------|
| `data_entry_table.py` | The main program |
| `records.csv` | Created automatically when you add the first record |

## Customising
To change the columns, edit the `HEADERS` list at the top of `data_entry_table.py` and the questions in the `add_record` function.

## Author
Ronyvictor Waswa
