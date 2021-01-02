#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    annaInclusiveTotal = 0
    for i in range(len(bill)):
        if i != k:
            annaInclusiveTotal+= bill[i]
    if b == annaInclusiveTotal/2:
        print("Bon Appetit")
    else:
        print(int(b -(annaInclusiveTotal/2)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
