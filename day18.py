#lines = [l.strip().split(',') for l in open('data/day18.sample').readlines() ]
lines = [l.strip().split(',') for l in open('data/day18').readlines() ]
voxels = set([ tuple(map(int, l)) for l in lines ])

#voxels = set([(1,2,2), (2,2,2)])

def is_trapped(v, voxels):
    x,y,z = v
    for dx in (-1,1):
        for dy in (-1,1):
            for dz in (-1,1):
                w = x+dx, y+dy, z+dz
                if w in voxels:
                    return True

    return False

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
      
print(count_all_faces(voxels))

