import math
import os
import random
import re
import sys
import collections

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    triplets = 0

    m1 = collections.defaultdict(int)
    m2 = collections.defaultdict(int)
    
    for i in reversed(arr):
        print("i is ",i)
        if (i*r) in m2:
            print ("i*r in m2",i*r)
            print ("m2[i*r]",m2[i*r])
            
            triplets += m2[i*r]
            print ("triplets",triplets)

        if (i*r) in m1:
            print ("i*r in m1",i*r)
            print ("m1[i*r]",m1[i*r])
            m2[i] += m1[i*r]
            print("m2", m2)


        m1[i] += 1
        print("m1[i]",m1[i])

    return (triplets)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
