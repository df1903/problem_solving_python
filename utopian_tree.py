"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring.
How tall will the tree be after n growth cycles?

For example, if the number of growth cycles is n = 5, the calculations are as follows:

Period  Height
0          1
1          2
2          3
3          6
4          7
5          14
"""


def utopian_tree(n: int) -> int:
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height = 2 * height
        else:
            height += 1
    return height


if __name__ == '__main__':
    print(utopian_tree(5))
