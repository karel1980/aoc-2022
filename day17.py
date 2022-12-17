blocks =  []

blocks.append ( ["####"])
blocks.append ( [".#.","###",".#."])
blocks.append ( ["..#","..#","###"])
blocks.append ( ["#","#","#","#"])
blocks.append ( ["##", "##"])

class Block:
    def __init__(self, spec, current_level):
        print("creating block with spec", spec, "current level", current_level)
        self.spec = spec
        self.x = 2
        self.y = current_level + len(spec) + 3 - 1
        self.width = max([len(l) for l in spec])

    def left(self):
        if self.can_be_at(self.x-1, self.y, world):
            self.x -= 1

    def right(self):
        if self.can_be_at(self.x+1, self.y, world):
            self.x += 1

    def down(self, world):
        if self.can_be_at(self.x, self.y-1, world):
            self.y -= 1
            return True

        return False

    def write(self, world):
        # add rows to world:
        #print("writing", self.y, world)
        while len(world) < self.y + 1:
            #print("growing world")
            world.append('..................')

        #print("writing", self.spec, self.x, self.y, world)
        for row in range(len(self.spec)):
            line = self.y - row
            chars = list(world[line])
            for col in range(self.width):
                if self.spec[row][col] == '#':
                    chars[self.x + col] = '#'

            world[line] = ''.join(chars)

    def can_be_at(self, x, y, world):
        #print("can_be_at", x, y, self.width)
        if x < 0:
            #print('off to the left')
            return False
        if x + self.width > 7:
            #print('off to the right')
            return False

        if y < len(self.spec) - 1:
            return False

        for row in range(len(self.spec)):
            for col in range(len(self.spec[row])):
                cx = x + col
                cy = y - row
                if self.spec[row][col] == '#' and cy < len(world) and cx < len(world[cy]) and world[cy][cx] == '#':
                    return False

        return True


world = []

#gusts = [ l.strip() for l in open('data/day17.sample').readlines() ][0]
gusts = [ l.strip() for l in open('data/day17').readlines() ][0]
gust_idx = 0

fallen = 0

def apply_gust(gust, world, block):
    if gust == '<':
        block.left()
    else: block.right()

def fall(world, block):
    result = block.down(world)
    if not result:
        block.write(world)

    return result

while fallen < 2022:
    block_spec = blocks[fallen % len(blocks)]
    block = Block(block_spec, len(world))
    
    stopped = False
    while not stopped:
        print("block", fallen)
        print("block starts at ", block.x, block.y)
        apply_gust(gusts[gust_idx%len(gusts)], world, block)
        print("after gust", gusts[gust_idx%len(gusts)], block.x, block.y)
        gust_idx += 1
        stopped = not fall(world, block)
        print("after fall", block.x, block.y)
          

    #for line in range(len(world)-1, -1, -1):
    #    print(world[line])

    fallen +=1

    
print(len(world))
