with open("inputs/day6.txt") as file:
    contents = file.read()

#  contents = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

marker = []
start_of_marker = 0
start_of_message = 0
for i, c in enumerate(contents):
    marker.append(c)
    if len(marker) > 14:
        marker = marker[-14:]
    if len(set(marker[-4:])) == 4 and start_of_marker == 0:
        start_of_marker = i+1
    if len(set(marker)) == 14:
        start_of_message = i+1
        break

print(start_of_marker)
print(start_of_message)
