import itertools

def move_head(head, action):
    hx, hy = head
    if action == "R":
        hx += 1
    elif action == "L":
        hx -= 1
    elif action == "U":
        hy += 1
    elif action == "D":
        hy -= 1
    return (hx, hy)

def move_tail(tail, head):
    hx, hy = head
    tx, ty = tail
    # Don't move if close enough
    if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
        return tail
    # Move up or down if on same column
    if tx == hx:
        ty += 1 if ty < hy else -1
        return (tx, ty)
    # Move right or left if on same row
    if ty == hy:
        tx += 1 if tx < hx else -1
        return (tx, ty)
    # Move diagonally towards h
    tx += 1 if tx < hx else -1
    ty += 1 if ty < hy else -1
    return (tx, ty)

def simulate_rope(actions):
    head = (0,0)
    tails = list(itertools.repeat((0,0), 9))
    first_tail_positions = set()
    last_tail_positions = set()
    for action in actions:
        for _ in range(int(action[2:])):
            head = move_head(head, action[0])
            tails[0] = move_tail(tails[0], head)
            for i,tail in enumerate(tails[1:]):
                tails[i+1] = move_tail(tail, tails[i])
            first_tail_positions.add(tails[0])
            last_tail_positions.add(tails[8])
            #  print(head, tail, set(tail_positions))
    return len(first_tail_positions), len(last_tail_positions)

with open("inputs/day09.txt") as file:
    actions = file.readlines()
    actions = map(lambda x: x.strip(), actions)

TEST = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"
    ]

first, last = simulate_rope(TEST)
assert first == 13
assert last == 1

TEST = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20"
    ]

first, last = simulate_rope(TEST)
assert last == 36

first, last = simulate_rope(actions)
print(first)
print(last)
