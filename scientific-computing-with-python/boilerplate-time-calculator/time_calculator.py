def next_day(day, days_gone):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    position = days.index(day)

    position += days_gone
    while position > 6:
        position -= 7
    
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

    new_min = new_min if len(str(new_min)) == 2 else "0" + str(new_min) 

    if period == "AM":
        while new_hrs >= 24:
            new_hrs -= 24
            days_gone += 1
        if new_hrs >= 12:
            period = "PM"
            if new_hrs >= 13:
                new_hrs -= 12
    
    elif period == "PM":
        while new_hrs >= 24:
            new_hrs -= 24
            days_gone += 1
        if new_hrs >= 12:
            period = "AM"
            days_gone += 1
            if new_hrs >= 13:
                new_hrs -= 12

    
    if actual_day != None:
        actual_day = actual_day.title()
        new_day = next_day(actual_day, days_gone)
        new_time = f"{new_hrs}:{new_min} {period}, {new_day}"
    else:
        new_time = f"{new_hrs}:{new_min} {period}"
    
    if days_gone == 1:
        new_time += " (next day)"
    elif days_gone > 1:
        new_time += f" ({days_gone} days later)"

    return new_time
