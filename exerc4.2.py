#!/usr/local/bin/python3
import sys

v = list()
n = int(sys.stdin.readline())

v.append(0)
for i in range(1, n+1):
    v.append(int(sys.stdin.readline()))

mem = dict()

def comb(n):
    return int(n*(n-1)/2)

def OPT(j):
    if j == 0:
        return 0

    if j in mem:
        return mem[j]

    ret = OPT(0) + comb(j)

    for i in range(1, j):
        ret = min(OPT(i) + comb(j-i), ret)

    mem[j] = ret+v[j]
    return mem[j]


print(OPT(n))