def add_time(start, duration, day=None):
    start_hrs = int(start[:-6])
    start_min = int(start[-5:-3])
    period = start[-2:]

    duration_hrs = int(duration[:-3])
    duration_min = int(duration[-2:])

    new_min = start_min + duration_min
    if new_min >= 60:
        new_min -= 60
        duration_hrs += 1
    
    new_hrs = start_hrs + duration_hrs

    return new_time