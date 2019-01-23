import math
import os
import random
import re
import sys

def largestRectangle(h):
    stack = []
    maxarea = 0
    i = 0
    while i < len(h):
        if (len(stack) == 0 or h[stack[-1]] <= h[i]):
            stack.append(i)
            i += 1
            #print(stack)
        else:
            top_of_stack = stack.pop()

            area = (h[top_of_stack]*((i - stack[-1] - 1) if stack else i))

            maxarea = max(maxarea, area)

    while stack:
        top_of_stack = stack.pop()

        area = (h[top_of_stack]*((i - stack[-1] - 1) if stack else i))

        maxarea = max(maxarea, area)

    return maxarea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
