import random
import datetime

def generate_random_date(start_year, end_year):
    rand_int = random.randint(0, 4)

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
    else:
        times = ["MO", "NI"]
        return str(random_date.strftime("%Y-%m-%d") + f"T{times[random.randint(0, 1)]}")