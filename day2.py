#!/usr/bin/env python3

ROCK="rock"
PAPER="paper"
SCISSORS="scissors"

LOOKUP = dict(A = ROCK, B = PAPER, C = SCISSORS, X = ROCK, Y = PAPER, Z = SCISSORS)

def safe(other):
    return LOOKUP.get(other, other)

def read_strategy(path):
    raw= [l.strip().split(' ') for l in open(path).readlines()]
    return map(lambda r: (r[0], r[1]), raw)

def item_score(item):
    #print("item",item)
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
    other = safe(other)
    you = safe(you)
    #print("game", other, you)
    if you == other:
          return DRAW
    if you == ROCK:
          return WIN if other == SCISSORS else LOSE
    if you == SCISSORS:
          return WIN if other == PAPER else LOSE
    if you == PAPER:
          return WIN if other == ROCK else LOSE

    raise "kapot"

def part1(path):
    strategy = read_strategy(path)

    total = 0
    for s in strategy:
        total += item_score(s[1]) + game_score(s[0], s[1])

    return total

STRATEGY=dict(X="lose", Y="draw", Z="win")

def strategy(key):
    return STRATEGY[key]

def part2(path):
    rounds = read_strategy(path)

    total = 0
    for s in rounds:
        #print("other plays", safe(s[0]))
        strat = strategy(s[1])
        #print("you should", strat)
        your_item = determine_play(safe(s[0]), strat)
        #print("your item is", your_item)
        total += item_score(your_item) + game_score(s[0], your_item)

    return total

def determine_play(other, strategy):
    #print("determine_play", other, strategy)
    if strategy == "draw":
        return other

    if other == ROCK:
        return PAPER if strategy == "win" else SCISSORS
    if other == PAPER:
        return SCISSORS if strategy == "win" else ROCK
    if other == SCISSORS:
        return ROCK if strategy == "win" else PAPER
    

if __name__=="__main__":
    #print(part1())
    print(part2('data/day2'))

