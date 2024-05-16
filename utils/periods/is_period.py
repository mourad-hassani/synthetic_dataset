import re

def is_period(text):
    day_pattern = r'^P-?\d+D$'
    month_pattern = r'^P-?\d+M$'
    year_pattern = r'^P-?\d+Y$'
    week_pattern = r'^P-?\d+W$'

    day_pattern_i = r'^P-?\d+D/P-?\d+D$'
    month_pattern_i = r'^P-?\d+M/P-?\d+M$'
    year_pattern_i = r'^P-?\d+Y/P-?\d+Y$'
    week_pattern_i = r'^P-?\d+W/P-?\d+W$'

    day_pattern_n = r'^P-?\d+D-#\d+$'
    month_pattern_n = r'^P-?\d+M-#\d+$'
    year_pattern_n = r'^P-?\d+Y-#\d+$'
    week_pattern_n = r'^P-?\d+W-#\d+$'

    patterns = [day_pattern, month_pattern, year_pattern, week_pattern, day_pattern_i, month_pattern_i, year_pattern_i, week_pattern_i, day_pattern_n, month_pattern_n, year_pattern_n, week_pattern_n]
    patterns = "|".join(patterns)

    if re.match(pattern=patterns, string=text):
        return True, "Valid format"
    else:
        return False, "Invalid format"