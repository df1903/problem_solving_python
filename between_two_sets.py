def get_total_x(array_1: list[int], array_2: list[int]) -> int:
    start_range: int = max(array_1)
    end_range: int = min(array_2)
    number: int = 0

    for i in range(start_range, end_range+1):
        if all(i % x == 0 for x in array_1) and all(x % i == 0 for x in array_2):
            number += 1

    return number


if __name__ == '__main__':
    a: list[int] = [2, 6]
    b: list[int] = [24, 36]
    print(get_total_x(a, b))
