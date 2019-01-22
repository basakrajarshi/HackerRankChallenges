import math
import os
import random
import re
import sys

def maxSubsetSum(arr):
    excl = 0
    incl = arr[0]
    for i in range(1,len(arr)):
        temp = incl
        incl = max(excl + arr[i], incl)
        excl = temp
    return incl
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
