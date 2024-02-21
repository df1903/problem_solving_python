"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
 Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:
    The red region denotes the house, where s is the start point, and t is the endpoint.
    The apple tree is to the left of the house, and the orange tree is to its right.

    Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.

    When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis.
    *A negative value of d means the fruit fell  d units to the tree's left, and a positive value of d means it falls d units to the tree's right. *


    Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t )?
"""

def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: [int], oranges: [int]):
    fruits = [0,0]
    for i in apples:
        if ((a + i) >= s) and ((a + i) <= t):
            fruits[0] += 1
    for j in oranges:
        if ((b+j) >= s) and ((b+j) <= t):
            fruits[1]+=1
    for k in fruits:
        print(k)


if __name__ == '__main__':
    s: int = 7
    t: int = 10
    a: int = 4
    b:int = 12
    apples: [int] = [2,3,-4]
    oranges: [int] = [3,-2,-4]
    countApplesAndOranges(s, t, a, b, apples, oranges)
