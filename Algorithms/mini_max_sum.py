import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini = 0
    maxi = 0
    asc = sorted(arr, reverse = False)
    des = sorted(arr, reverse = True)
    for i in range(len(asc)):
        if (i != (len(asc)-1)):
            mini += asc[i]
    for j in range(len(des)):
        if (j != (len(des)-1)):
            maxi += des[j]

    print (mini , maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
