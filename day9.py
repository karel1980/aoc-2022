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

snake = [(0,0) for i in range(10) ]

tailpositions = set()
tailpositions.add(snake[-1])

def update_tail(snake):

    for i in range(1, len(snake)):
        h = snake[i-1]
        t = snake[i]
        delta = (h[0] - t[0], h[1] - t[1])

        if abs(delta[0]) < 2 and abs(delta[1]) < 2:
            # touching -> don't move
            snake[i] = t
        else:
            # not touching -> move 1 step in the direction of head, both vertically and horizontally
            snake[i] = (t[0] + np.sign(delta[0]), t[1] + np.sign(delta[1]))

for direction, count in instructions:
    d = DIRS[direction]
    for c in range(count):
        head = snake[0]
        head = (head[0] + d[0], head[1] + d[1])
        snake[0] = head
        update_tail(snake)
        tailpositions.add(snake[-1])


print(len(tailpositions))

