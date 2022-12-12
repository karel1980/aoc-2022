
#operations = [('noop',), ('addx', 3), ('addx', -5)]
#operations = [l.strip().split(' ') for l in open('data/day10.sample')]
operations = [l.strip().split(' ') for l in open('data/day10')]

x = 1
cycle = 0
measurements = []
row = -1

sample_points = set([20, 60, 100, 140, 180,  220])

screen = [' ' for i in range(40 * 6)]

def printscreen(screen):
    for i in range(0, len(screen), 40):
        print("".join(screen[i:i+40]))

for op in operations:

    if op[0] == 'noop':
        cycles = 1
        inc = 0
    else:
        cycles = 2
        inc = int(op[1])
   
    print("begin executing ", op)

    for i in range(cycles):
        cycle += 1
        print("cycle", cycle)
        pos  = (cycle - 1) % 40

        #print("during cycle %d: %d"%(cycle, x))
        if cycle in sample_points:
            current_strength = x * cycle
            print("measurement at cycle %d: %d"%(cycle, current_strength))
            measurements.append(current_strength)

        if pos % 40 == 0:
            row += 1
        
        screen[row * 40 + pos] = '#' if pos >= x-1 and pos <=x+1 else ' '
        print('carriage at ', pos)
        print('x is currently', x)
        printscreen(screen)



        if i == cycles-1:
            x += inc
            print("x is now ", x)


    #print('carriage at ', cycle)
    #print('x is currently', x)
    #print("after cycle %d: %d"%(cycle, x))


print(sum(measurements))

printscreen(screen)
