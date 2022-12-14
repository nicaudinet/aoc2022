import ast

def points_between(start, end):
    sx, sy = start
    ex, ey = end
    if sx == ex:
        return [(sx, i) for i in range(min(sy, ey), max(sy, ey)+1)]
    if sy == ey:
        return [(i, sy) for i in range(min(sx, ex), max(sx, ex)+1)]

def process_path(path, terrain):
    points = path.split(" -> ")
    points = list(map(lambda x: ast.literal_eval(x), points))
    start = points[0]
    for end in points[1:]:
        for point in points_between(start, end):
            terrain[point] = 'rock'
        start = end

def process_terrain(contents):
    terrain = {}
    for path in contents:
        process_path(path, terrain)
    return terrain

def at_rest(pos, terrain):
    px, py = pos
    under = [(px-1, py+1), (px, py+1), (px+1, py+1)]
    for point in under:
        if point not in terrain:
            return False
    return True

def move(pos, terrain):
    px, py = pos
    under = (px, py+1)
    if under not in terrain:
        return under
    under_left = (px-1, py+1)
    if under_left not in terrain:
        return under_left
    under_right = (px+1, py+1)
    if under_right not in terrain:
        return under_right
    assert False

def drop_grain(terrain, max_height):
    pos = (500,0)
    while True:
        if pos[1] > max_height:
            return terrain, True
        if at_rest(pos, terrain):
            terrain[pos] = 'sand'
            return terrain, False
        pos = move(pos, terrain)

def pour_sand(terrain):
    stop = False
    max_height = max(list(map(lambda x: x[1], terrain.keys())))
    while not stop:
        terrain, stop = drop_grain(terrain, max_height)
    return terrain

def count_sand(terrain):
    return len(list(filter(lambda x: x == 'sand', terrain.values())))

def compute_sand_pour(contents):
    terrain = process_terrain(contents)
    terrain = pour_sand(terrain)
    return count_sand(terrain)

with open("inputs/day14.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

TEST = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
    ]

assert compute_sand_pour(TEST) == 24
print(compute_sand_pour(contents))

def at_rest(pos, terrain, max_height):
    px, py = pos
    if py == max_height:
        return True
    under = [(px-1, py+1), (px, py+1), (px+1, py+1)]
    for point in under:
        if point not in terrain:
            return False
    return True

def drop_grain(terrain, max_height):
    pos = (500,0)
    while True:
        if at_rest(pos, terrain, max_height + 1):
            terrain[pos] = 'sand'
            return terrain, (pos == (500,0))
        pos = move(pos, terrain)

assert compute_sand_pour(TEST) == 93
print(compute_sand_pour(contents))
