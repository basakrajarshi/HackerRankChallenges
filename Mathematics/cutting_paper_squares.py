import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m):
    if (n == 1 and m == 1):
        return (0)
    else:
        return (n*m - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
