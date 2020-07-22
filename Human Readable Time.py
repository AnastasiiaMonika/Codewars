"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

from datetime import timedelta
def make_readable(sec):
    return str(timedelta(seconds=sec))

def make_readable_manual(seconds):
    return '%02i:%02i:%02i' %(seconds//3600, (seconds%3600)//60, seconds%60)

seconds = 666
print(make_readable_manual(seconds))