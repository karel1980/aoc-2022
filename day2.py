#!/usr/bin/env python3

ROCK="rock"
PAPER="paper"
SCISSORS="scissors"

LOOKUP = dict(A = ROCK, B = PAPER, C = SCISSORS, X = ROCK, Y = PAPER, Z = SCISSORS)

def safe(other):
    return LOOKUP.get(other, other)

def read_strategy():
    raw= [l.strip().split(' ') for l in open('data/day2').readlines()]
    return map(lambda r: (safe(r[0]), safe(r[1])), raw)

def item_score(item):
    print("item",item)
    if item == ROCK:
        return 1
    if item == PAPER:
        return 2
    if item == SCISSORS:
        return 3

    raise "bad"


DRAW=3
WIN=6
LOSE=0

def game_score(other, you):
    print("game", other, you)
    if you == other:
          return DRAW
    if you == ROCK:
          return WIN if other == SCISSORS else LOSE
    if you == SCISSORS:
          return WIN if other == PAPER else LOSE
    if you == PAPER:
          return WIN if other == ROCK else LOSE

    raise "kapot"

def part1():
    strategy = read_strategy()

    total = 0
    for s in strategy:
        total += item_score(s[1]) + game_score(s[0], s[1])

    return total

def part2():
    return


print(part1())

    
