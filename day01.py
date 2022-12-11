with open("inputs/day01.txt") as file:
    lines = file.readlines()

lines = list(map(lambda s: s.strip(), lines))

elves = []
elf = []
for line in lines:
    if line == '':
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

calories = list(map(sum, elves))
print(max(calories))

calories.sort()
print(sum(calories[-3:]))
