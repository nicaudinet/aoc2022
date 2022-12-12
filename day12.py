import networkx as nx

with open("inputs/day12.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

TEST = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
    ]

def build_height_map(contents):
    rows = len(contents)
    cols = len(contents[0])
    height_map = []
    starts = []
    for r in range(rows):
        height_map.append([])
        for c in range(cols):
            char = contents[r][c]
            if char == "S":
                height_map[r].append(0)
                start = r * cols + c
                starts.append(start)
            elif char == "E":
                height_map[r].append(26)
                end = r * cols + c
            elif char == "a":
                height_map[r].append(0)
                starts.append(r * cols + c)
            else:
                height_map[r].append(ord(char) - ord("a"))
    return height_map, start, end, starts

def neighborhood(point, rows, cols):
    px, py = point
    neighbors = [(px+1, py), (px-1, py), (px, py+1), (px, py-1)]
    in_map = lambda a: a[0] >= 0 and a[0] < rows and a[1] >= 0 and a[1] < cols
    return filter(in_map, neighbors)

def build_graph(height_map):
    rows = len(height_map)
    cols = len(height_map[0])
    graph = nx.DiGraph()
    for r in range(rows):
        for c in range(cols):
            curr_height = height_map[r][c]
            curr_id = r * cols + c
            for neighbor in neighborhood((r,c), rows, cols):
                x, y = neighbor
                #  print(r,c)
                if height_map[x][y] <= curr_height + 1:
                    n_id = x * cols + y
                    graph.add_edge(curr_id, n_id)
    return graph

def shortest_path_length(contents):
    height_map, start, end, _ = build_height_map(contents)
    graph = build_graph(height_map)
    return nx.shortest_path_length(graph, start, end)

def absolute_shortest_path_length(contents):
    height_map, _, end, starts = build_height_map(contents)
    graph = build_graph(height_map)
    lens = []
    for start in starts:
        try:
            lens.append(nx.shortest_path_length(graph, start, end))
        except:
            pass
    return min(lens)

assert shortest_path_length(TEST) == 31
print(shortest_path_length(contents))

assert absolute_shortest_path_length(TEST) == 29
print(absolute_shortest_path_length(contents))
