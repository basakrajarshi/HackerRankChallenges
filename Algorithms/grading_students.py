import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    finalgrades = []
    for grade in grades:
        if (grade < 38):
            #print("First if ",grade)
            finalgrades.append(grade)
        else:
            #print("First else ", grade)
            if (grade % 5 <= 2):
                finalgrades.append(grade)
            else:
                finalgrades.append(grade + (5 - (grade % 5)))

    return (finalgrades)



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
