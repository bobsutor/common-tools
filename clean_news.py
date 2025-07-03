# cspell:ignore asis Crunchbase ndash tagtext yattag

import json
import os
from datetime import date, datetime

from common_data import DATA_FOLDER

PRESS_RELEASES_FILE = DATA_FOLDER + "/press-releases-and-blogs.json"
NEWS_FILE = DATA_FOLDER + "news-and-other-announcements.json"

LAST_WEEKS_NEWS = "newsletter-links.json"


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

# order is important in the following

terms_and_types = {
    " raises ": "financial",
    "equity offering": "financial",
    "private placement": "financial",
    "funding": "financial",
    "conference": "conference",
    "forum": "conference",
    "factory": "manufacturing",
    "manufacturing": "manufacturing",
    "roadmap": "roadmap",
    "road map": "roadmap",
    "cryptographic": "pqc",
    "encryption": "pqc",
    "qkd": "pqc",
    "pqc": "pqc",
    "post-quantum": "pqc",
    "protein": "quantum-computing-applications",
    "scheduling": "quantum-computing-applications",
    "optimization": "quantum-computing-applications",
    "error correction": "quantum-error-correction",
    "error suppression": "quantum-error-correction",
    "error mitigation": "quantum-error-correction",
    "qiskit": "quantum-coding",
    "cuda-q": "quantum-coding",
    "d-wave": "quantum-annealing",
    "nu quantum": "quantum-networking",
    "welinq": "quantum-networking",
    "quantum computing": "quantum-computing",
    "qunnect": "quantum-computing",
}

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

        title = key[12:].casefold()

        # data["type"] = ""

        if "type" not in data or not data["type"]:
            data["type"] = ""

            for term_, type_ in terms_and_types.items():
                if term_ in title:
                    data["type"] = type_
                    break

        if "description" not in data:
            data["description"] = [""]

        if "commentary" not in data:
            data["commentary"] = [""]

        if "authors" not in data:
            data["authors"] = ["X"]

        if "include" not in data:
            data["include"] = True

        data = dict(sorted(data.items(), key=lambda item: item[0].casefold()))
        d[key] = data

press_releases = dict(sorted(press_releases.items(), reverse=True, key=lambda item: item[0].casefold()))
news = dict(sorted(news.items(), reverse=True, key=lambda item: item[0].casefold()))

with open(PRESS_RELEASES_FILE, "wt", encoding="utf8") as file:
    json.dump(press_releases, file, indent=4, ensure_ascii=False)

with open(NEWS_FILE, "wt", encoding="utf8") as file:
    json.dump(news, file, indent=4, ensure_ascii=False)


newsletter_items = []

for d in [press_releases, news]:
    for key, data in d.items():
        date_ = key[:10]

        if is_within_X_days(date_):
            newsletter_items.append(
                {
                    "include": data.get("include", True),
                    "authors": data.get("authors", ["X"]),
                    "date": date_,
                    "description": data.get("description", [""]),
                    "link": data["link"],
                    "title": key[12:],
                    "type": data["type"],
                    "commentary": data.get("commentary", [""]),
                }
            )

newsletter_items = sorted(newsletter_items, key=lambda x: x["date"], reverse=True)


with open(LAST_WEEKS_NEWS, "wt", encoding="utf8") as file:
    json.dump({"quantum": newsletter_items}, file, indent=4, ensure_ascii=False)
