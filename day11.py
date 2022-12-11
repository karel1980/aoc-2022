lines = [l.strip() for l in open('data/day11.sample').readlines()]

monkeys = []


class Monkey:
    def __init__(self, items, op, test, on_true, on_false):
        self.items = items
        self.op = op
        self.test = test
        self.on_true = on_true
        self.on_false = on_false
        self.inspections = 0


def parse_spec(lines):
    starting = [int(item.strip()) for item in lines[1].split(':')[1].split(',')]
    op = lines[2].split('new =')[1].strip().split(' ')
    test = int(lines[3].split('divisible by')[1].strip())
    on_true = int(lines[4].split('monkey ')[1].strip())
    on_false = int(lines[5].split('monkey ')[1].strip())

    return Monkey(starting, op, test, on_true, on_false)

for i in range(0, len(lines), 7):
    spec = lines[i:i+6]
    monkeys.append(parse_spec(spec))


for round in range(20):
    for monkey in monkeys:
        items = list(monkey.items)
        for item in monkey.items:
            arg = item if monkey.op[2] == 'old' else int(monkey.op[2])
            new_worry_level = item * arg if monkey.op[1] == '*' else item + arg
            new_worry_level = int(new_worry_level / 3)
            #print('new worry level', new_worry_level)

            test_result = new_worry_level % monkey.test == 0


            target = monkey.on_true if test_result else monkey.on_false
            #print('goes to ', target)

            monkeys[target].items.append(new_worry_level)
        monkey.inspections += len(monkey.items)
        monkey.items = []

    print("round %d ends"%(round+1))

    for m in monkeys:
        print(m.items)


inspections = map(lambda m:m.inspections, monkeys)
top = sorted(inspections)[-2:]

print(top[0] * top[1])
