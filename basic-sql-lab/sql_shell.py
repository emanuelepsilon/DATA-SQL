import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("ai_internship.db")


HELP = """
Commands:
  .tables          show table names
  .schema TABLE    show columns for a table
  .help            show this help
  .exit            quit

SQL examples:
  SELECT * FROM applications;
  SELECT company, role FROM applications WHERE status = 'applied';
""".strip()


def print_rows(cursor: sqlite3.Cursor, rows: list[tuple]) -> None:
    column_names = [description[0] for description in cursor.description or []]
    if not column_names:
        print("OK")
        return

    widths = []
    for index, column_name in enumerate(column_names):
        max_value_width = max(
            [len(str(row[index])) if row[index] is not None else 4 for row in rows]
            or [0]
        )
        widths.append(max(len(column_name), max_value_width))

    header = " | ".join(
        column_name.ljust(widths[index])
        for index, column_name in enumerate(column_names)
    )
    separator = "-+-".join("-" * width for width in widths)
    print(header)
    print(separator)

    for row in rows:
        print(
            " | ".join(
                (str(value) if value is not None else "NULL").ljust(widths[index])
                for index, value in enumerate(row)
            )
        )


def run_sql(connection: sqlite3.Connection, sql: str) -> None:
    cursor = connection.execute(sql)
    rows = cursor.fetchall()
    print_rows(cursor, rows)
    connection.commit()


def show_tables(connection: sqlite3.Connection) -> None:
    run_sql(connection, "SELECT name FROM sqlite_master WHERE type = 'table';")


def show_schema(connection: sqlite3.Connection, table_name: str) -> None:
    run_sql(connection, f"PRAGMA table_info({table_name});")


def main() -> int:
    if not DB_PATH.exists():
        print("Database not found. Run this first:")
        print("  python setup_db.py")
        return 1

    print("SQL practice shell")
    print(f"Database: {DB_PATH}")
    print("Type .help for commands, .exit to quit.")
    print("End SQL statements with ;")
    print()

    connection = sqlite3.connect(DB_PATH)
    buffer: list[str] = []

    try:
        while True:
            prompt = "sql> " if not buffer else "...> "
            try:
                line = input(prompt)
            except (EOFError, KeyboardInterrupt):
                print()
                return 0

            stripped = line.strip()
            if not stripped:
                continue

            if not buffer and stripped.startswith("."):
                parts = stripped.split(maxsplit=1)
                command = parts[0].lower()

                if command in {".exit", ".quit"}:
                    return 0
                if command == ".help":
                    print(HELP)
                    continue
                if command == ".tables":
                    show_tables(connection)
                    continue
                if command == ".schema":
                    if len(parts) == 1:
                        print("Usage: .schema TABLE")
                    else:
                        show_schema(connection, parts[1])
                    continue

                print(f"Unknown command: {command}")
                continue

            buffer.append(line)
            sql = "\n".join(buffer).strip()
            if not sql.endswith(";"):
                continue

            try:
                run_sql(connection, sql)
            except sqlite3.Error as error:
                print(f"SQL error: {error}")
            finally:
                buffer.clear()

    finally:
        connection.close()


if __name__ == "__main__":
    raise SystemExit(main())
