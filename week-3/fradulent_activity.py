#!/bin/python3

import math
import os
import random
import re
import sys

def findAverage(expenditure):
    n = len(expenditure)
    expenditure.sort()
    if n % 2 ==1:
        return expenditure[n // 2]
    else:
        return (expenditure[n // 2] + expenditure[n // 2 - 1]) // 2

def activityNotifications(expenditure, d):
    n = len(expenditure)
    notificationsCount = 0
    
    start = 0
    end = start + d 
    
    while end < n - 1:
        average = findAverage(expenditure[start:end])
        current = expenditure[end]
        if (current - (2 * average)) >= 0:
            notificationsCount += 1
        start += 1
        end += 1
    return notificationsCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
