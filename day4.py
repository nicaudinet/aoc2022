with open("inputs/day4.txt") as file:
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(), contents))

count_1 = 0
count_2 = 0
for pair in contents:
    (first, second) = pair.split(',')
    (start_1, end_1) = map(int, first.split('-'))
    (start_2, end_2) = map(int, second.split('-'))

    first_in_second = start_1 >= start_2 and end_1 <= end_2
    second_in_first = start_2 >= start_1 and end_2 <= end_1
    if first_in_second or second_in_first:
        count_1 += 1

    first_overlap_left = start_1 <= start_2 and end_1 >= start_2
    first_overlap_right = start_1 <= end_2 and end_1 >= end_2
    first_in_second = start_1 > start_2 and end_1 < end_2
    second_in_first = start_2 > start_1 and end_2 < end_1
    if first_overlap_left or first_overlap_right or first_in_second or second_in_first:
        count_2 += 1

print(count_1)
print(count_2)
