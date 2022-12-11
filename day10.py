import numpy as np

TEST = [
    "addx 15",
    "addx -11",
    "addx 6",
    "addx -3",
    "addx 5",
    "addx -1",
    "addx -8",
    "addx 13",
    "addx 4",
    "noop",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx -35",
    "addx 1",
    "addx 24",
    "addx -19",
    "addx 1",
    "addx 16",
    "addx -11",
    "noop",
    "noop",
    "addx 21",
    "addx -15",
    "noop",
    "noop",
    "addx -3",
    "addx 9",
    "addx 1",
    "addx -3",
    "addx 8",
    "addx 1",
    "addx 5",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx -36",
    "noop",
    "addx 1",
    "addx 7",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "addx 6",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx 7",
    "addx 1",
    "noop",
    "addx -13",
    "addx 13",
    "addx 7",
    "noop",
    "addx 1",
    "addx -33",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "noop",
    "noop",
    "noop",
    "addx 8",
    "noop",
    "addx -1",
    "addx 2",
    "addx 1",
    "noop",
    "addx 17",
    "addx -9",
    "addx 1",
    "addx 1",
    "addx -3",
    "addx 11",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx -13",
    "addx -19",
    "addx 1",
    "addx 3",
    "addx 26",
    "addx -30",
    "addx 12",
    "addx -1",
    "addx 3",
    "addx 1",
    "noop",
    "noop",
    "noop",
    "addx -9",
    "addx 18",
    "addx 1",
    "addx 2",
    "noop",
    "noop",
    "addx 9",
    "noop",
    "noop",
    "noop",
    "addx -1",
    "addx 2",
    "addx -37",
    "addx 1",
    "addx 3",
    "noop",
    "addx 15",
    "addx -21",
    "addx 22",
    "addx -6",
    "addx 1",
    "noop",
    "addx 2",
    "addx 1",
    "noop",
    "addx -10",
    "noop",
    "noop",
    "addx 20",
    "addx 1",
    "addx 2",
    "addx 2",
    "addx -6",
    "addx -11",
    "noop",
    "noop",
    "noop"
    ]

def draw_pixel(X, cycle, screen):
    i = (cycle - 1) // 40
    j = (cycle - 1) % 40
    screen[i,j] = abs(X - ((cycle - 1) % 40)) <= 1
    c = '#' if screen[i,j] else '.'

def iterate(actions):
    X = 1
    cycle = 1
    signal_strength = 0
    screen = np.zeros((6,40))
    for action in actions:
        if action == "noop":
            if (cycle - 20) % 40 == 0:
                signal_strength += X * cycle
            draw_pixel(X, cycle, screen)
            cycle += 1
        else:
            for _ in range(2):
                if (cycle - 20) % 40 == 0:
                    signal_strength += X * (cycle - ((cycle - 20) % 40))
                draw_pixel(X, cycle, screen)
                cycle += 1
            X += int(action[len("addx "):])
    return signal_strength, screen

def print_screen(screen):
    for i in range(6):
        for j in range(40):
            char = '#' if screen[i,j] else '.'
            print(char, end="")
        print("")

with open("inputs/day10.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

signal_strength, screen = iterate(TEST)
#  print_screen(screen)
assert signal_strength == 13140

signal_strength, screen = iterate(contents)
print(signal_strength)
print_screen(screen)
