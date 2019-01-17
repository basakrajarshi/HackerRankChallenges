import math
import os
import random
import re
import sys
import collections

def makeAnagram(a, b):
    diff = {}
    for x in a:
        if x not in diff:
            diff[x] = 0
        diff[x] += 1
    for y in b:
        if y not in diff:
            diff[y] = 0
        diff[y] -= 1
    res = sum(abs(n) for n in diff.values())
    return(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
