import math
from functools import reduce
import copy

# Test monkeys

mt0 = {
        'items': [79, 98],
        'operation': lambda x: x * 19,
        'mod': 23,
        'test': lambda x: 2 if x % mt0['mod'] == 0 else 3,
        'activity': 0
        }

mt1 = {
        'items': [54, 65, 75, 74],
        'operation': lambda x: x + 6,
        'mod': 19,
        'test': lambda x: 2 if x % mt1['mod'] == 0 else 0,
        'activity': 0
        }

mt2 = {
        'items': [79, 60, 97],
        'operation': lambda x: x * x,
        'mod': 13,
        'test': lambda x: 1 if x % mt2['mod'] == 0 else 3,
        'activity': 0
        }

mt3 = {
        'items': [74],
        'operation': lambda x: x + 3,
        'mod': 17,
        'test': lambda x: 0 if x % mt3['mod'] == 0 else 1,
        'activity': 0
        }

TEST = [mt0, mt1, mt2, mt3]


# Real monkeys

m0 = {
        'items': [54, 82, 90, 88, 86, 54],
        'operation': lambda x: x * 7,
        'mod': 11,
        'test': lambda x: 2 if x % m0['mod'] == 0 else 6,
        'activity': 0
        }

m1 = {
        'items': [91, 65],
        'operation': lambda x: x * 13,
        'mod': 5,
        'test': lambda x: 7 if x % m1['mod'] == 0 else 4,
        'activity': 0
        }

m2 = {
        'items': [62, 54, 57, 92, 83, 63, 63],
        'operation': lambda x: x + 1,
        'mod': 7,
        'test': lambda x: 1 if x % m2['mod'] == 0 else 7,
        'activity': 0
        }

m3 = {
        'items': [67, 72, 68],
        'operation': lambda x: x * x,
        'mod': 2,
        'test': lambda x: 0 if x % m3['mod'] == 0 else 6,
        'activity': 0
        }

m4 = {
        'items': [68, 89, 90, 86, 84, 57, 72, 84],
        'operation': lambda x: x + 7,
        'mod': 17,
        'test': lambda x: 3 if x % m4['mod'] == 0 else 5,
        'activity': 0
        }

m5 = {
        'items': [79, 83, 64, 58],
        'operation': lambda x: x + 6,
        'mod': 13,
        'test': lambda x: 3 if x % m5['mod'] == 0 else 0,
        'activity': 0
        }

m6 = {
        'items': [96, 72, 89, 70, 88],
        'operation': lambda x: x + 4,
        'mod': 3,
        'test': lambda x: 1 if x % m6['mod'] == 0 else 2,
        'activity': 0
        }

m7 = {
        'items': [79],
        'operation': lambda x: x + 8,
        'mod': 19,
        'test': lambda x: 4 if x % m7['mod'] == 0 else 5,
        'activity': 0
        }

ACTUAL = [m0, m1, m2, m3, m4, m5, m6, m7]


# Part 1

def aim_item(monkey):
    item = monkey['items'].pop(0)
    item = monkey['operation'](item)
    item = item // 3
    monkey['activity'] += 1
    return item, monkey['test'](item)

def play_turn(monkey, monkeys):
    while monkey['items']:
        item, target = aim_item(monkey)
        monkeys[target]['items'].append(item)

def play_round(monkeys):
    for monkey in monkeys:
        play_turn(monkey, monkeys)

monkeys = copy.deepcopy(TEST)
for _ in range(20):
    play_round(monkeys)
activities = sorted([monkey['activity'] for monkey in monkeys], reverse=True)
assert (activities[0] * activities[1]) == 10605

monkeys = copy.deepcopy(ACTUAL)
for _ in range(20):
    play_round(monkeys)
activities = sorted([monkey['activity'] for monkey in monkeys], reverse=True)
print(activities[0] * activities[1])


# Part 2

# from Rosetta code
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# from Rosetta code
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def prepare_monkeys(monkeys):
    mods = [m['mod'] for m in monkeys]
    for monkey in monkeys:
        monkey['items_mod'] = []
        for item in monkey['items']:
            remainder = chinese_remainder(mods, [item % mod for mod in mods])
            monkey['items_mod'].append(remainder)

def aim_item(monkey, lcm):
    item = monkey['items_mod'].pop(0)
    item = monkey['operation'](item) % lcm
    monkey['activity'] += 1
    return item, monkey['test'](item)

def play_turn(monkey, monkeys, lcm):
    while monkey['items_mod']:
        item, target = aim_item(monkey, lcm)
        monkeys[target]['items_mod'].append(item)

def play_round(monkeys):
    lcm = reduce(lambda a, b: a * b, [m['mod'] for m in monkeys])
    for monkey in monkeys:
        play_turn(monkey, monkeys, lcm)

monkeys = copy.deepcopy(TEST)
prepare_monkeys(monkeys)
for _ in range(10000):
    play_round(monkeys)
activities = sorted([monkey['activity'] for monkey in monkeys], reverse=True)
assert (activities[0] * activities[1]) == 2713310158

monkeys = copy.deepcopy(ACTUAL)
prepare_monkeys(monkeys)
for _ in range(10000):
    play_round(monkeys)
activities = sorted([monkey['activity'] for monkey in monkeys], reverse=True)
print(activities[0] * activities[1])
