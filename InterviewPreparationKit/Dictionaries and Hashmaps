import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #print(magazine)
    #print(note)
    mag = {}
    for word in magazine:
        if word not in mag:
            mag[word] = 1
        else:
            mag[word] += 1

    nt = {}
    for wd in note:
        if wd not in nt:
            nt[wd] = 1
        else:
            nt[wd] += 1

    for key, value in nt.items():
        #print(key, value)
        if (key in mag):
            if (value <= mag[key]):
                continue
            else:
                print("No")
                return
        elif (key not in mag):
            print("No")
            return
        

    print("Yes")
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
