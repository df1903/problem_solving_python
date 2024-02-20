"""Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. """

def timeConversion(s: str) -> str:
    if s[-2:] == 'AM':
        if s[:2] == '12':
            s = '00'+ s[2:]
    else:
        if s[:2] != '12':
            hour: int = int(s[:2]) + 12
            s = str(hour) + s[2:]
    s = s[:-2]
    return s

if __name__ == '__main__':
    time = '12:05:45PM'
    result = timeConversion(time)
    print(result)
