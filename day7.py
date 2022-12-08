
#lines = [ l.strip() for l in open('data/day7.sample')]
lines = [ l.strip() for l in open('data/day7')]

filesize_in_dir = dict()

path = []

for line in lines:
    args = line.split(' ')

    if args[0] == '$' and args[1] == 'cd':
        if args[2] == '/':
            path = []
        elif args[2] == '..':
            path = path[:-1]
        else:
            path.append(args[2])

        flatpath = '/'.join(path)
        filesize_in_dir.setdefault(flatpath, 0)

    elif args[0] == '$' and args[1] == 'ls':
        pass
    elif args[0] != 'dir':
        flatpath = '/'.join(path)
        filesize_in_dir[flatpath] = filesize_in_dir.get(flatpath, 0) + int(args[0])

#print(filesize_in_dir)

total_in_dir = dict()

def is_sub(parent, child):
    if parent == '': return True
    return (child + '/').startswith(parent + '/')
        

for path in filesize_in_dir.keys():
    for path2 in filesize_in_dir.keys():
        if is_sub(path, path2):
            total_in_dir[path] = total_in_dir.get(path, 0) + filesize_in_dir.get(path2, 0)



#print(total_in_dir)

smalldirs = 0
for p in total_in_dir.keys():
    print(p, total_in_dir[p])
    if total_in_dir[p] <= 100000:
        smalldirs += total_in_dir[p]


print(smalldirs)


total_disk_space = 70000000
needed = 30000000
used = total_in_dir['']

candidates = []
best = ''
best_size = used
for p in total_in_dir.keys():
    used_after_delete = used - total_in_dir[p]
    if used_after_delete < total_disk_space - needed:
        if total_in_dir[p] < best_size:
            best_size = total_in_dir[p]
            best = p

print(best, best_size)



