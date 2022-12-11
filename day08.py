import numpy as np

with open("inputs/day8.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

TEST = [ "30373", "25512", "65332", "33549", "35390" ]

def to_canopy(data):
    rows = len(data)
    cols = len(data[0])
    canopy = []
    for r in range(rows):
        canopy.append([])
        for c in range(cols):
            canopy[r].append(int(data[r][c]))
    return np.array(canopy)

def count_visible(canopy):
    rows, cols = canopy.shape
    visible = 0
    for r in range(rows):
        for c in range(cols):
            tree = canopy[r,c]
            left = np.all(canopy[r, :c] < tree)
            right = np.all(canopy[r, c+1:] < tree)
            up = np.all(canopy[:r, c] < tree)
            down = np.all(canopy[r+1:, c] < tree)
            if left or right or up or down:
                visible += 1
    return visible

def viewing_distance(height, trees):
    distance = 0
    for tree in trees:
        distance += 1
        if tree >= height:
            break
    return distance

def scenic_score(canopy, r, c):
    tree = canopy[r,c]
    left = viewing_distance(tree, np.flip(canopy[r, :c]))
    right = viewing_distance(tree, canopy[r, c+1:])
    up = viewing_distance(tree, np.flip(canopy[:r, c]))
    down = viewing_distance(tree, canopy[r+1:, c])
    return left * right * up * down

def best_scenic_score(canopy):
    rows, cols = canopy.shape
    best_score = 0
    for r in range(rows):
        for c in range(cols):
            best_score = max(best_score, scenic_score(canopy, r, c))
    return best_score

test_canopy = to_canopy(TEST)
assert count_visible(test_canopy) == 21
assert scenic_score(test_canopy, 1, 2) == 4
assert best_scenic_score(test_canopy) == 8

canopy = to_canopy(contents)
print(count_visible(canopy))
print(best_scenic_score(canopy))
