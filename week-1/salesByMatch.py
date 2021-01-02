#!/bin/python3

import math
import os
import random
import re
import sys

# Completed the sockMerchant function below.
def sockMerchant(n, ar):
    found = {}
    pairs = 0
    for i in range(n):
        if ar[i] in found:
            continue
        found[ar[i]]= ar.count(ar[i])//2
        
    for itemType in found:
        pairs += found[itemType] 
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
