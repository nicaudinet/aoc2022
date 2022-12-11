import copy

def parse_move(move):
    num_crates = move[len("move "):-len(" from x to x")]
    origin = move[-len(" to x")-1]
    destination = move[-1]
    return (int(num_crates), int(origin)-1, int(destination)-1)

def play_move(move, stacks, reverse):
    n, o, d = move
    o_stack = copy.copy(stacks[o])
    stacks[o] = o_stack[:-n]
    if reverse:
        o_stack.reverse()
        stacks[d] += o_stack[:n]
    else:
        stacks[d] += o_stack[-n:]
    return stacks

with open("inputs/day5.txt") as file:
    contents = file.readlines()
    moves = list(filter(lambda x: x[0] == 'm', contents))
    moves = list(map(lambda x: parse_move(x.strip()), moves))

s1 = ['D','H','N','Q','T','W','V','B']
s2 = ['D','W','B']
s3 = ['T','S','Q','W','J','C']
s4 = ['F','J','R','N','Z','T','P']
s5 = ['G','P','V','J','M','S','T']
s6 = ['B','W','F','T','N']
s7 = ['B','L','D','Q','F','H','V','N']
s8 = ['H','P','F','R']
s9 = ['Z','S','M','B','L','N','P','H']

stacks = copy.deepcopy([s1,s2,s3,s4,s5,s6,s7,s8,s9])
for move in moves:
    play_move(move, stacks, reverse=True)
tops = ''.join(map(lambda x: x[-1], stacks))
print(tops)

stacks = copy.deepcopy([s1,s2,s3,s4,s5,s6,s7,s8,s9])
for move in moves:
    play_move(move, stacks, reverse=False)
tops = ''.join(map(lambda x: x[-1], stacks))
print(tops)
