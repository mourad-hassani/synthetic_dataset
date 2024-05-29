from utils.dates.generate_random import generate_random_date
from utils.periods.generate_random_period import generate_random_period, generate_close_random_period
from utils.offsets.generate_random_offset import generate_random_offset, generate_close_random_offset
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.offsets.is_offset import is_offset
from utils.dates.dates_settings import START_DATE, END_DATE
import random

def generate_random_temporal_expression():
    random_int = random.randint(0, 2)
    if random_int == 0:
        return generate_random_date(START_DATE, END_DATE)
    elif random_int == 1:
        return generate_random_period()
    else:
        return generate_random_offset()

def generate_close_random_temporal_expression(expression):
    if is_date(expression)[0]:
        year = int(expression.split("-")[0])
        if START_DATE < year < END_DATE:
            start_year = year - 3
            end_year = year + 3
        else:
            start_year = START_DATE
            end_year = END_DATE
        return generate_random_date(start_year, end_year)
    if is_period(expression)[0]:
        return generate_close_random_period(expression, is_period(expression)[1])
    if is_offset(expression)[0]:
        return generate_close_random_offset(expression, is_offset(expression)[1])