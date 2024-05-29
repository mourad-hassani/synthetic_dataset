from utils.dates.compute_similarity_dates import compute_similarity_dates
from utils.periods.compute_similarity_periods import compute_similarity_periods
from utils.offsets.compute_similarity_offsets import compute_similarity_offsets
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.offsets.is_offset import is_offset
from utils.dates.compute_similarity_dates import compute_similarity_dates_intervals
from utils.offsets.compute_similarity_offsets import compute_offset_in_days
from utils.dates.to_explicit_date import to_explicit_date

def compute_similarity_expressions(first_expression, second_expression, first_current_date, second_current_date):
    if is_date(first_expression)[0]:
        if is_date(second_expression)[0]:
            return compute_similarity_dates(first_expression, second_expression)
        elif is_offset(second_expression)[0]:
            offset_in_days = compute_offset_in_days(second_expression, is_offset(second_expression)[1], second_current_date)
            return compute_similarity_dates_intervals(to_explicit_date(first_expression), offset_in_days)
        else:
            return 0.0
    elif is_period(first_expression)[0]:
        if is_period(second_expression)[0]:
            return compute_similarity_periods(first_expression, is_period(first_expression)[1], second_expression, is_period(second_expression)[1])
        else:
            return 0.0
    elif is_offset(first_expression)[0]:
        if is_offset(second_expression)[0]:
            return compute_similarity_offsets(first_expression, is_offset(first_expression)[1], second_expression, is_offset(second_expression)[1], first_current_date, second_current_date)
        elif is_date(second_expression)[0]:
            offset_in_days = compute_offset_in_days(first_expression, is_offset(first_expression)[1], first_current_date)
            return compute_similarity_dates_intervals(to_explicit_date(second_expression), offset_in_days)
        else:
            return 0.0