"""
A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights,
and the characters have a maximum height they can jump.
There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose.
How many doses of the potion must the character take to be able to jump all of the hurdles.
If the character can already clear all of the hurdles, return 0.

Example
height = [1, 2, 3, 3, 2]

The character can jump 1 unit high initially and must take  3 - 1 = 2
doses of potion to be able to jump all of the hurdles.
"""


def hurdle_race(jump: int, height: list[int]) -> int:
    difference: int = max(height) - jump
    if difference > 0:
        return difference
    return 0


if __name__ == '__main__':
    height_p = [1, 2, 3, 3, 2]
    jump_p = 2
    result = hurdle_race(jump_p, height_p)
    print(result)
