import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    arr_s = sorted(ar, reverse = True)
    maxi = max(arr_s)
    num = 0
    for i in range(len(arr_s)):
        if (ar[i] == maxi):
            num += 1
    return (num)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
