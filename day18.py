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
      
faces = count_all_faces(voxels)
trapped =count_trapped(voxels)
print("faces", faces)
print("trapped", trapped)


print(faces - 6 * trapped)

