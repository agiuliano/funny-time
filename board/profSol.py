#!/usr/bin/python
import sys

v = list()
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
v.append(0) #only to index flowers with 1,2,...,n
for i in range(1,n):
    v.append(int(sys.stdin.readline()))
v.append(0)

mem = dict()

def OPT(i,p):
        if i == n:
                return min(p,v[i])

        if (i,p) in mem:
                return mem[(i,p)]

        ret = 0
        for pi in v:
            if pi >= p:
                ret = max( OPT(i+1,pi) + pi*(pi <= v[i]),ret)

        mem[(i,p)] = ret
        return mem[(i,p)]

print(OPT(1,max(v)))

