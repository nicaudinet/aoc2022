import ast
from functools import reduce, cmp_to_key
import copy

with open("inputs/day13.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

TEST = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]"
    ]

def parse_contents(contents):
    pairs = []
    for i in range(0, len(contents), 3):
        left = ast.literal_eval(contents[i])
        right = ast.literal_eval(contents[i+1])
        pairs.append((left,right))
    return pairs

def correct_order(pair):
    left, right = pair
    while left:
        if right == []:
            return False
        l = left.pop(0)
        r = right.pop(0)
        if type(l) == int and type(r) == int:
            if l == r:
                continue
            return l < r
        elif type(l) == list and type(r) == list:
            if l == r:
                continue
            else:
                return correct_order((l, r))
        elif type(l) == list and type(r) == int:
            r = [r]
            if l == r:
                continue
            else:
                return correct_order((l, r))
        elif type(l) == int and type(r) == list:
            l = [l]
            if l == r:
                continue
            else:
                return correct_order((l, r))
    return True

def sum_indices(pairs):
    sum = 0
    for i, pair in enumerate(pairs):
        if correct_order(pair):
            sum += i + 1
    return sum

def compare(a,b):
    pair = (copy.deepcopy(a), copy.deepcopy(b))
    if a == b:
        return 0
    elif correct_order(pair):
        return -1
    else:
        return 1

def sort_packets(pairs):
    packets = list(reduce(lambda a, b: a + b, pairs))
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(compare))
    i1 = packets.index([[2]]) + 1
    i2 = packets.index([[6]]) + 1
    return i1 * i2

assert sum_indices(parse_contents(TEST)) == 13
print(sum_indices(parse_contents(contents)))

assert sort_packets(parse_contents(TEST)) == 140
print(sort_packets(parse_contents(contents)))
