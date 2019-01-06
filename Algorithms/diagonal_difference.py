import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            #print(arr[i])
            # For the first diagonal
            if (i == j):
                d1 += arr[i][j]
            # For the second diagonal
            if (i + j == (len(arr[0]) - 1)):
                d2 += arr[i][j]

    return (abs(d1 - d2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
