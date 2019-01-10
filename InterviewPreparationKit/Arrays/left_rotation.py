import math
import os
import random
import re
import sys

def rotLeft(a, d):
    #print(a)
    #print(type(a))
    for i in range(d):
        x = a.pop(0)
        a.append(x)
    return(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
