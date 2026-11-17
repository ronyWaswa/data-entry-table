import csv
import os

FILE = "records.csv"
HEADERS = ["ID", "Name", "Course", "Marks"]


def load_records():
    """Read saved records from the CSV file (if it exists)."""
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline="") as f:
        return list(csv.DictReader(f))


def save_records(records):
    """Write all records to the CSV file."""
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(records)


def show_table(records):
    """Print the records as a neat table."""
    if not records:
        print("\nNo records yet.")
        return
    widths = {h: max(len(h), *(len(str(r[h])) for r in records)) for h in HEADERS}
    line = "+" + "+".join("-" * (widths[h] + 2) for h in HEADERS) + "+"
    print("\n" + line)
    print("| " + " | ".join(h.ljust(widths[h]) for h in HEADERS) + " |")
    print(line)
    for r in records:
        print("| " + " | ".join(str(r[h]).ljust(widths[h]) for h in HEADERS) + " |")
    print(line)
    print(f"Total records: {len(records)}")


def add_record(records):
    """Ask for one row of data and add it to the table."""
    name = input("Name: ").strip()
    course = input("Course: ").strip()
    try:
        marks = float(input("Marks (0-100): "))
    except ValueError:
        print("Marks must be a number. Record not added.")
        return
    if not name or not 0 <= marks <= 100:
        print("Invalid data. Record not added.")
        return
    next_id = max((int(r["ID"]) for r in records), default=0) + 1
    records.append({"ID": next_id, "Name": name, "Course": course, "Marks": marks})
    save_records(records)
    print("Record saved.")


def delete_record(records):
    """Remove a row by its ID."""
    rid = input("ID to delete: ").strip()
    kept = [r for r in records if str(r["ID"]) != rid]
    if len(kept) == len(records):
        print("No record with that ID.")
        return records
    save_records(kept)
    print("Record deleted.")
    return kept


def main():
    records = load_records()
    while True:
        print("\n=== DATA ENTRY TABLE ===")
        print("1. Add record\n2. View table\n3. Delete record\n4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_table(records)
        elif choice == "3":
            records = delete_record(records)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()