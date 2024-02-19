"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers. """

def miniMaxSum(arr: [int]):
    min_num:float = float('inf')
    max_num: float = -float('inf')
    sum: int = 0

    for x in arr:
        if x > max_num:
            max_num = x
        if x < min_num:
            min_num = x
        sum += x
    print(sum - max_num, sum - min_num)

if __name__ == '__main__':
    arr: [int] = [5,4,3,2,1]

    miniMaxSum(arr)
