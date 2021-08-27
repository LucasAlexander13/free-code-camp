def add_time(start, duration, day=None):
    start_hrs = int(start[:-6])
    start_min = int(start[-5:-3])
    period = start[-2:]

    duration_hrs = duration[:-3]
    duration_min = duration[-2:]

    return new_time