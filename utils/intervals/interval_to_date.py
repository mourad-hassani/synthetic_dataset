from utils.intervals.is_interval import is_interval
from utils.dates.to_explicit_date import to_explicit_date

def interval_to_date(annotation):
    if is_interval(annotation)[0]:
        dates = annotation.split(",")
        return [to_explicit_date(dates[0])[0], to_explicit_date(dates[1])[-1]] 
    return None
