import random
from utils.extract_integers import extract_integers

def generate_random_offset():
    rand_int = random.randint(1, 30)
    is_negative = bool(random.getrandbits(1))
    rand_format = random.randint(0, 7)

    if is_negative:
        rand_int *= -1
    
    if rand_format == 0:
        return f"OFFSET P{rand_int}D"
    elif rand_format == 1:
        return f"OFFSET P{rand_int}W"
    elif rand_format == 2:
        return f"OFFSET P{rand_int}M"
    elif rand_format == 3:
        return f"OFFSET P{rand_int}Y"
    elif rand_format == 4:
        return f"THIS P{abs(rand_int)}D OFFSET P{rand_int}D"
    elif rand_format == 5:
        return f"THIS P{abs(rand_int)}W OFFSET P{rand_int}W"
    elif rand_format == 6:
        return f"THIS P{abs(rand_int)}M OFFSET P{rand_int}M"
    elif rand_format == 7:
        return f"THIS P{abs(rand_int)}Y OFFSET P{rand_int}Y"

def generate_close_random_offset(value, type):
    if type in ["d", "w", "m", "y"]:
        value = extract_integers(value)[0]
    else:
        value = extract_integers(value)[1]
        
    is_negative = True if value < 0 else False
    value = abs(value)
    min_value = max(1, value - 10)
    max_value = min(30, value + 10)
    rand_int = random.randint(min_value, max_value)

    if is_negative:
        rand_int *= -1
    
    if type == "d":
        return f"OFFSET P{rand_int}D"
    elif type == "w":
        return f"OFFSET P{rand_int}W"
    elif type == "m":
        return f"OFFSET P{rand_int}M"
    elif type == "y":
        return f"OFFSET P{rand_int}Y"
    elif type == "td":
        return f"THIS P{abs(rand_int)}D OFFSET P{rand_int}D"
    elif type == "tw":
        return f"THIS P{abs(rand_int)}W OFFSET P{rand_int}W"
    elif type == "tm":
        return f"THIS P{abs(rand_int)}M OFFSET P{rand_int}M"
    elif type == "ty":
        return f"THIS P{abs(rand_int)}Y OFFSET P{rand_int}Y"