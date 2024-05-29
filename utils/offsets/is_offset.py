import re

def is_offset(text):
    day_offset_pattern = r'^OFFSET P(-?\d+)D$'
    week_offset_pattern = r'^OFFSET P(-?\d+)W$'
    month_offset_pattern = r'^OFFSET P(-?\d+)M$'
    year_offset_pattern = r'^OFFSET P(-?\d+)Y$'

    this_day_offset_pattern = r"^THIS P(-?\d+)D OFFSET P(-?\d+)D$"
    this_week_offset_pattern = r"^THIS P(-?\d+)W OFFSET P(-?\d+)W$"
    this_month_offset_pattern = r"^THIS P(-?\d+)M OFFSET P(-?\d+)M$"
    this_year_offset_pattern = r"^THIS P(-?\d+)Y OFFSET P(-?\d+)Y$"

    patterns_dicts = {day_offset_pattern: "d", week_offset_pattern: "w", month_offset_pattern: "m", year_offset_pattern: "y", this_day_offset_pattern: "td", this_week_offset_pattern: "tw", this_month_offset_pattern: "tm", this_year_offset_pattern: "ty"}
    patterns = [k for k, v in patterns_dicts.items()]

    for pattern in patterns:
        if re.match(pattern=pattern, string=text):
            return True, patterns_dicts[pattern]
    return False, "Invalid format"