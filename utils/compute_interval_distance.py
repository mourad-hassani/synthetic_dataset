def compute_interval_distance(interval1, interval2):
    # Sort the intervals so that the one with the smaller first element is assigned to x,
    # and the bigger one is assigned to y.
    x, y = sorted((interval1, interval2))
    
    # If x[1] lies between x[0] and y[0] (x[1] != y[0] but can be equal to x[0]),
    # then the ranges are not overlapping, and we return the difference of y[0] and x[1].
    # Otherwise, return 0.
    if x[0] <= x[1] < y[0] and all(y[0] <= y[1] for y in (interval1, interval2)):
        return y[0] - x[1]
    else:
        return 0