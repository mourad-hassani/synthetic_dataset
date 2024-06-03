from utils.dates.compute_similarity_dates import compute_similarity_dates_intervals
from utils.periods.compute_similarity_periods import compute_similarity_periods
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.dates.compute_similarity_dates import compute_similarity_dates_intervals
from utils.offsets.offset_to_date import offset_to_date
from utils.refs.ref_to_date import ref_to_date
from utils.dates.to_explicit_date import to_explicit_date
from utils.refs.compute_similarity_refs import compute_similarity_refs

def compute_similarity_expressions(first_expression, second_expression, first_current_date, second_current_date):
    if is_period(first_expression)[0]:
        if is_period(second_expression)[0]:
            return compute_similarity_periods(first_expression, is_period(first_expression)[1], second_expression, is_period(second_expression)[1])
        else:
            return 0.0
    
    refs = ["TMO", "TEV", "TNI"]
    
    if first_expression in refs:
        if second_expression in refs:
            return compute_similarity_refs(first_expression, second_expression)
        else:
            return 0.0
        
    first_is_date = False
    second_is_date = False

    if is_date(first_expression)[0]:
        first_is_date = True
        first_expression = to_explicit_date(first_expression)
    elif first_expression_date := offset_to_date(first_expression, first_current_date):
        first_is_date = True
        first_expression = first_expression_date
    elif first_expression_date := ref_to_date(first_expression, first_current_date):
        first_is_date = True
        first_expression = first_expression_date

    if is_date(second_expression)[0]:
        second_is_date = True
        second_expression = to_explicit_date(second_expression)
    elif second_expression_date := offset_to_date(second_expression, second_current_date):
        second_is_date = True
        second_expression = second_expression_date
    elif second_expression_date := ref_to_date(second_expression, second_current_date):
        second_is_date = True
        second_expression = second_expression_date

    if first_is_date and second_is_date:
        return compute_similarity_dates_intervals(first_expression, second_expression)
    else:
        return 0.0