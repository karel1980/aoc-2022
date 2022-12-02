#!/usr/bin/env python3

lines = [l.strip() for l in open('data/day1').readlines()]


joined = ','.join(lines)

split = joined.split(',,')

def part1():
    best = 0
    for s in split:
        calories = sum([int(i) for i in s.split(',')])

        if calories > best:
            best = calories


    return best


def part2():
    allsums = []
    for s in split:
        calories = sum([int(i) for i in s.split(',')])
        allsums.append(calories)

    top3 = sorted(allsums)[-3:]
    return sum(top3)


print(part1())
print(part2())
