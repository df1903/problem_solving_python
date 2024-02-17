"""Given an array of integers, find the sum of its elements"""

def simpleArraySum(ar: [int]) -> int:
    sum : int = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    size: int = int(input("Enter the size of array: ").strip())
    array: [int] = []
    for i in range(size):
        array.append(int(input(f'Enter the {i+1}th element: ')))
    result : int= simpleArraySum(array)
    print(f'The sum of the elements in the array is: {result}')
