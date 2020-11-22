#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    sum_hourglass = 0
    arr_hourglass = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for n in range(4):
        for i in range(4):
            sum_hourglass = sum(arr[i][n:n+3]) + arr[i+1][n+1] + sum(arr[i+2][n:n+3])
            arr_hourglass.append(sum_hourglass)
    print(max(arr_hourglass))