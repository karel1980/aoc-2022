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

def explain(path, distances, flowrates):
    clock = 0
    score = 0
    c = path[0]
    pressure = 0
    for p in path[1:]:
        print("move to", p)
        print("cost / flowrate", distances[c][p], flowrates[p])
        gain = (30 - clock - distances[c][p]) * flowrates[p]
        score += gain
        print("gain / score", gain, score)
        pressure+= flowrates[p]
        print("flowrate", pressure)
        

best = 0
def find_best_solution(location, valves, distances, flowrates, clock, opened, score, path):
    global best        

    moves = [ dst for dst in valves.keys() if flowrates[dst] > 0 and dst not in opened and clock+distances[location][dst] < 30 ]
    # todo: sort moves to go for the best improvement (remaining clock * flowrate) first?
    #print("at", location, "with opened", opened, "moves are", moves)

    for dst in moves:
        #print("opening", dst)
        opened.add(dst)
        path.append(dst)
        gain = (30 - clock - distances[location][dst]) * flowrates[dst]
        #print("from", location,"to",dst,"timecost", distances[location][dst], "flowrate", flowrates[dst], "gain", gain)
      
        if score + gain > best:
            best = score + gain
            print("new best", best)
            print("path", path)
            #explain(path, distances, flowrates)

        find_best_solution(dst, valves, distances, flowrates, clock + distances[location][dst], opened, score + gain, path)
        
        opened.remove(dst)
        del path[len(path)-1]
    


#valves, flowrates = parse_input('data/day16.sample')
valves, flowrates = parse_input('data/day16')

distances = create_distance_matrix(valves)
for v in distances:
    print("distances from",v, distances[v])

find_best_solution('AA', valves, distances, flowrates, 0, set(['AA']), 0, ['AA'])

