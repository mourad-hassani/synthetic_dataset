import random
import datetime
from utils.dates.to_explicit_date import to_explicit_date

def generate_random_date(start_year, end_year):
    
    rand_int = random.randint(0, 3)

    start_date = datetime.datetime(start_year, 1, 1)
    end_date = datetime.datetime(end_year, 12, 31)
    
    delta = end_date - start_date
    
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    
    if rand_int == 0:
        return random_date.strftime("%Y")
    
    elif rand_int == 1:
        seasons = ["SU", "WI", "FA", "SP"]
        
        return str(random_date.strftime("%Y") + f"-{seasons[random.randint(0, 3)]}")
    
    elif rand_int == 2:
        return random_date.strftime("%Y-%m")
    
    elif rand_int == 3:
        return random_date.strftime("%Y-%m-%d")
    
def generate_random_close_date(date):
    explicit_date = to_explicit_date(date)

    first_date = explicit_date[0]
    second_date = first_date

    if len(explicit_date) > 1:
        second_date = explicit_date[1]
    
    start_year, start_month, start_day = list(map(int, first_date.split("-")))
    end_year, end_month, end_day = list(map(int, second_date.split("-")))

    start_date = datetime.datetime(start_year, start_month, start_day) + datetime.timedelta(days=-5)
    end_date = datetime.datetime(end_year, end_month, end_day) + datetime.timedelta(days=5)

    start_year, start_month, start_day = start_date.year, start_date.month, start_date.day
    end_year, end_month, end_day = end_date.year, end_date.month, end_date.day
    
    return generate_random_date_full(start_year, end_year, start_month, end_month, start_day, end_day)
    
def generate_random_date_full(start_year, end_year, start_month = None, end_month = None, start_day = None, end_day = None):
    
    if start_day and end_day and start_month and end_month:
        start_date = datetime.datetime(start_year, start_month, start_day)
        end_date = datetime.datetime(end_year, end_month, end_day)
    
    else:
        start_date = datetime.datetime(start_year, 1, 1)
        end_date = datetime.datetime(end_year, 12, 31)
    
    delta = end_date - start_date
    
    random_days = random.randint(0, abs(delta.days))
    random_date = start_date + datetime.timedelta(days=random_days)
    
    return random_date.strftime("%Y-%m-%d")