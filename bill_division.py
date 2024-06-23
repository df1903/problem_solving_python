"""
Two friends Anna and Brian, are deciding how to split the bill at a dinner.
Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion.
You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6].
Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2 = 3.
If he includes the cost of bill[2], he will calculate (2+4+6)/2 = 6. In the second case, he should refund 3 to Anna.
"""


def bona_appetit(bill: list[int], k: int, b: int) -> None:
    total: int = 0
    diference: int

    for i in range(len(bill)):
        if k != i:
            total += bill[i]
    diference = b - (total//2)

    if diference == 0:
        print("Bon Appetit")
    else:
        print(diference)


if __name__ == '__main__':
    bill_p: list[int] = [3, 10, 2, 9]
    k_p: int = 1
    b_p: int = 12
    bona_appetit(bill_p, k_p, b_p)
