import math
import os
import random
import re
import sys

def all_the_same(elements):
   return len(elements) == elements.count(elements[0])

def substrCount(n, s):
    l = list(s)
    count = 0
    #print(l)
    # Find all subarrays
    subs = []
    for i in range(len(l)):
        n = i+1
        while n <= len(l):
            sub = l[i:n]
            subs.append(sub)
            n += 1
    #print (subs)
    for s in subs:
        if (len(s) == 1):
            #print(s)
            count += 1
        elif (all_the_same(s) == True):
            #print(s)
            count += 1
        else:
            print(s)
            # Remove the middle element from the list
            if (len(s) % 2 != 0):
                idd = int(math.floor(len(s)/2))
                #print(idd)
                s.pop(idd)
                #print(s)
                if (all_the_same(s) == True):
                    count += 1
    return (count)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
