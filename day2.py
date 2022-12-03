with open("inputs/day2.txt") as file:
    lines = file.readlines()

#  lines = ["A Y", "B X", "C Z"] 

score = 0
for line in lines:
    m1 = ord(line[0]) - ord("A")
    m2 = ord(line[2]) - ord("X")

    score += m2 + 1

    if m1 == (m2 - 1) % 3:
        score += 6
    if m1 == m2:
        score += 3

print(score)

score = 0
for line in lines:
    m1 = ord(line[0]) - ord("A")
    m2 = ord(line[2]) - ord("X")

    score += m2 * 3

    if m2 == 0:
        score += (m1 - 1) % 3 + 1
    if m2 == 1:
        score += m1 + 1
    if m2 == 2:
        score += (m1 + 1) % 3 + 1

print(score)
