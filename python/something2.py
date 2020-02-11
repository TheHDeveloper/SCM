#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b, n, m):
    r = []
    mi = max(a)
    ma = min(b)
    for i in range(mi,ma+1):
        z=1
        for j in range(0,n):
            if(z==0):
                break
            elif(i%a[j]!=0):
                z = 0
        if(z==0):
            continue
        if(z==1):
            for k in range(0,m):
                if(z==0):
                    break
                if(b[k]%i!=0):
                    z = 0
        if(z==1):
            r.append(i)
    return len(r)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr, n, m)

    fptr.write(str(total) + '\n')

    fptr.close()
