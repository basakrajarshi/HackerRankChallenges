import math
import os
import random
import re
import sys

def commonChild(s1, s2):
    leastcommonsub = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    #print(leastcommonsub)
    for i, x in enumerate(s1):
        for j,y in enumerate(s2):
            #print(x,y)
            if (x == y):
                #print("YES", x, y)
                leastcommonsub[i+1][j+1] = leastcommonsub[i][j] + 1
                #print("If",leastcommonsub)
            else:
                leastcommonsub[i+1][j+1] = max(leastcommonsub[i+1][j],
                leastcommonsub[i][j+1])
                #print("Else",leastcommonsub)
    return(leastcommonsub[-1][-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
