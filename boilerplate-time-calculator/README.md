# Time Calculator

The function named add_time takes in two required parameters and one optional parameter:

* Start time in the 12-hour clock format (ending in AM or PM)
* Duration time that indicates the number of hours and minutes
* (optional) Starting day of the week, case insensitive

The function adds the duration time to the start time and returns the result.

If the result will be the next day, it shows (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result.

## Usage

    add_time("3:00 PM", "3:10")
    # Returns: 6:10 PM

    add_time("11:30 AM", "2:32", "Monday")
    # Returns: 2:02 PM, Monday

    add_time("11:43 AM", "00:20")
    # Returns: 12:03 PM

    add_time("10:10 PM", "3:30")
    # Returns: 1:40 AM (next day)

    add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)

    add_time("6:30 PM", "205:12")
    # Returns: 7:42 AM (9 days later)

## Testing

The unit tests are in test_module.py
