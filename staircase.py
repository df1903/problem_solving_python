"""Staircase detail

This is a staircase of size n = 4:
   #
  ##
 ###
####
"""

def staircase(n : int):
    for i in range(n):
        for j in range(n):
            if j+i < (n-1):
                print(' ', end='')
            else:
                print("#", end='')
        print()

if __name__ == '__main__':
    n: int = int(input('Enter the size of the staircase: '))
    staircase(n)