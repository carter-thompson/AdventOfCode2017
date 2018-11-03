#!/usr/bin/env python3

with open('day5.txt') as f:
    data = f.read()


n = data.splitlines()
n = list(map(int, n))
# n = [0,3,0,1,-3]
i = 0
steps = 0
while(0 <= i < len(n)):
    steps += 1
    jump = n[i] + i
    n[i] += 1
    i = jump
print(steps)

n = data.splitlines()
n = list(map(int, n))
i = 0
steps = 0
while(0 <= i < len(n)):
    steps += 1
    jump = n[i] + i
    n[i] += 1 if n[i] < 3 else -1
    i = jump
print(steps)
