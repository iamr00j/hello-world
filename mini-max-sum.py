#https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minimum = 0
    maximum = 0
    x = 0
    y = -1

    while True:
        minimum += arr[x]
        maximum += arr[y]
        x += 1
        y -= 1
        if x == len(arr) - 1 or y == 1:
            break
    
    print (minimum, maximum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
