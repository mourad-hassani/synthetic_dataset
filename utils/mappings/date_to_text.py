import re
from utils.dates.is_date import is_date

integer_to_month = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december",
}

symbol_to_season = {
    "FA": "fall",
    "SP": "spring",
    "WI": "winter",
    "SU": "summer",
}

def date_to_text(annotation):
    is_date_bool, date_format = is_date(annotation)
    if is_date_bool:
        if date_format == "yyyy":
            return annotation
        elif date_format == "yyyy-s":
            year = annotation.split("-")[0]
            season = annotation.split("-")[-1]
            season = symbol_to_season[season]
            return f"{season} of {year}"
        elif date_format == "yyyy-mm":
            year = annotation.split("-")[0]
            month = annotation.split("-")[-1]
            month = integer_to_month[int(month)]
            return f"{month} {year}"
        elif date_format == "yyyy-mm-dd":
            year = annotation.split("-")[0]
            month = annotation.split("-")[1]
            day = annotation.split("-")[-1]
            month = integer_to_month[int(month)]
            return f"{day} {month} {year}"
    return None