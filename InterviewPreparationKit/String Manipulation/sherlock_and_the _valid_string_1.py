import math
import os
import random
import re
import sys
import collections

def isValid(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    
    ll = list(set(d.values()))
    if len(ll) == 1:
        return("YES")
    elif len(ll) == 2:
        l1 = []
        l2 = []
        for key in d.keys():
            val = d[key]
            if val == ll[0]:
                l1.append(key)
            if val == ll[1]:
                l2.append(key)
        if len(l1) == 1 or len(l2) == 1:
            return("YES")
        else:
            return("NO")        
    else:
        return("NO")    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
