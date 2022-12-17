import re

def parse_input(path):
    lines = [ l.strip() for l in open(path).readlines() ]
    #print(lines)

    p = re.compile("Valve ([A-Z]*) has flow rate=(\\d*); tunnels? leads? to valves? (.*)")

    data = [ p.match(l) for l in lines ]
    data = [ m.groups() for m in data ]

    # valves[n] = list of n reachable from n
    valves = dict()
    # flowrates[n] = rate of node n
    flowrates = dict()

    for d in data:
        #print(d)
        n = d[0]
        flowrates[n] = int(d[1])
        valves[n] = [ e.strip() for e in d[2].split(',') ]

    for n in valves:
        valves[n] = list(sorted(valves[n], key=lambda d:flowrates[d]))

    return valves, flowrates

def calculate_distances(valve, valves):
    seen = set([valve])
    result = dict()
    queue = [valve]
    current = 2 # time to walk + time to open

    while len(queue) > 0:
        new_queue = []
        for src in queue:
            for dst in valves[src]:
                if dst not in seen:
                    result[dst] = current
                    new_queue.append(dst)
                    seen.add(dst)

        current += 1
        queue = new_queue

    return result

def create_distance_matrix(valves):
    result = dict()
    for src in valves:
        result[src] = calculate_distances(src, valves)

    return result


best = 0
def find_best_solution(location1, location2, valves, distances, flowrates, clock1, clock2, opened, score, path1, path2):
    global best        

    if location1 == 'nop':
        moves1 = ['nop']  
    else: moves1 = [ dst for dst in valves.keys() if flowrates[dst] > 0 and dst not in opened and clock1+distances[location1][dst] < 26 ]
    if location2 == 'nop':
        moves2 = ['nop']
    else: moves2 = [ dst for dst in valves.keys() if flowrates[dst] > 0 and dst not in opened and clock2+distances[location2][dst] < 26 ]

    # if one cannot make valid moves, but the other can, we must let one idle
    if len(moves1) == 0 and len(moves2) > 0:
        moves1 = ['nop']
    if len(moves2) == 0 and len(moves1) > 0:
        moves2 = ['nop']

    moves = []
    for m1 in moves1:
        for m2 in moves2:
            if m1 != m2:
                moves.append((m1,m2))

    for dst1,dst2 in moves:
        if dst1 != 'nop':
            opened.add(dst1)
        if dst2 != 'nop':
            opened.add(dst2)
        path1.append(dst1)
        path2.append(dst2)
        gain = 0 if dst1 == 'nop' else (26 - clock1 - distances[location1][dst1]) * flowrates[dst1]
        gain += 0 if dst2 == 'nop' else (26 - clock2 - distances[location2][dst2]) * flowrates[dst2]
      
        if score + gain > best:
            best = score + gain
            print("new best", best)
            print("path1", path1)
            print("path2", path2)
            #explain(path, distances, flowrates)

        find_best_solution(dst1, dst2, valves, distances, flowrates, clock1 + (0 if dst1 == 'nop' else distances[location1][dst1]), clock2 + (0 if dst2 == 'nop' else distances[location2][dst2]), opened, score + gain, path1, path2)
        
        if dst1 != 'nop':
            opened.remove(dst1)
        if dst2 != 'nop':
            opened.remove(dst2)
        del path1[len(path1)-1]
        del path2[len(path2)-1]
    


#valves, flowrates = parse_input('data/day16.sample')
valves, flowrates = parse_input('data/day16')

distances = create_distance_matrix(valves)
for v in distances:
    print("distances from",v, distances[v])

find_best_solution('AA', 'AA', valves, distances, flowrates, 0, 0, set(['AA']), 0, ['AA'], ['AA'])

# TODO: this is very very slow - try to guide the search by sorting moves best-first or using an a*

