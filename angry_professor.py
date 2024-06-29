"""
A Discrete Mathematics professor has a class of students.
Frustrated with their lack of discipline,
the professor decides to cancel class if fewer than some number of students are present when class starts.
Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

Example
n = 5
k = 3
a = [-2,-1,0,1,2]

The first 3 students arrived on. The last 2 were late. The threshold is 3 students, so class will go on. Return YES.

Note: Non-positive arrival times (a[i]<= 0) indicate the student arrived early or on time;
positive arrival times (a[i] > 0) indicate the student arrived a[i] minutes late.
"""


def angry_professor(k: int, students: list[int]):
    on_time: int = 0
    for s in students:
        if s <= 0:
            on_time += 1

    if on_time >= k:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    result: str = angry_professor(1, [-1, -3, 4, 2])
    print(result)
