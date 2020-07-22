"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""

def what_to_print(sec, formula, name):
    return None if formula == 0 else str(formula) + (name + 's' if formula != 1 else name)

def format_duration(sec):
    if sec == 0:
        return 'now'
    years_formula = sec//31536000
    days_formula = (sec%31536000)//86400
    hours_formula = (sec%86400)//3600
    minutes_formula = (sec%3600)//60
    seconds_formula = sec%60

    result =[]
    
    result.extend([what_to_print(sec, years_formula, ' year')])
    result.extend([what_to_print(sec, days_formula, ' day')])
    result.extend([what_to_print(sec, hours_formula, ' hour')])
    result.extend([what_to_print(sec, minutes_formula, ' minute')])
    result.extend([what_to_print(sec, seconds_formula, ' second')])

    result = [value for value in result if value != None]
    if len(result) > 1:
        result[-2] = str(result[-2] + ' and '+ result[-1])
        result.pop() # delete last element
    return print(', '.join(result))

seconds = 666
format_duration(3662)