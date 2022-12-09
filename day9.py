import numpy as np

def parse(line):
    p = line.split(' ')
    return (p[0], int(p[1]))

DIRS = dict()
DIRS['L'] = (0, -1)
DIRS['R'] = (0, 1)
DIRS['D'] = (1, 0)
DIRS['U'] = (-1, 0)

#instructions = [ parse(l.strip()) for l in open('data/day9.sample').readlines()]
instructions = [ parse(l.strip()) for l in open('data/day9').readlines()]

head = (0,0)
tail = (0,0)


tailpositions = set()
tailpositions.add(tail)

def update_tail(t, h):
    delta = (h[0] - t[0], h[1] - t[1])

    # touching -> don't move
    if abs(delta[0]) < 2 and abs(delta[1]) < 2:
        return t

    # not touching -> move 1 step in the direction of head, both vertically and horizontally
    return (t[0] + np.sign(delta[0]), t[1] + np.sign(delta[1]))
      

for direction, count in instructions:
    d = DIRS[direction]
    for c in range(count):
        head = (head[0] + d[0], head[1] + d[1])
        tail = update_tail(tail, head)

        tailpositions.add(tail)


print(len(tailpositions))

