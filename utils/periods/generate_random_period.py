import random
from utils.extract_integers import extract_integers

first_type = [("P", "D"), ("P", "W"), ("P", "M"), ("P", "Y")]
second_type = ["P1D-#", "P1W-#", "P1M-#", "P1Y-#"]
third_type = [("P", "D/P", "D"), ("P", "W/P", "W"), ("P", "M/P", "M"), ("P", "Y/P", "Y")]

def generate_random_period():
    rand_int = random.randint(0, 2)
    if rand_int == 0:
        rand_int = random.randint(0, 3)
        rand_per = random.randint(-10, 10)
        while rand_per == 0:
            rand_per = random.randint(-10, 10)
        return first_type[rand_int][0] + str(rand_per) + first_type[rand_int][1]
    elif rand_int == 1:
        rand_int = random.randint(0, 3)
        return second_type[rand_int] + str(random.randint(1, 10))
    elif rand_int == 2:
        rand_int = random.randint(0, 3)
        rand_per = random.randint(1, 10)
        rand_per1 = random.randint(rand_per + 1, rand_per + 10)
        return third_type[rand_int][0] + str(rand_per) + third_type[rand_int][1] + str(rand_per1) + third_type[rand_int][2]

def generate_close_random_period(period, type):
    integers = extract_integers(period)
    if type == "pd":
        return f"P{random.randint(integers[0]-10, integers[0]+10)}D"
    elif type == "pw":
        return f"P{random.randint(integers[0]-10, integers[0]+10)}W"
    elif type == "pm":
        return f"P{random.randint(integers[0]-10, integers[0]+10)}M"
    elif type == "py":
        return f"P{random.randint(integers[0]-10, integers[0]+10)}Y"
    elif type == "pdn":
        return f"P1D-#{random.randint(max(1, integers[0]-10), integers[0]+10)}"
    elif type == "pwn":
        return f"P1W-#{random.randint(max(1, integers[0]-10), integers[0]+10)}"
    elif type == "pmn":
        return f"P1M-#{random.randint(max(1, integers[0]-10), integers[0]+10)}"
    elif type == "pyn":
        return f"P1Y-#{random.randint(max(1, integers[0]-10), integers[0]+10)}"
    elif type == "pdi":
        rand_per = random.randint(max(1, integers[0]-10), integers[0]+10)
        rand_per1 = random.randint(rand_per+1, max(rand_per+1, integers[1] + 10))
        return f"P{rand_per}D/P{rand_per1}D"
    elif type == "pwi":
        rand_per = random.randint(max(1, integers[0]-10), integers[0]+10)
        rand_per1 = random.randint(rand_per+1, max(rand_per+1, integers[1] + 10))
        return f"P{rand_per}W/P{rand_per1}W"
    elif type == "pmi":
        rand_per = random.randint(max(1, integers[0]-10), integers[0]+10)
        rand_per1 = random.randint(rand_per+1, max(rand_per+1, integers[1] + 10))
        return f"P{rand_per}M/P{rand_per1}M"
    elif type == "pyi":
        rand_per = random.randint(max(1, integers[0]-10), integers[0]+10)
        rand_per1 = random.randint(rand_per+1, max(rand_per+1, integers[1] + 10))
        return f"P{rand_per}Y/P{rand_per1}Y"