
def part1(path):

    lines = [l.strip().split(',') for l in open(path).readlines()]

    lines = [(a.split('-'), b.split('-')) for a,b in lines]

    total = 0
    for p1, p2 in lines:

        a,b = p1
        c,d = p2
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if a>=c and a<=d and b >=c and b <= d:
            total +=1
        elif c>= a and c <= b and d>=a and d<=b:
            total +=1
        else:
            total += 0

    return total

def part2(path):

    lines = [l.strip().split(',') for l in open(path).readlines()]

    lines = [(a.split('-'), b.split('-')) for a,b in lines]

    total = 0
    for p1, p2 in lines:

        a,b = p1
        c,d = p2
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if (a>=c and a<=d) or  (b >=c and b <= d):
            total +=1
        elif (c>= a and c <= b) or (d>=a and d<=b):
            total +=1
        else:
            total += 0

    return total


if __name__=="__main__":
    print(part1('data/day4'))
    #print(part1('data/day4.sample'))
    print(part2('data/day4'))
