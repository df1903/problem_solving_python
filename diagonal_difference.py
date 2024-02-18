"""Given a square matrix, calculate the absolute difference between the sums of its diagonals. """

def diagonalDifference(arr) -> int:
    diagonal_1: int = 0
    diagonal_2: int = 0
    n: int = len(arr)

    for i in range(n):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][n-1-i]
    return abs(diagonal_1 - diagonal_2)


if __name__ == '__main__':
    arr: [] = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result: int = diagonalDifference(arr)
    print(result)