import numpy as np
coords = set()

# lists of col,row coordinate pairs
lines = [ l.strip().split(' -> ') for l in open('data/day14')]
#lines = [ l.strip().split(' -> ') for l in open('data/day14.sample')]

for spec in lines:
    spec = [ tuple(map(int, pair.split(','))) for pair in spec ]

    for i in range(len(spec)-1):
        a,b = spec[i], spec[i+1]
        print('line from',a,'to',b)
        # fill the line between a and b
        dcol = b[0] - a[0]
        drow = b[1] - a[1]

        pos = a
        length= max([abs(dcol), abs(drow)])+1
        print('length', length)
        for j in range(length):
            pos = (a[0] + np.sign(dcol)*j, a[1] + np.sign(drow)*j)
            print('adding',pos)
            coords.add(pos)

# add the floor
xs = [p[0] for p in coords]
xmin, xmax = min(xs), max(xs)
print("cols:",xmin, xmax)

ys = [p[1] for p in coords]
ymin, ymax = min(ys), max(ys)
print("rows:",ymin,ymax)

lowest_layer = ymax + 2

for col in range(0, xmax + 500):
    coords.add((col, lowest_layer))

# coords now contains the full scene, let's start adding sand
lowest_row = max([p[1] for p in coords])
print("lowest row", lowest_row)


def down(p):
    return p[0],p[1]+1
def downleft(p):
    return p[0]-1,p[1]+1
def downright(p):
    return p[0]+1,p[1]+1


def show(coords, sand = (-100,-100)):
    xs = [p[0] for p in coords]
    xmin, xmax = min(xs), max(xs)

    ys = [p[1] for p in coords]
    ymin, ymax = min(ys), max(ys)

    print(xmin, xmax)

    for row in range(ymin, ymax + 1):
        print(''.join(['#' if (col, row) in coords or (col,row) == sand else '.' for col in range(xmin, xmax+1)]))

print("coords", sorted(coords))
show(coords)

clock = 0
falling_off = False
blocked = False

entrypoint = (500,0)

clock = 0
sandlayer = [ ' ' for i in range(10000)]
sandlayer[500] = 'o'

layer_num = 0
def calculate_next_layer(prev_layer, rocklayer):
    result = [ ' ' for i in range(1000)]
    for i in range(len(rocklayer)):
        if rocklayer[i] == '#':
            result[i] = '#'

    for i in range(1,len(prev_layer)-1):
        if 'o' in prev_layer[i-1:i+2] and rocklayer[i] != '#':
            result[i] = 'o'

    return result


total_sand = 1
while layer_num != lowest_layer:
    layer_num += 1
    layercoords =  list(map(lambda c: c[0], filter(lambda c: c[1] == layer_num, coords)))
    rocklayer = [' ' for i in range(len(sandlayer)) ]
    for col in layercoords:
        rocklayer[col] = '#'
    sandlayer = calculate_next_layer(sandlayer, rocklayer)
    total_sand += sum([ 1 if c == 'o' else 0 for c in sandlayer])
    print("".join(sandlayer[250:750]))
    print(total_sand)

print(total_sand)


