#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    fullStringSetCount = n//len(s)
    count = (fullStringSetCount * s.count("a")* len(s))//len(s)
    if fullStringSetCount*len(s)<n:
        for i in range(n-fullStringSetCount*len(s)):
            if s[i] == "a":
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()