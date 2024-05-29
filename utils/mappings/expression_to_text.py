from utils.mappings.date_to_text import date_to_text
from utils.mappings.period_to_text import period_to_text
from utils.mappings.offset_to_text import offset_to_text
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.offsets.is_offset import is_offset

def expression_to_text(annotation):
    if is_date(annotation)[0]:
        return date_to_text(annotation)
    if is_period(annotation)[0]:
        return period_to_text(annotation)
    if is_offset(annotation)[0]:
        return offset_to_text(annotation)
    return None