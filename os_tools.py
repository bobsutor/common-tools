# general purpose tools

# cspell:ignore autofit oxml powerpnt rels taskkill twips winword

import os
import shutil
import sys
import time
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


def start_timer():
    time_stack.append(datetime.now())


def end_timer():
    elapsed_time = datetime.now() - time_stack.pop()
    return elapsed_time.total_seconds()


def format_iso_date(date: str, include_day_of_week=False) -> str:
    try:
        if include_day_of_week:
            return datetime.fromisoformat(date).strftime("%A, %B %d, %Y").replace(" 0", " ")
        else:
            return datetime.fromisoformat(date).strftime("%B %d, %Y").replace(" 0", " ")
    except ValueError as exc:
        raise ValueError(f"Problem with date: {date}") from exc

    return "WHOOPS"


def kill_acrobat() -> None:
    os.system("taskkill /F /IM Acrobat.exe /T")


def kill_excel() -> None:
    os.system("taskkill /F /IM excel.exe /T")


def kill_powerpoint() -> None:
    os.system("taskkill /F /IM powerpnt.exe /T")


def kill_word() -> None:
    os.system("taskkill /F /IM winword.exe /T")


def warning(msg: str, indent=0) -> None:
    print(f"{indent * ' '}{fg.li_yellow}{msg}{fg.rs}")


def terminating_error(msg: str, indent=0) -> None:
    print(f"{indent * ' '}{fg.red}{msg}{fg.rs}")
    sys.exit(1)
