import re

#lines = [ l.strip() for l in open('data/day15').readlines() ]
lines = [ l.strip() for l in open('data/day15.sample').readlines() ]


def simplify_ranges(ranges):
    ranges = list(sorted(ranges))

    i = 0
    while i < len(ranges)-1:
        a = ranges[i]
        b = ranges[i+1]
        if b[0] <= a[1] + 1:
            del ranges[i+1]
            ranges[i] = (a[0], max(a[1],b[1]))

    return ranges

def count_without_beacons(sensors, target):
    pattern = re.compile("Sensor at x=([-\d]*), y=([-\d]*): closest beacon is at x=([-\d]*), y=([-\d]*)")
    ranges = set()
    bxs = set()
    for sensor in sensors:
        sx = sensor[0][0]
        sy = sensor[0][1]
        bx = sensor[1][0]
        by = sensor[1][1]

        if by == target:
            bxs.add(bx)

        sensor_range = abs(by-sy) + abs(bx-sx)

        distance_from_target = abs(target - sy)

        if sensor_range < distance_from_target:
            # sensor does not give information about target
            continue
        delta = sensor_range - distance_from_target
        ranges.add((sx - delta, sx + delta))
    
    print("before simplification", list(sorted(ranges)))
    ranges = simplify_ranges(ranges)
    print("after simplification", list(sorted(ranges)))

    not_sensored = 0
    for r in ranges:
        not_sensored += r[1] - r[0] + 1

#    positions = set()
#    for r in ranges:
#        for i in range(r[0], r[1]+1):
#            positions.add(i)
#
#    positions -= bxs
    #print(bxs)
    #print(list(sorted(positions)))

    return not_sensored - len(set(bxs))

def parse_lines(lines):
    result = []
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
        result.append(((sx,sy),(bx,by)))

    return result
    
sensors = parse_lines(lines)
print("number of non-beacons at line 10:", count_without_beacons(sensors, 10))
print("number of non-beacons at line 2M:", count_without_beacons(sensors, 2000000))
