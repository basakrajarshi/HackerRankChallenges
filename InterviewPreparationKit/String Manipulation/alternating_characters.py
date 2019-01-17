import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    ch = list(s)
    res = ch[0]
    count = 0
    #print(ch)
    for c in range(len(ch)-1):
        #print(ch[c],ch[c+1])
        if ch[c] != ch[c+1]:
            res = res + ch[c+1]
        else:
            count += 1
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
