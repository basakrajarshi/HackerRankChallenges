import math
import os
import random
import re
import sys
import itertools


def maximumToys(prices, k):
    list.sort(prices)
    count = cost = 0
    for price in prices:
        if cost + price <= k:
            count += 1
            cost += price
        else:
            break
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
