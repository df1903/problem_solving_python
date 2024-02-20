"""You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles. Count how many candles are tallest. """

def birthdayCakeCandles(candles: [int]) -> int:
    max_age: int = 0
    num_candles: int = 0
    for i in candles:
        if i > max_age:
            max_age = i
            num_candles = 1
            continue
        elif i == max_age:
            num_candles += 1
    return num_candles


if __name__ == '__main__':
    candles: [int] = [3, 2, 1, 3]
    result: int = birthdayCakeCandles(candles)
    print(result)