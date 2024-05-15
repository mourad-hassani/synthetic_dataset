import re

def is_date(text):
    yyyy_pattern = r'^\d{4}$'
    yyyy_mm_pattern = r'^\d{4}-\d{2}$'
    yyyy_mm_dd_pattern = r'^\d{4}-\d{2}-\d{2}$'
    yyyy_mm_dd_t_pattern = r'^\d{4}-\d{2}-\d{2}T(?:MO|NI)$'
    yyyy_s_pattern = r'^\d{4}-(?:SU|WI|FA|SP)$'

    if re.match(r"^\d{4}", text):
        if int(text[:4]) < 1900:
            return False, "Less than 1900"

    if re.match(yyyy_mm_dd_pattern, text):
        return True, "yyyy-mm-dd"
    elif re.match(yyyy_mm_pattern, text):
        return True, "yyyy-mm"
    elif re.match(yyyy_pattern, text):
        if int(text) >= 1900:
            return True, "yyyy"
        else:
            return False, "Not a year"
    elif re.match(yyyy_mm_dd_t_pattern, text):
        return True, "yyyy-mm-dd-t"
    elif re.match(yyyy_s_pattern, text):
        return True, "yyyy-s"
    else:
        return False, "Invalid format"