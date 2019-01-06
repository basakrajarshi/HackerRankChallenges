import os
import sys

def timeConversion(s):
    res = ""
    h = s.split(':')[0]
    hour = int(h)  
    minute = s.split(':')[1].split(':')[0]
    sec = s.split(':')[2].split(':')[0]
    
    if ("AM" in s):
        second = sec.replace("AM", "")
        if (hour == 12):
            res = str(0) + str(0) + ":" + minute + ":" + second
        else:
            if (hour <= 9):
                res = str(0) + str(hour) + ":" + minute + ":" + second
            else:
                res = str(hour) + ":" + minute + ":" + second
    elif ("PM" in s):
        second = sec.replace("PM", "")
        if (hour == 12):
            res = str(hour) + ":" + minute + ":" + second
        else:
            res = str(hour + 12) + ":" + minute + ":" + second

    return (res)
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
