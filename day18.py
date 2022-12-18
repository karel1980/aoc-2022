#lines = [l.strip().split(',') for l in open('data/day18.sample').readlines() ]
lines = [l.strip().split(',') for l in open('data/day18').readlines() ]
voxels = set([ tuple(map(int, l)) for l in lines ])

#voxels = set([(1,2,2), (2,2,2)])

def neighbors(n):
    result = []
    x,y,z = n
    for d in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        dx,dy,dz = d
        result.append((x+dx, y+dy, z+dz))
    return result

def is_trapped_air(v, voxels):
    debug = v == (2,2,5)
    if v in voxels:
        return False
    x,y,z = v
    for n in neighbors(v):
        if n not in voxels:
            return False

    return True

# for all voxels v:
#     for all connected neighbors n of v:
#         if all neighbors of n are in voxels:
#              add n to trapped

def count_trapped(voxels):
    trapped = set()
    for v in voxels:
        for n in neighbors(v):
            if is_trapped_air(n, voxels):
                trapped.add(n)

    return len(trapped)


def count_faces2(v, voxels, outside):
    x,y,z = v
    result = 0
    for d in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
        dx,dy,dz = d
        w = (x+dx, y+dy, z+dz)
        is_rock = w in voxels
        if not is_rock and w in outside:
            result += 1

    return result

def count_faces(v, voxels):
    x,y,z = v
    result = 0
    for d in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
        dx,dy,dz = d
        w = (x+dx, y+dy, z+dz)
        is_face = (x+dx, y+dy, z+dz) not in voxels
        if is_face:
            result += 1

    return result

def count_all_faces(voxels):
    return sum([count_faces(v, voxels) for v in voxels])
      
def count_all_faces2(voxels, outside):
    return sum([count_faces2(v, voxels, outside) for v in voxels])
      
def find_outside_air(voxels):
    minx, miny, minz = min([v[0] for v in voxels]) -1, min([v[1] for v in voxels])-1, min([v[2] for v in voxels])-1
    maxx, maxy, maxz = max([v[0] for v in voxels]) +1, max([v[1] for v in voxels])+1, max([v[2] for v in voxels])+1

    origin = (minx, miny, minz)

    outside=set()
    queue=[origin]

    while len(queue) > 0:
        head = queue.pop()
        outside.add(head)
        for n in neighbors(head):
            if n not in queue and n not in outside and minx<=n[0]<=maxx and miny<=n[1]<=maxy and minz<=n[2]<=maxz and n not in voxels:
                queue.append(n)

    return outside


outside = find_outside_air(voxels)
print(count_all_faces2(voxels, outside))

