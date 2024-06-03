from utils.dates.generate_random_date import generate_random_date
from utils.periods.generate_random_period import generate_random_period, generate_close_random_period
from utils.offsets.generate_random_offset import generate_random_offset, generate_close_random_offset
from utils.refs.generate_random_ref import generate_random_ref
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.offsets.is_offset import is_offset
from utils.refs.is_ref import is_ref
from utils.dates.dates_settings import START_DATE, END_DATE
import numpy as np
import random

def generate_random_temporal_expression():
    random_int = np.random.choice(np.arange(4), p=np.array([0.4, 0.25, 0.3, 0.05]))
    if random_int == 0:
        return generate_random_date(START_DATE, END_DATE)
    if random_int == 1:
        return generate_random_period()
    if random_int == 2:
        return generate_random_offset()
    if random_int == 3:
        return generate_random_ref()

def generate_close_random_temporal_expression(expression, current_date):
    rand_bool = bool(random.getrandbits(1))

    if is_date(expression)[0]:
        year = int(expression.split("-")[0])
        return generate_random_date(year, year)
    if is_period(expression)[0]:
        return generate_close_random_period(expression, is_period(expression)[1])
    if is_offset(expression)[0]:
        if rand_bool:
            return generate_close_random_offset(expression, is_offset(expression)[1])
        else:
            year = int(current_date.split("-")[0])
            return generate_random_date(year, year)
    if is_ref(expression)[0]:
        if rand_bool:
            return generate_random_ref()
        else:
            year = int(current_date.split("-")[0])
            return generate_random_date(year, year)