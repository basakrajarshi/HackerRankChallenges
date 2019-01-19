import math
import os
import random
import re
import sys

def commonChild(s1, s2):
    prev_lcs = [0]*(len(s2)+1)
    curr_lcs = [0]*(len(s2)+1)
    for c1 in s1:
        curr_lcs, prev_lcs = prev_lcs, curr_lcs
        for j, c2 in enumerate(s2,1):
            if (c1 == c2):
                curr_lcs[j] = prev_lcs[j-1] + 1
            else:
                curr_lcs[j] = max(prev_lcs[j], curr_lcs[j-1])
    #print(curr_lcs)
    #print(prev_lcs)
    return curr_lcs[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
