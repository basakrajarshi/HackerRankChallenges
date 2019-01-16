import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #print(apples)
    #print(oranges)
    num_apples = 0
    num_oranges = 0

    #Counting number of apples falling on house:
    for apple in apples:
        if (apple > 0):
            if (a + apple >= s and a + apple <= t):
                num_apples += 1

    # Counitng the number of oranges falling on house:
    for orange in oranges:
        if (orange < 0):
            if (b + orange <= t and b + orange >= s):
                num_oranges += 1

    print(num_apples)
    print(num_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
