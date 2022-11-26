def add_time(start, duration, day = None):
    ''' Time adder

    Takes a time "HH:MM AM" or "HH:MM PM", and a duration in HH:MM
    (optional) starting day of the week, case insensitive
    Returns the end time, (optional) day, and number of days later
    '''
    print (start, duration, day)
    time_in, ampm_in = start.split()
    hr_in, min_in = time_in.split(':')
    dur_hr, dur_min = duration.split(':')

    # First way, convert to float then calculate and convert back

    # second way, add mins (final mins = %60... and add // 60 to hrs)
    mins_add = int(min_in) + int(dur_min)
    mins =  str(mins_add % 60).zfill(2)

    hrs_add = int(hr_in) + int(dur_hr) + (mins_add // 60)
    hrs = hrs_add % 12  #TODO: should this say 00 or 12 at 12?
    new_time = str(hrs) + ':' + mins + ' '
    print('time added line 22: ', new_time)

    # need to work out AM or PM and append to new_time here.
    # 11:59AM -> 12:01PM
    # mins add = 59 + 2 = 61
    # mins = '01'
    # hrs_add = 11 + 0 + 1 == 12
    # hrs = 0
    # half days = 1

    half_days = hrs_add // 12
    print('half days ' + str(half_days))
    ampm =  None
    # flip AM/PM
    if half_days % 2: #if half_days is odd
        new_time += "PM" if ampm_in == "AM" else "AM" # could put the halfdays if in this line
    else:
        new_time += ampm_in

    # days_add accounts for adding half a day when its the evening
    days_add = int(half_days // 2 + 1) if (half_days and ampm_in == "PM") else int(half_days // 2)
    print('days add ' + str(days_add))

    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day:
        day_index_in = day_list.index(day[0].upper() + day[1:].lower())

    day_index = None
    if days_add >= 1:
        #TODO: take this if out of the days_add if, we should print it even if same day
        if day:
            # There's 7 days... We go up to sunday then start again
            day_index = (days_add - 6 + day_index_in) % 7 - 1
            new_time += (', ' + day_list[day_index])

        if days_add == 1:
            new_time += ' (next day)'

        if days_add > 1:
            new_time += (' (' + str(days_add) + ' days later)')

    # if half_days % 2: #if half_days is odd
    #     # TODO: this is wrong - the time should flip dependant on the actual time...
    #     ampm = "PM" if ampm_in == "AM" else "AM" # could put the halfdays if in this line
    #     if ( half_days // 2 ) > 0:
    #         if day:
    #             # calculate change in day
    #             day_index = (half_days * 2)
    #     #else:
    #          # day stays same
    #         # print extra days
    # else:
    #     ampm = ampm_in

    print(new_time)
    return new_time