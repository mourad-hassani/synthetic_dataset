from utils.extract_integers import extract_integers
from utils.compute_interval_distance import compute_interval_distance

def compute_similarity_periods(first_period, first_period_type, second_period, second_period_type):
    if first_period_type != second_period_type:
        return 0.0
    elif first_period == second_period:
        return 1.0
    else:
        first_integers, second_integers = extract_integers(first_period), extract_integers(second_period)
        if len(first_integers) == 1:
            distance = abs(first_integers[0] - second_integers[0])
            return 0.5 / distance**2
        else:
            distance = compute_interval_distance(first_integers, second_integers)
            if distance == 0:
                return 0.8
            else:
                return 0.5 / distance**2