#!/usr/local/bin/python3

import sys

v = list()
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

v.append(0)
for i in range(1, n):
    v.append(int(sys.stdin.readline()))
v.append(0)

opt = dict()

opt[0] = sum(v)

for j in range(1, n+1):
    max = 0
    for i in range(1, k+1):
        if j-i >= 0:
            tmp = opt[j-i]-v[j]
            if tmp > max or i == 1:
                opt[j] = tmp
                max = tmp


print(opt[n])
