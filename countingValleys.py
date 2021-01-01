#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    elevationSum = 0
    valleys = 0
    inValley = False
    for i in range(steps):
        if path[i]=="D":
            elevationSum -=1
            if elevationSum < 0: 
                inValley = True
        else:
            elevationSum +=1
            if elevationSum > 0: 
                inValley = False
        if elevationSum == 0 and inValley == True:
             valleys += 1
             inValley = False
             
    return valleys
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
