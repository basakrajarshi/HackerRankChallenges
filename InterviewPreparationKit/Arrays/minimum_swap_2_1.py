import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda y:y[1])
    vis = {}
    for k in range(n):
        vis[k] = False

    result = 0

    for i in range(n):
        if (vis[i] == True or arrpos[i][0] == i):
            continue
        
        cyclesize = 0
        j = i

        while (vis[j] == False):
            vis[j] = True
            j = arrpos[j][0]
            cyclesize += 1

        if (cyclesize > 0):
            result = result + (cyclesize - 1)

    return (result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
