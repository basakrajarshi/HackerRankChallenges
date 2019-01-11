import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    length = len(arr)
    result = 0
    arr_dict = {}
    for i,item in enumerate(arr):
        arr_dict[item] = i

    checked = [False] * length

    for key, value in sorted(arr_dict.items(), key = lambda x:x[0]):
        print (key, value)

        if (checked[key-1] == True or (key-1) == value):
            continue
        
        cycles = 0
        value = key-1

        while (checked[value] is False):
            checked[value] = True
            value = arr_dict[value+1]
            cycles += 1
    
        result += (cycles - 1)
    
    return(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
