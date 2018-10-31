#!/usr/bin/env python3

with open('day4.txt') as f:
    passPhrases = f.read()

passPhrases = passPhrases.splitlines()

sum = 0
for phrase in passPhrases:
    if len(set(phrase.split())) == len(phrase.split()):
        sum+=1

print(sum)
