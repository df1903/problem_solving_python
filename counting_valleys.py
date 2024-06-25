"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps,
 for every step it was noted if it was an uphill, U, or a downhill, D step.
 Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude.
  We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea
 level and ending with a step down to sea level.

A valley is a sequence of consecutive steps below sea level, starting with a step down
 from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

"""


def counting_valleys(steps: int, path: str):
    valleys: int = 0
    current_level: int = 0
    for direction in path:
        previous_level = current_level
        if direction == 'U':
            current_level += 1
        if direction == 'D':
            current_level -= 1
            if current_level == -1 and previous_level == 0:
                valleys += 1

    return valleys


if __name__ == '__main__':
    path_p: str = 'UDDDUDUU'
    steps_p: int = len(path_p)
    print(counting_valleys(steps_p, path_p))
