import sqlite3
import sys
from pathlib import Path


DB_PATH = Path(__file__).with_name("ai_internship.db")


def print_rows(cursor: sqlite3.Cursor, rows: list[tuple]) -> None:
    column_names = [description[0] for description in cursor.description or []]
    if not column_names:
        print("Query ran successfully.")
        return

    print(" | ".join(column_names))
    print("-" * (len(" | ".join(column_names))))
    for row in rows:
        print(" | ".join(str(value) if value is not None else "NULL" for value in row))


def main() -> int:
    if not DB_PATH.exists():
        print("Database not found. Run: python setup_db.py")
        return 1

    if len(sys.argv) > 1:
        sql = " ".join(sys.argv[1:])
    else:
        print("Type SQL, then press Enter.")
        sql = input("sql> ").strip()

    if not sql:
        print("No SQL provided.")
        return 1

    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.execute(sql)
        rows = cursor.fetchall()
        print_rows(cursor, rows)
        connection.commit()
    except sqlite3.Error as error:
        print(f"SQL error: {error}")
        return 1
    finally:
        connection.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
