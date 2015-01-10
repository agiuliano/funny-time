#!/usr/local/bin/python3

import sys

r = list()
r_ord = list()
w = list()
w_ord = list()
n = int(sys.stdin.readline())

for i in range(n):
    r.append(int(sys.stdin.readline()))

for i in range(n):
    w.append(int(sys.stdin.readline()))

if len(w) != len(r):
    raise Exception("Weights and resistences have to be of the same length")

swapping = True

while swapping:
    swapping = False
    for i in range(n-1):
        if r[i] < r[i+1]:
            tmp = r[i]
            r[i] = r[i+1]
            r[i+1] = tmp
            tmp = w[i]
            w[i] = w[i+1]
            w[i+1] = tmp

M = [[(1 if i==1 and j <= r[0] and j>0 else 0)
      for j in range(0, sum(w)+1)]
     for i in range(0, n+1)]


for i in range(2, n+1):
    for j in range(1, sum(w)+1):
        if j > r[i-1]:
            M[i][j] = M[i-1][j]
        else:
            M[i][j] = max(M[i-1][j], 1 + M[i-1][j+w[i-1]])

print("result:")
print(max(M[n-1]))