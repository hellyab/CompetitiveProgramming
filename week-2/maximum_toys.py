#!/bin/python3

import math
import os
import random
import re
import sys

def counting_sort(items):
    max = 0
    for i in range(len(items)):
        if items[i] > max:
            max = items[i]
    count_list = []
    for i in range(max+1):
        count_list.append(0)
    for i in range(len(items)):
        count_list[items[i]]+=1
    final_list = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            final_list.append(i)
    return final_list

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_prices = insertion_sort(prices)
    total = 0
    ctr = 0
    while total + prices[ctr]<=k:
        total += prices[ctr]
        ctr +=1
    return ctr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
