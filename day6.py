

def parse(path):
    lines = [l.strip() for l in open(path).readlines()]

    return lines


def part1(path):
    puzzle = parse(path)

    return 0


if __name__=="__main__":
    print(part1('data/day6.sample'))
    #print(part1('data/day6'))
