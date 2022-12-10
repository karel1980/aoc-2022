
#operations = [('noop',), ('addx', 3), ('addx', -5)]
#operations = [l.strip().split(' ') for l in open('data/day10.sample')]
operations = [l.strip().split(' ') for l in open('data/day10')]

x = 1
cycle = 0
measurements = []

sample_points = set([20, 60, 100, 140, 180,  220])


for op in operations:

    if op[0] == 'noop':
        cycles = 1
        inc = 0
    else:
        cycles = 2
        inc = int(op[1])
   

    for i in range(cycles):
        cycle += 1
        #print("during cycle %d: %d"%(cycle, x))
        if cycle in sample_points:
            current_strength = x * cycle
            print("measurement at cycle %d: %d"%(cycle, current_strength))
            measurements.append(current_strength)

    x += inc
    print("after cycle %d: %d"%(cycle, x))


print(sum(measurements))
