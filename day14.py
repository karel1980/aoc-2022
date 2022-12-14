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

# coords now contains the full scene, let's start adding sand
lowest_row = max([p[1] for p in coords])

coords.add((500,-5))

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

while not falling_off:
    sand = (500,0)
    stopped = False

    clock+=1
    while not stopped and not falling_off:
        if down(sand) not in coords:
            sand = down(sand)
        elif downleft(sand) not in coords:
            sand = downleft(sand)
        elif downright(sand) not in coords:
            sand = downright(sand)
        else:
            stopped = True

        if sand[1] > lowest_row:
            falling_off = True

        #show(coords,sand)

    if not falling_off:
        coords.add(sand)
      
print(clock - 1)


