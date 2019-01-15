import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    diffarr = [0]*(n+1)
    #print(diffarr)
    for i in queries:
        diffarr[i[0]-1] += i[2]
        diffarr[i[1]] -= i[2]
    maxi = 0
    asum = 0
    for j in diffarr:
        asum += j
        if (asum > maxi):
            maxi = asum 
             
    return (maxi)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
