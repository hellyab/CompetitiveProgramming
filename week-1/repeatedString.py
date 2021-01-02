#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    remainingACount = 0
    count = 0
    fullStringSetCount = n // len(s)
    for i in range (len(s)):
        if s[i] == "a":
            if i < n % len(s) :
                remainingACount +=1 
            count += 1
    return (count * fullStringSetCount) + remainingACount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
