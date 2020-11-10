#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n_binary = bin(n)[2:].split('0')
    cose_number = sorted(n_binary, reverse=True)[0]
    print(len(cose_number))