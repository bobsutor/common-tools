# -------------------------------------------------------------------------------------------------
# Common data used across all reports
# -------------------------------------------------------------------------------------------------

# cspell:ignore FUTURUM Aptos

from datetime import date
from datetime import datetime

# -------------------------------------------------------------------------------------------------
# Dates
# -------------------------------------------------------------------------------------------------

# REPORT_DATE = datetime.strptime("2025-04-03", "%Y-%m-%d").date()
REPORT_DATE = date.today()

TODAY = REPORT_DATE.strftime("%B %d, %Y").replace(" 0", " ")
TODAY_YY_MM_DD = REPORT_DATE.strftime("%Y-%m-%d")
THIS_YEAR = REPORT_DATE.strftime("%Y")

# -------------------------------------------------------------------------------------------------
# Global options
# -------------------------------------------------------------------------------------------------

FOR_FUTURUM = False
SHOW_CHART_LOGOS = False
SHOW_FIGURE_NUMBERS = False

CHART_PORTRAIT_MODE = True

LANDSCAPE_CHART_WIDTH = 1920
LANDSCAPE_CHART_HEIGHT = 1080

PORTRAIT_CHART_WIDTH = 1920
PORTRAIT_CHART_HEIGHT = 1920

if FOR_FUTURUM:
    CHART_PORTRAIT_MODE = False
    SHOW_FIGURE_NUMBERS = False

if CHART_PORTRAIT_MODE:
    CHART_WIDTH = PORTRAIT_CHART_WIDTH
    CHART_HEIGHT = PORTRAIT_CHART_HEIGHT
else:
    CHART_WIDTH = LANDSCAPE_CHART_WIDTH
    CHART_HEIGHT = LANDSCAPE_CHART_HEIGHT

OUR_COMPANY = "Sutor Group Intelligence and Advisory"

COPYRIGHT = f"Copyright © 2025 {OUR_COMPANY}"

DATA_FOLDER = "../../data/"
COMPANY_DATA_FOLDER = "../../data/company-data/"

YAHOO_PREFIX = "https://finance.yahoo.com/quote"

LINK_SYMBOL = "&#x1F517;"

QR_CODE = "input/images/SG-qr-code-crimson.png"

FEATURED_IMAGE_PATH = "input/images/copilot-quantum-ai-substack.png"

SUTOR_GROUP_LOGO_PATH = "input/images/SG-logo-Harvard-Crimson.jpg"
FUTURUM_LOGO_PATH = "input/images/futurum_logo.png"
FUTURUM_TRANS_LOGO_PATH = "input/images/futurum_logo_trans.png"

CSS_FILE = "css/sutor-group-report-style.css"

HARVARD_CRIMSON = "#A51C30"
BANANA_YELLOW = "#FFE135"
ROYAL_BLUE = "#0044B9"

FUTURUM_TEAL = "#007079"
FUTURUM_LIGHT_BLUE = "#00a8e8"
FUTURUM_RED = "#8f0040"
FUTURUM_BLUE = "#007ea7"

FUTURUM_COLORS = [FUTURUM_TEAL, FUTURUM_LIGHT_BLUE, FUTURUM_RED, FUTURUM_BLUE]

DISCLOSURE_FILE = "../../data/disclosures.html"
with open(DISCLOSURE_FILE, "rt", encoding="utf8") as input_file:
    THE_DISCLOSURES = " ".join(input_file.readlines())
    THE_DISCLOSURES = THE_DISCLOSURES.replace("\n", "")

while "  " in THE_DISCLOSURES:
    THE_DISCLOSURES = THE_DISCLOSURES.replace("  ", " ")

SUTOR_GROUP_FILE = "../../data/sutor-group.html"
with open(SUTOR_GROUP_FILE, "rt", encoding="utf8") as input_file:
    THE_SUTOR_GROUP = " ".join(input_file.readlines())
    THE_SUTOR_GROUP = THE_SUTOR_GROUP.replace("\n", "")

while "  " in THE_SUTOR_GROUP:
    THE_SUTOR_GROUP = THE_SUTOR_GROUP.replace("  ", " ")

COPYRIGHT_AND_LICENSE_FILE = "../../data/copyright-license-notice.html"
with open(COPYRIGHT_AND_LICENSE_FILE, "rt", encoding="utf8") as input_file:
    COPYRIGHT_AND_LICENSE = " ".join(input_file.readlines())
    COPYRIGHT_AND_LICENSE = COPYRIGHT_AND_LICENSE.replace("\n", "")

while "  " in COPYRIGHT_AND_LICENSE:
    COPYRIGHT_AND_LICENSE = COPYRIGHT_AND_LICENSE.replace("  ", " ")

FOOTER_DATE_STYLE = f"""
@media print {{

    @page {{

        @bottom-left {{
            content: '{TODAY}';
            font-family: Arial, Aptos, san-serif, "IBM Plex Sans";
            font-size: 9pt;
        }}
    }}
}}
"""
