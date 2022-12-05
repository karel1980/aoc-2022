
def readpuzzle(path):
    lines = [l.strip() for l in open(path).readlines()]
    return lines

def value(c):
    return '@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)

def score(part1, part2):
    a = set(part1)
    b = set(part2)

    i = a.intersection(b) 

    return sum([value(letter) for letter in i])

def linescore(line):
    mid = int(len(line)/2)
    a,b = line[:mid], line[mid:]
    return score(a,b)

def part1(path):
    lines = readpuzzle(path)

    total = 0

    for line in lines:
        total += linescore(line)

    return total 


def commontypescore(lines):
    a,b,c = set(lines[0]), set(lines[1]), set(lines[2])

    commonitem = list(a.intersection(b).intersection(c))[0]

    return score(commonitem,commonitem)

def part2(path):
    lines = readpuzzle(path)

    total = 0

    for i in range(0, len(lines), 3):
        total += commontypescore(lines[i:i+3])

    return total

if __name__=="__main__":
    #print(part1('data/day3'))
    print(part2('data/day3'))
