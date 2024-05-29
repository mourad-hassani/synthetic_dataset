from utils.dates.generate_random import generate_random_date
from utils.periods.generate_random_period import generate_random_period
from utils.offsets.generate_random_offset import generate_random_offset
import random

def generate_random_temporal_expression():
    random_int = random.randint(0, 2)
    if random_int == 0:
        return generate_random_date(1900, 2024)
    elif random_int == 1:
        return generate_random_period()
    else:
        return generate_random_offset()