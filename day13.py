#lines = [ l .strip() for l in open('data/day13.sample').readlines()]
lines = [ l .strip() for l in open('data/day13').readlines()]

def compare(left, right, indent = 0):
    print(" "*indent, "Compare", left, "vs", right)
    if type(left) == int and type(right) == int:
        if left < right: 
            print(" " * indent, "left side is smaller, in order")
            return 1
        if left > right: 
            print(" " * indent, "right side is smaller, NOT in order")
            return -1
        if left == right: 
            print(" " * indent, "compare next")
            return 0

    if type(left) == int:
        print(" "*indent, "wrapping left in list")
        return compare([left], right, indent + 2)

    if type(right) == int:
        print(" "*indent, "wrapping right in list")
        return compare(left, [right], indent + 2)

    for i in range(len(left)):
        if i >= len(right):
            print(" "*indent, "right ran out of items")
            return -1 # right ran out of items

        cmp = compare(left[i], right[i], indent + 2)
        if cmp != 0: return cmp
        
    if len(left) == len(right):
        print(" " * indent, "identical lists")
        return 0
    else:
        print(" "*indent, "left ran out of items")
        return 1 # left ran out of items before right

pair_index = 0
sum_in_order_indices = 0
for i in range(0, len(lines), 3):
    pair_index += 1

    left = eval(lines[i])
    right = eval(lines[i+1])

    print(left, right)

    print("pair",pair_index,left,right)
    cmp = compare(left, right)
    print("in order?", cmp, cmp != -1)
    if cmp == 1:
        sum_in_order_indices+=pair_index


print(sum_in_order_indices)
