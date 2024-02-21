"""HackerLand University has the following grading policy:
    Every student receives a grade in the inclusive range from 0 to 100.
    Any grade less 40 than is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""

def gradingStudents(grades: [int]) -> [int]:
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i]%5 == 3:
                grades[i] += 2
            elif grades[i]%5 == 4:
                grades[i] += 1
    return grades

if __name__ == '__main__':
    grades: [int] = [4,37,38,40,42,88]
    grades = gradingStudents(grades)
    print(grades) # [4, 37, 40, 40, 42, 90)
