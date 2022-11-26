def add_time(start, duration, day = None):
    ''' Time adder

    Takes a time "HH:MM AM" or "HH:MM PM", and a duration in HH:MM
    (optional) starting day of the week, case insensitive
    Returns the end time, (optional) day, and number of days later
    '''
    # Get input data
    time_in, ampm_in = start.split()
    hr_in, min_in = time_in.split(':')
    dur_hr, dur_min = duration.split(':')

    # Calculate final minutes
    mins_add = int(min_in) + int(dur_min)
    mins =  str(mins_add % 60).zfill(2)

    # Calculate final hours
    hrs_add = int(hr_in) + int(dur_hr) + (mins_add // 60)
    hrs = hrs_add % 12 if (hrs_add % 12) > 0 else 12
    new_time = str(hrs) + ':' + mins + ' '

    half_days = hrs_add // 12

    # flip AM/PM
    if half_days % 2: #if half_days is odd
        new_time += "PM" if ampm_in == "AM" else "AM" # could put the halfdays if in this line
    else:
        new_time += ampm_in

    # Calculate (optional) day name
    days_add = int(half_days // 2 + 1) if (half_days and ampm_in == "PM") else int(half_days // 2)

    if day:
        day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index_in = day_list.index(day[0].upper() + day[1:].lower())
        # There's 7 days... We go up to sunday then start again
        day_index = (days_add - 6 + day_index_in) % 7 - 1
        new_time += (', ' + day_list[day_index])

    # Calculate number of days passed
    if days_add == 1:
        new_time += ' (next day)'
    elif days_add > 1:
        new_time += (' (' + str(days_add) + ' days later)')

    return new_time