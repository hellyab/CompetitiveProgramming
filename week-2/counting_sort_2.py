#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    count_list = []
    for i in range(max+1):
        count_list.append(0)
    for i in range(len(arr)):
        count_list[arr[i]]+=1
    final_list = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            final_list.append(str(i))
    return " ".join(final_list)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
