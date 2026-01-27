# general purpose tools

# cspell:ignore autofit oxml powerpnt rels taskkill twips winword rangle

import os
import shutil
import sys
import time
from datetime import date
from datetime import datetime

from sty import fg  # type: ignore

time_stack = []  # type: ignore


def clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def delete_dir_if_present(_dir: str) -> None:
    if os.path.isdir(_dir):
        # weird Windows permission error work around - something to do with timing
        while True:
            try:
                shutil.rmtree(_dir)
            except PermissionError:
                print(f"Saw PermissionError in 'delete_dir_if_present' for '{_dir}'")
                time.sleep(1.0)
            else:
                break


def delete_file_if_present(_file: str) -> None:
    if os.path.isfile(_file):
        # weird Windows permission error work around - something to do with timing
        while True:
            try:
                os.remove(_file)
            except PermissionError:
                print(f"Saw PermissionError in 'delete_file_if_present' for '{_file}'")
                time.sleep(1.0)
            else:
                break


def is_within_X_days(date_string, X_days=8):
    """
    Check if a YYYY-MM-DD date string is within X_days days before today.

    Args:
        date_string (str): Date in YYYY-MM-DD format

    Returns:
        bool: True if the date is within X_days days (past or future), False otherwise
    """
    try:
        # Parse the input date string
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()

        # Get today's date
        today = datetime.now().date()

        # Calculate the absolute difference in days
        # days_diff = abs((input_date - today).days)
        days_diff = (today - input_date).days

        if days_diff < 0:
            # newer than today
            return False

        # Return True if within X_days days
        return days_diff <= X_days

    except ValueError:
        # Return False if the date string is invalid
        return False


def is_date_later_than_today(date_string):
    """
    Tests if a date string in YYYY-MM-DD format is later than today.

    Args:
        date_string (str): The date in YYYY-MM-DD format.

    Returns:
        bool: True if the date is later than today, False otherwise.
    """
    try:
        # Parse the input date string into a date object
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()

        # Get today's date
        today = date.today()

        # Compare the dates
        return input_date > today
    except ValueError:
        print(f"Error: Invalid date format for '{date_string}'. Please use YYYY-MM-DD.")
        return False


def start_timer():
    time_stack.append(datetime.now())


def end_timer(decimal_places=1):
    elapsed_time = datetime.now() - time_stack.pop()
    return round(elapsed_time.total_seconds(), decimal_places)


def format_iso_date(date_: str, include_day_of_week_=False) -> str:
    try:
        if include_day_of_week_:
            return datetime.fromisoformat(date_).strftime("%A, %B %d, %Y").replace(" 0", " ")
        else:
            return datetime.fromisoformat(date_).strftime("%B %d, %Y").replace(" 0", " ")

    except ValueError as exc:
        raise ValueError(f"Problem with date: {date_}") from exc

    return "WHOOPS"


def kill_acrobat() -> None:
    os.system("taskkill /F /IM Acrobat.exe /T")


def kill_excel() -> None:
    os.system("taskkill /F /IM excel.exe /T")


def kill_powerpoint() -> None:
    os.system("taskkill /F /IM powerpnt.exe /T")


def kill_word() -> None:
    os.system("taskkill /F /IM winword.exe /T")


def information(msg: str, indent=0) -> None:
    print(f"{indent * ' '}{fg.li_green}{msg}{fg.rs}", flush=True)


def information_plain(msg: str, indent=0) -> None:
    print(f"{indent * ' '}{msg}", flush=True)


def warning(msg: str, indent=0) -> None:
    print(f"{indent * ' '}{fg.li_yellow}{msg}{fg.rs}", flush=True)


def terminating_error(msg: str, indent=0) -> None:
    print(f"{indent * ' '}{fg.red}{msg}{fg.rs}", flush=True)
    sys.exit(1)


def reflow_text_list(text_list: list[str], line_length=100) -> list[str]:
    if isinstance(text_list, str):
        text_list = [text_list]

    if not text_list:
        return [""]

    if not text_list[0]:
        return text_list

    text = " ".join(text_list).strip()

    if text[-1] not in [".", "!", "?", ">"]:
        text += "."

    text = text.replace("<br>", " ")
    text = text.replace("<br/>", " ")
    text = text.replace("<br />", " ")
    text = text.replace("<p> ", "<p>")
    text = text.replace("</p> ", "</p>")
    text = text.replace(" <p>", "<p>")
    text = text.replace(" </p>", "</p>")

    text = text.replace("|", "&vert;")
    text = text.replace("⟩", "&rangle;")
    text = text.replace("π", "&pi;")
    text = text.replace("θ", "&theta;")
    text = text.replace("φ", "&phi;")

    while "  " in text:
        text = text.replace("  ", " ")

    new_text_list: list[str] = []

    working_line_length = line_length

    while len(text) > working_line_length:
        # try to find a blank

        position = text.rfind(" ", 0, working_line_length)
        new_text = ""

        if position != -1:
            new_text = text[:position].strip()
            text = text[position:].strip()
        else:
            # keep making the working line length larger until we can find a blank

            working_line_length += 10
            continue

        new_text_list.append(new_text)
        working_line_length = line_length

    text = text.strip()
    if text:
        new_text_list.append(text)

    return new_text_list
