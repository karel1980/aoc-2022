import re

lines = [ l.strip() for l in open('data/day15').readlines() ]
#lines = [ l.strip() for l in open('data/day15.sample').readlines() ]


def count_without_beacons(lines, target):
    pattern = re.compile("Sensor at x=([-\d]*), y=([-\d]*): closest beacon is at x=([-\d]*), y=([-\d]*)")
    ranges = set()
    bxs = set()
    for line in lines:
        m = pattern.match(line)
        if m is None:
            raise("input does not match pattern")

        #print(line)

        sx = int(m.groups()[0])
        sy = int(m.groups()[1])
        bx = int(m.groups()[2])
        by = int(m.groups()[3])

        if by == target:
            bxs.add(bx)

        #print(sx, sy, bx, by)

        sensor_range = abs(by-sy) + abs(bx-sx)

        distance_from_target = abs(target - sy)

        if sensor_range < distance_from_target:
            # sensor does not give information about target
            continue
        delta = sensor_range - distance_from_target
        ranges.add((sx - delta, sx + delta))
    

    positions = set()
    for r in ranges:
        for i in range(r[0], r[1]+1):
            positions.add(i)

    positions -= bxs
    #print(bxs)
    #print(list(sorted(positions)))

    return len(positions)

print("number of non-beacons at line 10:", count_without_beacons(lines, 10))
print("number of non-beacons at line 2M:", count_without_beacons(lines, 2000000))
