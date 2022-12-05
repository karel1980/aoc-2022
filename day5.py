import re


def getline(l, cols):
    result =  ''

    for c in range(cols): 
        result += l[c*4 + 1]

    return result


def parse(path):
    lines = [l.rstrip() for l in open(path).readlines()]

    empty = lines.index('')

    stacklines = lines[:empty-1]

    cols = int((max([len(l) for l in stacklines]) + 1) / 4)

    stacklines = [ getline(l + '                    ', cols) for l in stacklines ]

    print(stacklines)

    stacks = list()
    # build stacks
    for c in range(cols):
        stacks.append('')

    # add letters
    for l in stacklines:
        for c in range(cols):
            stacks[c] += l[c]

    # remove
    for c in range(cols):
        stacks[c] = "".join([x for x in stacks[c] if x != ' '])

    print(stacks)
    # reverse
    #for c in range(cols):
    #    stacks[c] = list(reversed(stacks[c]))

    print(stacks)

    return stacks, lines[empty+1:]

def execute(stacks, instruction):
    p = re.compile("move (\d+) from (\d+) to (\d+)")
    m = p.match(instruction)
    count, src, dst = [ int(n) for n in m.groups() ]

    #print(stacks)
    #print(instruction)

    for c in range(count):
        top, stacks[src-1] = stacks[src-1][0],stacks[src-1][1:]
        stacks[dst-1] = top + stacks[dst-1][:]


def execute(stacks, instruction):
    p = re.compile("move (\d+) from (\d+) to (\d+)")
    m = p.match(instruction)
    count, src, dst = [ int(n) for n in m.groups() ]

    #print(stacks)
    #print(instruction)

    pickup, stacks[src-1] = stacks[src-1][:count], stacks[src-1][count:]
    stacks[dst-1] = pickup + stacks[dst-1][:]


def part1(path):
    stacks, instructions = parse(path)

    for i in instructions:
        execute(stacks, i)

    msg = "".join(s[0] for s in stacks)

    return msg

if __name__=="__main__":
    print(part1('data/day5.sample'))
    print(part1('data/day5'))

