#grid = [ l.strip() for l in open('data/day12.sample').readlines() ]
grid = [ l.strip() for l in open('data/day12').readlines() ]
height = len(grid)
width = len(grid[0])

scores = [ [ -1 for col in range(width) ] for row in range(height)]

S = ()
E = ()

for row in range(height):
    for col in range(width):
        if grid[row][col] == 'S':
            S = (row, col)
        if grid[row][col] == 'E':
            E = (row, col)

print("S", S)
print("E", E)

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

def neighbors(pos):
    all = [(pos[0]+d[0], pos[1]+d[1]) for d in (UP, DOWN, LEFT, RIGHT)]
    possible = list(filter(lambda n: n[0] >= 0 and n[0] < height and n[1] >= 0 and n[1] < width, all))
    marker = grid[pos[0]][pos[1]]
    if marker == 'S':
        current = ord('a')-1
    elif marker == 'E':
        current = ord('z')+1
    else: current = ord(marker)
    
    allowed = list(filter(lambda n: (ord('z')+1 if grid[n[0]][n[1]] == 'E' else ord(grid[n[0]][n[1]])) <= current + 1, possible))
    result = list(filter(lambda n: scores[n[0]][n[1]] == -1, allowed))
    print("candidates from ",pos, result)
    return result

dist = 0
candidates = []
for row in range(height):
    for col in range(width):
        if grid[row][col] in ['S','a']:
            scores[row][col] = 0
            candidates.append((row,col))

    

for p in candidates:
    scores[p[0]][p[1]] = 0

while len(candidates) > 0:
    pos = candidates[0]
    candidates = candidates[1:]
    for n in neighbors(pos):
        if scores[n[0]][n[1]] == -1:
            # not visited yet -> set score and add to candidates
            scores[n[0]][n[1]] = scores[pos[0]][pos[1]] + 1
            candidates.append(n)
            


for row in scores:
    print(row)
print (scores[E[0]][E[1]])
