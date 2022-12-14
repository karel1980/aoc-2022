from numpy import sign

#grid = [ [int(i) for i in list(l.strip())] for l in open('data/day8.sample').readlines() ]
grid = [ [int(i) for i in list(l.strip())] for l in open('data/day8').readlines() ]

height = len(grid)
width = len(grid[0])

result = [ [False for i in row] for row in grid ]













NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, -1)
WEST = (0, 1)

def visible_from_side(r, c, side, grid):
    t = grid[r][c]

    r += side[0]
    c += side[1]

    while r >= 0 and r < height and c >= 0 and c < width:
        if grid[r][c] >= t:
            return False
        r += side[0]
        c += side[1]

    return True


def is_visible(row, col, grid):
    return visible_from_side(row, col, NORTH, grid) or visible_from_side(row, col, SOUTH, grid) or visible_from_side(row, col, EAST, grid) or visible_from_side(row, col, WEST, grid)

visible_count = 0
for row in range(height):
    for col in range(width):
        result[row][col] = is_visible(row, col, grid)
        visible_count += 1 if is_visible(row, col, grid) else 0

print(result)
#print(visible_from_side(0, 0, 0, 1, grid))
#print(visible_from_side(2, 0, 2, 2, grid))

print(visible_count)

#print(is_visible(1, 3, grid))

def count_trees(r, c, direction, grid):
    tree = grid[r][c]
    blocked = False
    count = 0
    r += direction[0]
    c += direction[1]
    while r >= 0 and r < height and c >= 0 and c < width and not blocked:
        count += 1
        if grid[r][c] >= tree:
            blocked = True
        r += direction[0]
        c += direction[1]

    return count

def scenic_score(r, c, grid):
    result = 1
    result *= count_trees(r, c, NORTH, grid)
    result *= count_trees(r, c, SOUTH, grid)
    result *= count_trees(r, c, EAST, grid)
    result *= count_trees(r, c, WEST, grid)

    return result

best_scenic = -1
for row in range(height):
    for col in range(width):
        s = scenic_score(row, col, grid)
        if s > best_scenic:
            best_scenic = s

print(best_scenic)
