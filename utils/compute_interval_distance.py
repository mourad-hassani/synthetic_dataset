from datetime import datetime

def compute_interval_distance(interval1, interval2):
    x, y = sorted((interval1, interval2))

    if x[0] <= x[1] < y[0] and all(y[0] <= y[1] for y in (interval1, interval2)):
        return y[0] - x[1]
    else:
        return 0

def compute_interval_distance_date(interval1, interval2):
    interval1 = [days_since_base(interval1[0]), days_since_base(interval1[1])]
    interval2 = [days_since_base(interval2[0]), days_since_base(interval2[1])]

    interval1 = sorted(interval1)
    interval2 = sorted(interval2)
    
    start1, end1 = interval1
    start2, end2 = interval2

    if end1 >= start2 and end2 >= start1:
        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)
        overlap_length = overlap_end - overlap_start
        union_start = min(start1, start2)
        union_end = max(end1, end2)
        union_length = union_end - union_start
        overlap_fraction = overlap_length / union_length
        return overlap_fraction
    
    distance = max(start2 - end1, start1 - end2)
    return distance

def days_since_base(date_string, base_date_string="1000-01-01"):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    base_date = datetime.strptime(base_date_string, "%Y-%m-%d")
    
    days_difference = (date - base_date).days
    return days_difference