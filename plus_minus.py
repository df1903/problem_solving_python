"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with places after the decimal."""


def plusMinus(arr: [int]):
    proportions = {
        "positive": 0,
        "negative": 0,
        "zero":0
    }
    n = len(arr)
    for i in arr:
        if i > 0:
            proportions['positive'] += 1
            continue
        if i < 0:
            proportions['negative'] += 1
            continue
        proportions['zero'] += 1

    for key in proportions.keys():
        print(f'proportion of {key} values {proportions[key]/ n}')


if __name__ == '__main__':
    arr: [int] = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)