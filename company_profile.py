# cspell:ignore asis Crunchbase ndash tagtext yattag noopener

import json
from datetime import date, datetime

import os_tools
import yattag
from common_data import DATA_FOLDER, ORGANIZATION_DATA_FOLDER

TODAY_YY_MM_DD = date.today().strftime("%Y-%m-%d")

NEWS_ARCHIVE_FILE = "news-archive.json"

MAX_NEWS_ITEMS = 30

with open(f"{DATA_FOLDER}/{NEWS_ARCHIVE_FILE}", "rt", encoding="utf8") as file:
    press_releases = json.load(file)


def is_within_last_year(reference_date_str: str, target_date_str: str) -> bool:
    """
    Checks if target_date is within the year ending on reference_date.

    Args:
        reference_date_str: The reference date string ("YYYY-MM-DD").
        target_date_str: The date string to check ("YYYY-MM-DD").

    Returns:
        True if target_date is strictly after (reference_date - 1 year)
        and less than or equal to reference_date. False otherwise.

    Raises:
        ValueError: If date strings are not in "YYYY-MM-DD" format.
    """
    try:
        # 1. Parse the date strings into date objects
        # Using .date() is efficient if you don't need time information
        ref_date = datetime.strptime(reference_date_str, "%Y-%m-%d").date()
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from exc

    # 2. Calculate the date exactly one year before the reference date
    # Using replace handles leap years correctly (e.g., one year before 2024-02-29 is 2023-02-28)
    one_year_prior = ref_date.replace(year=ref_date.year - 1)

    # 3. Perform the comparison
    # The target date must be:
    # - Strictly *after* the date one year prior
    # - Less than or equal to the reference date
    return one_year_prior < target_date <= ref_date


def build_company_profile(company_name: str, heading_level: str = "h3", indent_sections=True) -> str:
    # os.system("cls")

    input_json = f"{ORGANIZATION_DATA_FOLDER}{company_name}.json"

    company_data = dict()
    name = ""

    try:
        with open(input_json, "rt", encoding="utf8") as json_file:
            for name_, data_ in json.load(json_file).items():
                name = name_
                company_data = data_
                break

    except FileNotFoundError as exc:
        os_tools.terminating_error(f"Could not find the company data for '{company_name}':  {exc}")

    doc, tag, text = yattag.Doc().tagtext()

    if indent_sections:
        p_style = "margin-left: 40px;"
    else:
        p_style = ""

    with tag(heading_level):
        text("Company")

    with tag("p", style=p_style):
        with tag(
            "a",
            href=company_data["links"]["website"],
            target="_blank",
            title="Go to company website",
            rel="noopener",
        ):
            text(company_name)

        if company_data["financial"]["public"]:
            text(" (")
            with tag(
                "a",
                href=f"https://finance.yahoo.com/quote/{company_data['financial']['ticker-symbol']}/",
                target="_blank",
                rel="noopener",
                title="Get company information from Yahoo! Finance",
            ):
                text(company_data["financial"]["ticker-symbol"])
            text(")")

        if company_data["contact-info"]["email"]:
            doc.stag("br")
            text("Contact Email: ")
            with tag(
                "a",
                href=f"mailto:{company_data['contact-info']['email']}",
                target="_blank",
                title="Send an email",
            ):
                text(company_data["contact-info"]["email"])

        if company_data["contact-info"]["phone"]:
            doc.stag("br")
            phone = company_data["contact-info"]["phone"]
            if not phone.startswith("+"):
                phone = "+1" + phone
            phone = phone.replace("(", "").replace(")", "")
            phone = phone.replace("-", "").replace(".", "")
            phone = phone.replace(" ", "")
            text("Contact Phone: ")
            with tag("a", href=f"tel:{phone}", target="_blank", title="Call the company"):
                text(phone)

    with tag(heading_level):
        text("Year Founded")

    with tag("p", style=p_style):
        text(company_data["year-founded"])

    if (
        "financial" in company_data
        and "date-went-public" in company_data["financial"]
        and company_data["financial"]["date-went-public"] is not None
    ):
        with tag(heading_level):
            text("Date Went Public")

        with tag("p", style=p_style):
            text(os_tools.format_iso_date(company_data["financial"]["date-went-public"]))

    with tag(heading_level):
        text("Headquarters")

    with tag("p", style=p_style):
        with tag(
            "a",
            href=f"https://google.com/maps/search/{company_data['hq-address']['long']}",
            target="_blank",
            rel="noopener",
            title="See location on Google Maps",
        ):
            text(company_data["hq-address"]["long"])

    with tag(heading_level):
        text("Company Description")

    with tag("p", style=p_style):
        with tag("em"):
            text(
                f"Generated with the aid of {company_data['description']['source']}"
                + f" on {os_tools.format_iso_date(company_data['description']['date-last-updated'])}"
            )

    with tag("p", style=p_style):
        text(" ".join(company_data["description"]["text"]))

    with tag(heading_level):
        text("Senior Leadership")

    with tag("table", style="width: 100%;"):
        for role, role_data in company_data["leadership"].items():
            with tag("tr"):
                if not isinstance(role_data, list):
                    role_data = [role_data]

                for person in role_data:
                    with tag("td", style="width: 15%;"):
                        if person["links"]["image"] is not None and person["links"]["image"]:
                            if person["links"]["primary"] is not None and person["links"]["primary"]:
                                with tag(
                                    "a", href=person["links"]["primary"], target="_blank", rel="noopener"
                                ):
                                    doc.stag(
                                        "img",
                                        src=person["links"]["image"].strip(),
                                        style="width: 5em; border-radius: 50%;",
                                    )
                            else:
                                doc.stag(
                                    "img",
                                    src=person["links"]["image"].strip(),
                                    style="width: 5em; border-radius: 50%;",
                                )
                        else:
                            doc.asis("&nbsp;")
                    with tag("td", style="width: 42.5%;"):
                        if person["links"]["primary"] is not None and person["links"]["primary"]:
                            with tag("a", href=person["links"]["primary"], target="_blank", rel="noopener"):
                                text(person["name"])
                        else:
                            text(person["name"])

                    with tag("td", style="width: 42.5%;"):
                        text(role)

    # with tag("ul"):
    #     for role, role_data in company_data["leadership"].items():
    #         if not isinstance(role_data, list):
    #             role_data = [role_data]

    #         for person in role_data:
    #             with tag("li"):
    #                 if person["links"]["primary"] is not None and person["links"]["primary"]:
    #                     if ".linkedin." in person["links"]["primary"]:
    #                         with tag(
    #                             "a",
    #                             href=person["links"]["primary"],
    #                             target="_blank",
    #                             title="Go to their LinkedIn profile",
    #                         ):
    #                             text(person["name"])
    #                     else:
    #                         with tag("a", href=person["links"]["primary"], target="_blank"):
    #                             text(person["name"])
    #                 else:
    #                     text(person["name"])

    #                 text(", ")
    #                 text(role)

    # if "leadership" in company_data["quantum"] and company_data["quantum"]["leadership"]:
    #     with tag(heading_level):
    #         text("Quantum Leadership")

    #     with tag("ul"):
    #         for role, role_data in company_data["quantum"]["leadership"].items():
    #             if not isinstance(role_data, list):
    #                 role_data = [role_data]

    #             for person in role_data:
    #                 with tag("li"):
    #                     if person["links"]["primary"] is not None and person["links"]["primary"]:
    #                         with tag("a", href=person["links"]["primary"], target="_blank"):
    #                             text(person["name"])
    #                     else:
    #                         text(person["name"])

    #                     text(", ")
    #                     text(role)

    # Show recent press releases and blog posts if there are any

    company_news_items = []  # type: ignore
    other_earnings_briefs = []  # type: ignore

    for press_release_key, press_release_data in press_releases.items():
        if (
            "include-in-daily-links" in press_release_data
            and not press_release_data["include-in-daily-links"]
        ):
            continue

        if name in press_release_data["companies"]:
            the_title = press_release_key[12:]

            if the_title.startswith("Sutor Group Earnings Brief:"):
                other_earnings_briefs.append(
                    {"date": press_release_key[:10], "title": the_title, "link": press_release_data["link"]}
                )
            elif the_title.startswith("The Futurum Group"):
                other_earnings_briefs.append(
                    {"date": press_release_key[:10], "title": the_title, "link": press_release_data["link"]}
                )
            else:
                company_news_items.append(
                    {"date": press_release_key[:10], "title": the_title, "link": press_release_data["link"]}
                )

    if other_earnings_briefs:
        filtered_announcements = []
        for announcement in other_earnings_briefs:
            if announcement["date"] and not is_within_last_year(TODAY_YY_MM_DD, announcement["date"]):
                continue

            if not announcement["link"]:
                continue

            filtered_announcements.append(announcement)

        if filtered_announcements:
            with tag(heading_level):
                text("Previous Earnings Briefs")

            with tag("ul"):
                for announcement in filtered_announcements:
                    with tag("li"):
                        if announcement["date"]:
                            text(os_tools.format_iso_date(announcement["date"]))
                            doc.asis(" &ndash; ")

                        with tag("a", href=announcement["link"], target="_blank", rel="noopener"):
                            text(announcement["title"])

    if company_news_items:
        news_item_count = 0

        filtered_announcements = []
        for announcement in company_news_items:
            if announcement["date"] and not is_within_last_year(TODAY_YY_MM_DD, announcement["date"]):
                continue

            if not announcement["link"]:
                continue

            news_item_count += 1
            if news_item_count > MAX_NEWS_ITEMS:
                break

            filtered_announcements.append(announcement)

        if filtered_announcements:
            with tag(heading_level):
                text("Selected Recent Press Releases, Announcements, News, and Blog Posts")

            with tag("ul"):
                for announcement in filtered_announcements:
                    with tag("li"):
                        if announcement["date"]:
                            text(os_tools.format_iso_date(announcement["date"]))
                            doc.asis(" &ndash; ")

                        with tag("a", href=announcement["link"], target="_blank", rel="noopener"):
                            text(announcement["title"])

    result = yattag.indent(doc.getvalue())
    # result = doc.getvalue()

    result = result.replace("</strong>\n      <a", "</strong> <a")

    return result


if __name__ == "__main__":
    COMPANY = "D-Wave Quantum"
    with open(
        f"../sg-reports/output/{COMPANY}-Company-Profile.html", "wt", encoding="utf-8"
    ) as output_html_file:
        print(build_company_profile(COMPANY, "h3", True), file=output_html_file)
