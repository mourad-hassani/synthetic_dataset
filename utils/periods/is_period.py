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

    patterns_dicts = {day_pattern: "pd", month_pattern: "pm", year_pattern: "py", week_pattern: "pw", day_pattern_i: "pdi", month_pattern_i: "pmi", year_pattern_i: "pyi", week_pattern_i: "pwi", day_pattern_n: "pdn", month_pattern_n: "pmn", year_pattern_n: "pyn", week_pattern_n: "pwn"}
    patterns = [k for k, v in patterns_dicts.items()]

    for pattern in patterns:
        if re.match(pattern=pattern, string=text):
            return True, patterns_dicts[pattern]
    return False, "Invalid format"