import math
import os
import random
import re
import sys

def isBalanced(s):
    if len(s) % 2 != 0:
        return("NO")
    else:
        openers = tuple('({[')
        closers = tuple(')}]')
        #mapper = dict(zip(openers, closers))
        mapper = {"(":")", "{":"}", "[":"]"}
        queue = []
        print(mapper)
        for l in s:
            if l in openers:
                queue.append(mapper[l])
            elif l in closers:
                if len(queue) == 0  or l != queue.pop():
                    return ("NO")
        if len(queue) == 0:
            return ("YES")
        else:
            return ("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
