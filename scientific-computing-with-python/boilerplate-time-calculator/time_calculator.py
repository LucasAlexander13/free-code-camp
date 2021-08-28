def next_day(day, days_gone):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    position = days.index(day)

    position += days_gone
    while position > 6:
        position - 7
    
    return days[position]

def add_time(start, duration, actual_day=None):
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
    days_gone = 0

    if period == "AM":
        while new_hrs >= 24:
            new_hrs -= 24
            days_gone += 1
        if new_hrs >= 13:
            new_hrs -= 12
            period = "PM"
    
    elif period == "PM":
        while new_hrs >= 24:
            new_hrs -= 24
            days_gone += 1
        if new_hrs >= 13:
            new_hrs -= 12
            days_gone += 1
            period = "AM"
    
    pass_days = ""
    if days_gone == 1:
        pass_days = "(next day)"
    elif days_gone > 1:
        pass_days = f"{days_gone} days later"
    
    if actual_day != None:
        actual_day = actual_day.title()
        new_day = next_day(actual_day, days_gone)
        return new_time
    else: