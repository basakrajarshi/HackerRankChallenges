import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    #print(s1)
    #print(s2)
    ss1 = list(s1)
    ss2 = list(s2)

    sd1 = {}
    for i in ss1:
        if i not in sd1:
            sd1[i] = 1
        else:
            sd1[i] += 1

    sd2 = {}
    for i in ss2:
        if i not in sd2:
            sd2[i] = 1
        else:
            sd2[i] += 1

    for i in sd2:
        print(i)
        if (i in sd1):
            return ("YES")
        else:
            continue

    return("NO")



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
