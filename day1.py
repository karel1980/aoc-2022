#!/usr/bin/env python3

lines = [l.strip() for l in open('data/day1').readlines()]


joined = ','.join(lines)

split = joined.split(',,')

best = 0
for s in split:
    calories = sum([int(i) for i in s.split(',')])

    if calories > best:
        best = calories


print(best)
