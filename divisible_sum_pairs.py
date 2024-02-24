"""Given an array of integers and a positive integer k, determine the number of (i,j) pairs where and ar[i] + ar[j] is divisible by. k"""

def divisibleSumPairs(n: int, k: int, ar: [int]) -> int:
    num: int = 0
    for i in range(n):
        for j in range(i+1,n):
            if  ((ar[i] + ar[j]) % k == 0):
                num += 1
    return num

if __name__ == '__main__':
    ar: int = [1, 3, 2, 6, 1, 2]
    k: int = 3
    n: int = len(ar)

    print(divisibleSumPairs(n, k, ar))