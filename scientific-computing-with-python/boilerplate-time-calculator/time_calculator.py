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
    days = 0

    if period == "AM":
        while new_hrs >= 24:
            new_hrs -= 24
            days += 1
        if new_hrs >= 13:
            new_hrs -= 12
            period = "PM"
    
    elif period == "PM":
        while new_hrs >= 24:
            new_hrs -= 24
            days += 1
        if new_hrs >= 13:
            new_hrs -= 12
            days += 1
            period = "AM"
    
    pass_days = ""
    if days == 1:
        pass_days = "(next day)"
    elif days > 1:
        pass_days = f"{days} days later"
    

    return new_time