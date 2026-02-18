import os
from datetime import datetime
from pprint import pformat

def create_log(obj, log_dir="logs"):
    """
    Appends a formatted representation of any object to a date-based log file.
    Creates the directory and file if they do not exist.
    """

    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Date-wise filename (YYYY-MM-DD.txt)
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_path = os.path.join(log_dir, f"{date_str}.txt")

    # Timestamp per entry
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Convert object to readable multi-line string
    parsed = pformat(obj, width=120)

    # Build log entry (line-based)
    lines = [
        f"[{timestamp}]",
        *parsed.splitlines(),
        "-" * 80,
        ""
    ]

    # Append to file
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines))
