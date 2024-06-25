"""
Two cats and a mouse are at various positions on a line. You will be given their starting positions.
Your task is to determine which cat will reach the mouse first,
assuming the mouse does not move and the cats travel at equal speed.
If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given q queries in the form of x, y, and z
representing the respective positions for cats A and B, and for mouse C.
Complete the function cat_and_mouse to return the appropriate answer to each query, which will be printed on a new line.

If cat A catches the mouse first, print Cat A.
If cat B catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

Example

The cats are at 2 positions (Cat A) and 5 (Cat B), and the mouse is at position 4.
 Cat B, at position 5 will arrive first since it is only unit away while the other is units away. Return 'Cat B'.
"""


def cat_and_mouse(x: int, y: int, z: int):
    x_to_z: int = abs(x-z)
    y_to_z: int = abs(y-z)

    if x_to_z < y_to_z:
        return "Cat A"
    if y_to_z < x_to_z:
        return "Cat B"

    return "Mouse C"


if __name__ == '__main__':
    print(cat_and_mouse(1, 3, 2))
