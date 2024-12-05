def part_1():
    stack_left = []
    stack_right = []

    # read input
    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := [*map(int, h.readline().strip().split())]):
            stack_left.append(l[0])
            stack_right.append(l[1])
            
    stack_left = sorted(stack_left)
    stack_right = sorted(stack_right)
    
    return sum([abs(k - v) for k, v in ((stack_left[i], stack_right[i]) for i in range(len(stack_left)))])

def part_2():
    stack_left = []
    stack_right = []

    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := h.readline().strip().split()):
            stack_left.append(int(l[0]))
            stack_right.append(int(l[1]))
    
    return sum([x * stack_right.count(x) for x in stack_left])

def part_2t():
    stack_left = []
    stack_right = []

    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := [( _ := stack_left.append(i[0])) or stack_right.append(i[1]) for i in h.readline().strip().split()]): pass
    
    return sum([int(x) * stack_right.count(x) for x in stack_left])

print(part_1())
print(part_2())
