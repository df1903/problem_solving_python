"""
A jail has a number of prisoners and a number of treats to pass out to them.
Their jailer decides the fairest way to divide the treats is to seat
the prisoners around a circular table in sequentially numbered chairs.
A chair number will be drawn from a hat. Beginning with the prisoner in that chair,
one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful.
Determine the chair number occupied by the prisoner who will receive that candy.

Example

n = 4
m = 6
s = 2

There are 4 prisoners, 6 pieces of candy and distribution starts at chair 2.
The prisoners arrange themselves in seats numbered 1 to 4.
Prisoners receive candy at positions 2, 3, 4, 1, 2, 3. The prisoner to be warned sits in chair number 3.
2 3 4 5 1
"""


def save_the_prisoner(prisoners: int, sweets: int, start) -> int:
    warning: int = (sweets + start - 1) % prisoners

    if warning == 0:
        warning = prisoners

    return warning


if __name__ == '__main__':
    show: int = save_the_prisoner(4, 6, 2)
    print(show)
