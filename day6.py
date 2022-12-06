

def parse(path):
    lines = [l.strip() for l in open(path).readlines()]

    return lines[0]

def findMarkerPosition(puzzle):
    pos = 0
    while True:
        if len(set(puzzle[pos:pos+4])) == 4:
            return pos + 4
        pos+=1

    raise 'kapot'

def findMarkerPosition2(puzzle):
    pos = 0
    while True:
        if len(set(puzzle[pos:pos+14])) == 14:
            return pos + 14
        pos+=1

    raise 'kapot'

def part1(path):
    puzzle = parse(path)

    return findMarkerPosition(puzzle)

def part2(path):
    puzzle = parse(path)

    return findMarkerPosition2(puzzle)


if __name__=="__main__":
    #print(part1('data/day6.sample'))
    #print(findMarkerPosition('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))
    print(part2('data/day6'))
