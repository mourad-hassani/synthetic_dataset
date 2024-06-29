from utils.mappings.date_to_text import date_to_text
from utils.mappings.period_to_text import period_to_text
from utils.mappings.offset_to_text import offset_to_text
from utils.mappings.ref_to_text import ref_to_text
from utils.mappings.interval_to_text import interval_to_text
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.offsets.is_offset import is_offset
from utils.refs.is_ref import is_ref
from utils.intervals.is_interval import is_interval

def expression_to_text(annotation):
    if is_date(annotation)[0]:
        return date_to_text(annotation)
    if is_period(annotation)[0]:
        return period_to_text(annotation)
    if is_offset(annotation)[0]:
        return offset_to_text(annotation)
    if is_ref(annotation)[0]:
        return ref_to_text(annotation)
    if is_interval(annotation)[0]:
        return interval_to_text(annotation)
    
    return None