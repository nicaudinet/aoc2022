with open("inputs/day3.txt") as file:
    rucksacks = file.readlines()
    rucksacks = list(map(lambda x: x.strip(), rucksacks))

counter = 0
for r in rucksacks:
    split_index = len(r) // 2
    p1, p2 = set(r[:split_index]), set(r[split_index:])
    diff = p1.difference(p1.difference(p2))
    item = ord(list(diff)[0])
    if item <= ord('Z'):
        counter += item - ord('A') + 27
    else:
        counter += item - ord('a') + 1
print(counter)


def chunk(l,n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

counter = 0
groups = list(chunk(rucksacks,3))
for group in groups:
    s1, s2, s3 = map(set, group)
    diff = s2.difference(s2.difference(s1))
    diff = s3.difference(s3.difference(diff))
    item = ord(list(diff)[0])
    #  print(chr(item))
    if item <= ord('Z'):
        counter += item - ord('A') + 27
    else:
        counter += item - ord('a') + 1
print(counter)
