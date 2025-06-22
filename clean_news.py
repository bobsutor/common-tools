# cspell:ignore asis Crunchbase ndash tagtext yattag

import json

from common_data import DATA_FOLDER

PRESS_RELEASES_FILE = DATA_FOLDER + "/press-releases-and-blogs.json"
NEWS_FILE = DATA_FOLDER + "news-and-other-announcements.json"

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
            raise ValueError(f"Bad key: {key}")

        if "http" not in data["link"]:
            raise ValueError(f"Bad link: {data['link']}")

press_releases = dict(sorted(press_releases.items(), reverse=True, key=lambda item: item[0].casefold()))
news = dict(sorted(news.items(), reverse=True, key=lambda item: item[0].casefold()))

with open(PRESS_RELEASES_FILE, "wt", encoding="utf8") as file:
    json.dump(press_releases, file, indent=4, ensure_ascii=False)

with open(NEWS_FILE, "wt", encoding="utf8") as file:
    json.dump(news, file, indent=4, ensure_ascii=False)
