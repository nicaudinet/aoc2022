import copy

def parse_sensor(line):
    sx = int(line.split("x=")[1].split(",")[0])
    sy = int(line.split("y=")[1].split(":")[0])
    bx = int(line.split("x=")[2].split(",")[0])
    by = int(line.split("y=")[2])
    return (sx,sy), (bx,by)

def manhattan(p,q):
    px, py = p
    qx, qy = q
    return abs(px-qx) + abs(py-qy)

def process_beacons(lines):
    beacons = set()
    distance_map = {}
    for line in lines:
        sensor, beacon = parse_sensor(line)
        beacons.add(beacon)
        distance_map[sensor] = manhattan(sensor, beacon)
    return beacons, distance_map

class Range:
    def __init__(self, lower, upper):
        assert lower <= upper
        self.lower = lower
        self.upper = upper 

    def __repr__(self):
        return str((self.lower, self.upper))

    def __lt__(self, r):
        return self.lower < r.lower

    def num_points(self):
        return self.upper - self.lower + 1

    def in_range(self, value):
        return self.lower <= value and self.upper >= value

def in_ranges(val, ranges):
    return any([r.in_range(val) for r in ranges])

def compute_ranges(row, distance_map):
    ranges = []
    for sensor in distance_map.keys():
        sx, sy = sensor
        if abs(row - sy) <= distance_map[sensor]:
            lower = sx - distance_map[sensor] + abs(sy - row)
            upper = sx + distance_map[sensor] - abs(sy - row)
            ranges.append(Range(lower, upper))
    return ranges

def simplify_ranges(ranges):
    ranges = sorted(copy.deepcopy(ranges))
    curr = ranges[0]
    simplified_ranges = []
    for r in ranges[1:]:
        if curr.upper >= r.lower:
            if curr.upper <= r.upper:
                curr = Range(curr.lower, r.upper)
        else:
            simplified_ranges.append(curr)
    simplified_ranges.append(curr)
    return simplified_ranges

def compute_non_present(row, ranges, beacons):
    range_sum = sum([r.num_points() for r in ranges])
    valid = lambda b: b[1] == row and in_ranges(b[0], ranges)
    beacons_in_range = len([b for b in beacons if valid(b)])
    return range_sum - beacons_in_range

def cannot_be_present(row, beacons, distance_map):
    ranges = compute_ranges(row, distance_map)
    ranges = simplify_ranges(ranges)
    return compute_non_present(row, ranges, beacons)

def tuning_frequency(max_x, max_y, beacons, distance_map):
    for row in range(max_y):
        ranges = compute_ranges(row, distance_map)
        ranges = simplify_ranges(ranges)
        if len(ranges) > 1:
            return (ranges[0].upper + 1) * 4000000 + row

with open("inputs/day15.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

TEST = [
    "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3"
    ]

test_beacons, test_distance_map = process_beacons(TEST)
assert cannot_be_present(10, test_beacons, test_distance_map) == 26
beacons, distance_map = process_beacons(contents)
print(cannot_be_present(2000000, beacons, distance_map))

assert tuning_frequency(20, 20, test_beacons, test_distance_map) == 56000011
print(tuning_frequency(4000000, 4000000, beacons, distance_map))
