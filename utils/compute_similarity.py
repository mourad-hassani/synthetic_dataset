from utils.dates.is_date import is_date
from utils.dates.is_in import is_in
from utils.dates.compute_distance_dates import compute_distance_dates_same_type, compute_distance_dates

def compute_similarity(first_date, second_date):
    first_is_date, first_date_type = is_date(first_date)
    second_is_date, second_date_type = is_date(second_date)
    if first_is_date and second_is_date:
        if first_date == second_date:
            return 1.0
        elif first_date_type == second_date_type:
            distance = compute_distance_dates_same_type(first_date=first_date, second_date=second_date, date_type=first_date_type)
            distance = distance**2 if distance < 100 else distance
            return 0.4 / distance
        elif first_date_type != second_date_type and is_in(first_date=first_date, first_date_type=first_date_type, second_date=second_date, second_date_type=second_date_type):
            return 0.5
        else:
            distance = compute_distance_dates(first_date, first_date_type, second_date, second_date_type)
            distance = distance**2 if distance < 100 else distance
            return 0.01 / distance
    else:
        raise ValueError(f"first_date: {first_date}, second_date: {second_date}")