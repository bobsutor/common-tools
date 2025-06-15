"""
Formatting glossary with yattag
"""

# cspell:ignore addnext Aptos klass Oxml OxmlElement Pt yattag

import docx_tools
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

# cspell:disable

eu_countries = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
]

# EMEA (Europe, Middle East, and Africa)
emea_countries = [
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Armenia",
    "Austria",
    "Azerbaijan",
    "Bahrain",
    "Belarus",
    "Belgium",
    "Benin",
    "Bosnia and Herzegovina",
    "Botswana",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cameroon",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Comoros",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Egypt",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Faroe Islands",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Guernsey",
    "Guinea",
    "Guinea-Bissau",
    "Hungary",
    "Iceland",
    "Iran",
    "Iraq",
    "Ireland",
    "Isle of Man",
    "Israel",
    "Italy",
    "Ivory Coast",
    "Jersey",
    "Jordan",
    "Kenya",
    "Kuwait",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Mali",
    "Malta",
    "Mauritania",
    "Mauritius",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Netherlands",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Palestine",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Slovakia",
    "Slovenia",
    "Somalia",
    "South Africa",
    "Spain",
    "Sudan",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tanzania",
    "Togo",
    "Tunisia",
    "Turkey",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "Vatican City",
    "Western Sahara",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

# NA (North America)
na_countries = [
    "Antigua and Barbuda",
    "Bahamas",
    "Barbados",
    "Belize",
    "Canada",
    "Costa Rica",
    "Cuba",
    "Dominica",
    "Dominican Republic",
    "El Salvador",
    "Grenada",
    "Guatemala",
    "Haiti",
    "Honduras",
    "Jamaica",
    "Mexico",
    "Nicaragua",
    "Panama",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Trinidad and Tobago",
    "United States",
]

# LATAM (Latin America)
latam_countries = [
    "Argentina",
    "Belize",
    "Bolivia",
    "Brazil",
    "Chile",
    "Colombia",
    "Costa Rica",
    "Cuba",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "El Salvador",
    "French Guiana",
    "Guatemala",
    "Guyana",
    "Haiti",
    "Honduras",
    "Jamaica",
    "Mexico",
    "Nicaragua",
    "Panama",
    "Paraguay",
    "Peru",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Suriname",
    "Trinidad and Tobago",
    "Uruguay",
    "Venezuela",
]

# APAC (Asia-Pacific)
apac_countries = [
    "Afghanistan",
    "Australia",
    "Bangladesh",
    "Bhutan",
    "Brunei",
    "Cambodia",
    "China",
    "Cook Islands",
    "Fiji",
    "India",
    "Indonesia",
    "Japan",
    "Kiribati",
    "Laos",
    "Malaysia",
    "Maldives",
    "Marshall Islands",
    "Micronesia",
    "Mongolia",
    "Myanmar",
    "Nepal",
    "New Caledonia",
    "New Zealand",
    "Niue",
    "North Korea",
    "Pakistan",
    "Palau",
    "Papua New Guinea",
    "Philippines",
    "Singapore",
    "Solomon Islands",
    "South Korea",
    "Sri Lanka",
    "Thailand",
    "Timor-Leste",
    "Tonga",
    "Tuvalu",
    "Vanuatu",
    "Vietnam",
]

# APME (Asia-Pacific Middle East)

apme_countries = [
    "Australia",
    "Bahrain",
    "Bangladesh",
    "Bhutan",
    "Brunei",
    "Cambodia",
    "China",
    "Fiji",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Israel",
    "Japan",
    "Jordan",
    "Kiribati",
    "Kuwait",
    "Laos",
    "Lebanon",
    "Malaysia",
    "Maldives",
    "Marshall Islands",
    "Micronesia",
    "Mongolia",
    "Myanmar (Burma)",
    "Nauru",
    "Nepal",
    "New Zealand",
    "North Korea",
    "Oman",
    "Pakistan",
    "Palau",
    "Papua New Guinea",
    "Philippines",
    "Qatar",
    "Samoa",
    "Saudi Arabia",
    "Singapore",
    "Solomon Islands",
    "South Korea",
    "Sri Lanka",
    "Syria",
    "Taiwan",
    "Thailand",
    "Timor-Leste",
    "Tonga",
    "Tuvalu",
    "United Arab Emirates",
    "Vanuatu",
    "Vietnam",
    "Yemen",
]

# AMER (North, Central, and South America)

amer_countries = [
    "Anguilla",
    "Antigua and Barbuda",
    "Argentina",
    "Aruba",
    "Barbados",
    "Belize",
    "Bermuda",
    "Bolivia",
    "Brazil",
    "British Virgin Islands",
    "Canada",
    "Cayman Islands",
    "Chile",
    "Colombia",
    "Costa Rica",
    "Cuba",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "El Salvador",
    "Greenland",
    "Grenada",
    "Guadeloupe",
    "Guatemala",
    "Guyana",
    "Haiti",
    "Honduras",
    "Jamaica",
    "Martinique",
    "Mexico",
    "Montserrat",
    "Netherlands Antilles",
    "Nicaragua",
    "Panama",
    "Paraguay",
    "Peru",
    "Puerto Rico",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines",
    "Suriname",
    "The Bahamas",
    "Trinidad and Tobago",
    "Turks and Caicos Islands",
    "U.S. Virgin Islands",
    "United States",
    "Uruguay",
    "Venezuela",
]

oceania_countries = [
    "Australia",
    "New Zealand",
    "Papua New Guinea",
    "Fiji",
    "Solomon Islands",
    "Vanuatu",
    "Samoa",
    "Kiribati",
    "Tonga",
    "Micronesia",
    "Marshall Islands",
    "Palau",
    "Tuvalu",
    "Nauru",
]


regions_data = {
    # this is the order they are shown on the chart
    "APAC": {"countries": apac_countries, "name": "Asia-Pacific"},
    "EMEA": {"countries": emea_countries, "name": "Europe, Middle East, and Africa"},
    "LATAM": {"countries": latam_countries, "name": "Latin America"},
    "NA": {"countries": na_countries, "name": "North America"},
    "AMER": {"countries": amer_countries, "name": "North, Central, and South America"},
    "APME": {"countries": apme_countries, "name": "Asia Pacific and Middle East"},
    "EU": {"countries": eu_countries, "name": "European Union"},
    "OC": {"countries": oceania_countries, "name": "Oceania"},
}


regions_counts = dict()  # type: ignore


for _region_abbreviation, _region_data in regions_data.items():
    regions_counts[_region_abbreviation] = dict()
    regions_counts[_region_abbreviation]["count"] = 0
    regions_counts[_region_abbreviation]["countries"] = dict()
    for _country in _region_data["countries"]:
        regions_counts[_region_abbreviation]["countries"][_country] = 0

# U.S. states and territories

us_states_and_territories = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District of Columbia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "VI": "Virgin Islands",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
}

us_state_counts: dict[str, int] = dict()

for _state in us_states_and_territories.values():
    us_state_counts[_state] = 0

us_governors = {
    "Alabama": {"Governor": "Kay Ivey", "Party": "Republican"},
    "Alaska": {"Governor": "Mike Dunleavy", "Party": "Republican"},
    "Arizona": {"Governor": "Katie Hobbs", "Party": "Democratic"},
    "Arkansas": {"Governor": "Sarah Huckabee Sanders", "Party": "Republican"},
    "California": {"Governor": "Gavin Newsom", "Party": "Democratic"},
    "Colorado": {"Governor": "Jared Polis", "Party": "Democratic"},
    "Connecticut": {"Governor": "Ned Lamont", "Party": "Democratic"},
    "Delaware": {"Governor": "Matt Meyer", "Party": "Democratic"},
    "Florida": {"Governor": "Ron DeSantis", "Party": "Republican"},
    "Georgia": {"Governor": "Brian Kemp", "Party": "Republican"},
    "Hawaii": {"Governor": "Josh Green", "Party": "Democratic"},
    "Idaho": {"Governor": "Brad Little", "Party": "Republican"},
    "Illinois": {"Governor": "J.B. Pritzker", "Party": "Democratic"},
    "Indiana": {"Governor": "Eric Holcomb", "Party": "Republican"},
    "Iowa": {"Governor": "Kim Reynolds", "Party": "Republican"},
    "Kansas": {"Governor": "Laura Kelly", "Party": "Democratic"},
    "Kentucky": {"Governor": "Andy Beshear", "Party": "Democratic"},
    "Louisiana": {"Governor": "Jeff Landry", "Party": "Republican"},
    "Maine": {"Governor": "Janet Mills", "Party": "Democratic"},
    "Maryland": {"Governor": "Wes Moore", "Party": "Democratic"},
    "Massachusetts": {"Governor": "Maura Healey", "Party": "Democratic"},
    "Michigan": {"Governor": "Gretchen Whitmer", "Party": "Democratic"},
    "Minnesota": {"Governor": "Tim Walz", "Party": "Democratic"},
    "Mississippi": {"Governor": "Tate Reeves", "Party": "Republican"},
    "Missouri": {"Governor": "Mike Kehoe", "Party": "Republican"},
    "Montana": {"Governor": "Greg Gianforte", "Party": "Republican"},
    "Nebraska": {"Governor": "Jim Pillen", "Party": "Republican"},
    "Nevada": {"Governor": "Joe Lombardo", "Party": "Republican"},
    "New Hampshire": {"Governor": "Kelly Ayotte", "Party": "Republican"},
    "New Jersey": {"Governor": "Phil Murphy", "Party": "Democratic"},
    "New Mexico": {"Governor": "Michelle Lujan Grisham", "Party": "Democratic"},
    "New York": {"Governor": "Kathy Hochul", "Party": "Democratic"},
    "North Carolina": {"Governor": "Josh Stein", "Party": "Democratic"},
    "North Dakota": {"Governor": "Kelly Armstrong", "Party": "Republican"},
    "Ohio": {"Governor": "Mike DeWine", "Party": "Republican"},
    "Oklahoma": {"Governor": "Kevin Stitt", "Party": "Republican"},
    "Oregon": {"Governor": "Tina Kotek", "Party": "Democratic"},
    "Pennsylvania": {"Governor": "Josh Shapiro", "Party": "Democratic"},
    "Rhode Island": {"Governor": "Daniel McKee", "Party": "Democratic"},
    "South Carolina": {"Governor": "Henry McMaster", "Party": "Republican"},
    "South Dakota": {"Governor": "Larry Rhoden", "Party": "Republican"},
    "Tennessee": {"Governor": "Bill Lee", "Party": "Republican"},
    "Texas": {"Governor": "Greg Abbott", "Party": "Republican"},
    "Utah": {"Governor": "Spencer Cox", "Party": "Republican"},
    "Vermont": {"Governor": "Phil Scott", "Party": "Republican"},
    "Virginia": {"Governor": "Glenn Youngkin", "Party": "Republican"},
    "Washington": {"Governor": "Bob Ferguson", "Party": "Democratic"},
    "West Virginia": {"Governor": "Patrick Morrisey", "Party": "Republican"},
    "Wisconsin": {"Governor": "Tony Evers", "Party": "Democratic"},
    "Wyoming": {"Governor": "Mark Gordon", "Party": "Republican"},
}

# Canadian provinces and territories

canadian_provinces_and_territories = {
    "AB": "Alberta",
    "BC": "British Columbia",
    "MB": "Manitoba",
    "NB": "New Brunswick",
    "NL": "Newfoundland and Labrador",
    "NS": "Nova Scotia",
    "NT": "Northwest Territories",
    "NU": "Nunavut",
    "ON": "Ontario",
    "PE": "Prince Edward Island",
    "QC": "Québec",
    "SK": "Saskatchewan",
    "YT": "Yukon",
}

canada_province_counts: dict[str, int] = dict()

for _province in canadian_provinces_and_territories.values():
    canada_province_counts[_province] = 0

# Australian states and territories

australian_states_and_territories = {
    "ACT": "Australian Capital Territory",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "QLD": "Queensland",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "WA": "Western Australia",
}

# German federal states

german_states = {
    "BW": "Baden-Württemberg",
    "BY": "Bavaria",
    "BE": "Berlin",
    "BB": "Brandenburg",
    "HB": "Bremen",
    "HH": "Hamburg",
    "HE": "Hesse",
    "NI": "Lower Saxony",
    "MV": "Mecklenburg-Vorpommern",
    "NW": "North Rhine-Westphalia",
    "RP": "Rhineland-Palatinate",
    "SL": "Saarland",
    "SN": "Saxony",
    "ST": "Saxony-Anhalt",
    "SH": "Schleswig-Holstein",
    "TH": "Thuringia",
}

german_state_counts: dict[str, int] = dict()

for _state in german_states.values():
    german_state_counts[_state] = 0


# French modern region names

french_current_regions_names = [
    "Auvergne-Rhône-Alpes",
    "Bourgogne-Franche-Comté",
    "Bretagne",
    "Centre-Val de Loire",
    "Corse",
    "Grand Est",
    "Hauts-de-France",
    "Île-de-France",
    "Normandie",
    "Nouvelle-Aquitaine",
    "Occitanie",
    "Pays de la Loire",
    "Provence-Alpes-Côte d'Azur",
]


french_region_counts: dict[str, int] = dict()

for _region in french_current_regions_names:
    french_region_counts[_region] = 0

japanese_regions = [
    "Chubu",
    "Chugoku",
    "Hokkaido",
    "Kansai",
    "Kanto",
    "Kyushu",
    "Okinawa",
    "Shikoku",
    "Tohoku",
]

# cspell:enable


def get_region_abbreviations():
    return [region for region in regions_data]


def increment_country_in_regions(country):
    if country == "USA":
        country = "United States"
    elif country == "UK":
        country = "United Kingdom"
    elif country == "UAE":
        country = "United Arab Emirates"
    elif country == "The Netherlands":
        country = "Netherlands"
        print("Replace 'The Netherlands' with 'Netherlands'")

    found_a_region = False

    for region, countries_in_region in regions_counts.items():
        if country in countries_in_region["countries"]:
            found_a_region = True
            regions_counts[region]["count"] += 1
            countries_in_region["countries"][country] += 1

    if not found_a_region:
        print(f"Country {country} is not in any region.")


def print_countries_in_regions_counts():
    for region_name, data in regions_counts.items():
        title = f"{region_name}: {data['count']}"
        print(f"\n{title}\n{len(title) * '-'}")
        for country, country_count in data["countries"].items():
            if country_count > 0:
                print(f"  {country}: {country_count}")


def increment_state_in_US(address):
    state = get_state_or_province(address)
    assert state in us_states_and_territories.values()
    us_state_counts[state] += 1  # type: ignore


def get_US_state_counts():
    states = []
    counts = []
    for _state, _count in us_state_counts.items():
        if _count != 0:
            states.append(_state)
            counts.append(_count)
    return states, counts


def increment_province_in_Canada(address):
    province = get_state_or_province(address)
    assert province in canadian_provinces_and_territories.values()
    canada_province_counts[province] += 1  # type: ignore


def get_Canada_province_counts():
    provinces = []
    counts = []
    for _province, _count in canada_province_counts.items():
        if _count != 0:
            provinces.append(_province)
            counts.append(_count)
    return provinces, counts


def increment_region_in_France(address):
    region = get_state_or_province(address)
    if region not in french_current_regions_names:
        raise ValueError(f"Unknown French region: {region}")
    french_region_counts[region] += 1  # type: ignore


def get_French_region_counts():
    regions = []
    counts = []
    for _region, _count in french_region_counts.items():
        if _count != 0:
            regions.append(_region)
            counts.append(_count)
    return regions, counts


def increment_state_in_Germany(address):
    state = get_state_or_province(address)
    if state not in german_states.values():
        raise ValueError(f"Unknown German state: {state}")
    german_state_counts[state] += 1  # type: ignore


def get_German_state_counts():
    states = []
    counts = []
    for _state, _count in german_state_counts.items():
        if _count != 0:
            states.append(_state)
            counts.append(_count)
    return states, counts


def increment_state_province_or_local_region(address):
    country = get_country(address)

    if country == "USA":
        increment_state_in_US(address)

    elif country == "Canada":
        increment_province_in_Canada(address)

    elif country == "France":
        increment_region_in_France(address)

    elif country == "Germany":
        increment_state_in_Germany(address)

    elif country == "UK":
        increment_UK_city(address)


def get_max_companies_in_a_state_or_province():
    m = max(us_state_counts.values())
    m = max(m, *canada_province_counts.values())
    m = max(m, *french_region_counts.values())
    m = max(m, *german_state_counts.values())
    return m


# UK cities

UK_city_counts: dict[str, int] = dict()


def increment_UK_city(address):
    city = get_city(address)
    if city not in UK_city_counts:
        UK_city_counts[city] = 1
    else:
        UK_city_counts[city] += 1


def get_UK_city_counts():
    sorted_UK_city_counts = {k: UK_city_counts[k] for k in sorted(UK_city_counts)}
    cities = []
    counts = []
    for _city, _count in sorted_UK_city_counts.items():
        if _count != 0:
            cities.append(_city)
            counts.append(_count)
    return cities, counts


def get_regions_and_counts():
    regions = sorted(list(regions_counts.keys()), key=str.casefold)
    counts = [regions_counts[region]["count"] for region in regions]

    return (regions, counts)


def write_region_html_appendix(id_, appendix_title, yattag_tag, yattag_text):
    with yattag_tag("h2", id=id_):
        yattag_text(appendix_title)

    for region_abbreviation, region_data in regions_data.items():
        with yattag_tag("p", klass="region-name"):
            yattag_text(f"{region_data['name']} ({region_abbreviation})")

        with yattag_tag("p", klass="country-list"):
            yattag_text(", ".join(region_data["countries"]))


def write_region_word_appendix(id_, appendix_title, word_document):
    # pylint: disable=W0212
    heading = word_document.add_heading(appendix_title, 1)
    run = heading.runs[0]
    docx_tools.add_bookmark_for_id(id_, run)

    # Create a custom region style
    region_style = word_document.styles.add_style("RegionAppendix", 1)
    region_style.font.name = "Aptos"
    region_style.font.bold = True
    region_style.font.italic = False
    region_style.font.size = word_document.styles["Normal"].font.size

    sorted_by_region = dict(sorted(regions_data.items(), key=lambda item: item[0]))

    for region_abbreviation, region_data in sorted_by_region.items():
        # p = word_document.add_paragraph(
        #     f"{region_data['name']} ({region_abbreviation})", style="RegionAppendix"
        # )

        p = word_document.add_paragraph(
            f"{region_abbreviation} – {region_data['name']}", style="RegionAppendix"
        )
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.keep_with_next = True

        p = word_document.add_paragraph(", ".join(region_data["countries"]))
        p.paragraph_format.left_indent = Pt(18)
    # pylint: enable=W0212


def get_city(address_):
    while "  " in address_:
        address_ = address_.replace("  ", " ")

    if ", " not in address_:
        return address_

    address_parts = address_.split(", ")
    return address_parts[0].strip()


def get_country(address_):
    while "  " in address_:
        address_ = address_.replace("  ", " ")

    if ", " not in address_:
        return address_

    address_parts = address_.split(", ")
    return address_parts[-1].strip()


def get_state_or_province(address_):
    # for simplicity, we call them states
    # could also be provinces and French regions, for example

    while "  " in address_:
        address_ = address_.replace("  ", " ")

    if ", " not in address_:
        return address_

    address_parts = address_.split(", ")

    # Handle cities that are their own states or provinces

    if address_parts[0] in ["Berlin"]:
        return address_parts[0]

    if len(address_parts) > 2:
        state = address_parts[-2].strip()
        country = address_parts[-1].strip()

        if country == "USA" and state in us_states_and_territories:
            return us_states_and_territories[state]

        if country == "Canada" and state in canadian_provinces_and_territories:
            return canadian_provinces_and_territories[state]

        if country == "Australia" and state in australian_states_and_territories:
            return australian_states_and_territories[state]

        return state

    return None
