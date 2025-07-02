# cspell:ignore asis Crunchbase ndash tagtext yattag

import json
import os
from datetime import date, datetime, timedelta

from common_data import DATA_FOLDER

PRESS_RELEASES_FILE = DATA_FOLDER + "/press-releases-and-blogs.json"
NEWS_FILE = DATA_FOLDER + "news-and-other-announcements.json"

LAST_WEEKS_NEWS = DATA_FOLDER + "/newsletter-entries-from-press-releases.json"

month_stats: dict[int, int] = dict()
for x in range(1, 13):
    month_stats[x] = 0


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


def is_within_X_days(date_string, X_days=8):
    """
    Check if a YYYY-MM-DD date string is within 8 days of today.

    Args:
        date_string (str): Date in YYYY-MM-DD format

    Returns:
        bool: True if the date is within 8 days (past or future), False otherwise
    """
    try:
        # Parse the input date string
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()

        # Get today's date
        today = datetime.now().date()

        # Calculate the absolute difference in days
        days_diff = abs((input_date - today).days)

        # Return True if within X_days days
        return days_diff <= X_days

    except ValueError:
        # Return False if the date string is invalid
        return False


os.system("cls")


with open(PRESS_RELEASES_FILE, "rt", encoding="utf8") as file:
    press_releases = json.load(file)

with open(NEWS_FILE, "rt", encoding="utf8") as file:
    news = json.load(file)

for d in [press_releases, news]:
    for key, data in d.items():
        if "date" in data:
            del data["date"]
        if "title" in data:
            del data["title"]

        data["companies"].sort(key=str.casefold)

        if "http" in key:
            raise ValueError(f"Bad key contains http: {key}")

        if data["link"].count("http") > 1:
            raise ValueError(f"Bad link contains http more than once: {data['link']}")

        if not data["link"]:
            raise ValueError(f"Missing link: {data['link']}")

        if "http" not in data["link"]:
            raise ValueError(f"Bad link without http: {data['link']}")

        if is_date_later_than_today(key[0:10]):
            raise ValueError(f"Bad key contains date after today: {key}")

        month_stats[int(key[5:7])] += 1

press_releases = dict(sorted(press_releases.items(), reverse=True, key=lambda item: item[0].casefold()))
news = dict(sorted(news.items(), reverse=True, key=lambda item: item[0].casefold()))

with open(PRESS_RELEASES_FILE, "wt", encoding="utf8") as file:
    json.dump(press_releases, file, indent=4, ensure_ascii=False)

with open(NEWS_FILE, "wt", encoding="utf8") as file:
    json.dump(news, file, indent=4, ensure_ascii=False)


newsletter_items = []

# print(month_stats)

for press_release_key, press_release_data in press_releases.items():
    press_release_date = press_release_key[:10]

    if is_within_X_days(press_release_date):
        newsletter_items.append(
            {
                "include": True,
                "authors": ["X"],
                "date": press_release_date,
                "description": [""],
                "link": press_release_data["link"],
                "title": press_release_key[12:],
                "type": "quantum-computing",
                "commentary": [""],
            }
        )


with open(LAST_WEEKS_NEWS, "wt", encoding="utf8") as file:
    json.dump(newsletter_items, file, indent=4, ensure_ascii=False)
