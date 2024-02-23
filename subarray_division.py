"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.
"""


def birthday(s: [int], d: int, m: int) -> int:
    size: int = len(s)
    num: int = 0
    temp: int

    for i in range(size):
        if ((i + m) <= size):
            temp = s[i]
            for j in range(1,m):
                temp += s[i+j]
            if temp == d:
                num += 1
    return num

if __name__ == '__main__':
    s: [int] = [2,2,1,3,2]
    d: int = 4
    m: int = 2
    result: int = birthday(s, d, m)
    print(result)
