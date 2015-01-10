#!/usr/local/bin/python3

import sys

v = list()
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

v.append(0)
for i in range(1, n):
    v.append(int(sys.stdin.readline()))
v.append(0)


def OPTCOUNT(start):
    if start >= n:
        return 0

    ret = 0
    for i in range(start, min(start+k, n)):
        print(list(range(start, min(start+k, n))))
        opt = v[i] + OPT(i+k)
        print('ciclo: ', i, 'opt: ', opt)
        ret += opt

    return ret

def OPT(i, p):
    if i == n:
        return min(p, v[i])
    for j in range(i, min(i+k, n)):
        OPT(j+k, v[j])


print(OPT(1, max(v)))