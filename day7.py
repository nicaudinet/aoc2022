import sys

sys.setrecursionlimit(10000)

with open("inputs/day7.txt") as file:
    commands = file.readlines()
    commands = list(map(lambda s: s.strip(), commands))
    commands = commands[1:]

TEST = [
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k"
    ]

class File:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = 0

    def is_file(self):
        return len(self.children) == 0

class FileSystem:
    def __init__(self, commands):
        self.commands = commands
        self.dirs = []
        self.root = self.build_tree()
        self.compute_sizes(self.root)

    def build_ls(self, curr):
        while self.commands:
            if self.commands[0][0] == "$":
                break
            line = self.commands.pop(0)
            if line[:len("dir")] == "dir":
                name = line[len("dir "):]
                file = File(name, curr)
                curr.children[name] = file
                self.dirs.append(file)
            else:
                size, name = line.split(" ")
                file = File(name, curr)
                file.size = int(size)
                curr.children[name] = file

    def build_tree(self):
        curr = File('/', None)
        self.dirs.append(curr)
        while self.commands:
            command = self.commands.pop(0)
            if command[:len("$ cd")] == "$ cd":
                dirname = command[len("$ cd "):]
                if dirname == "..":
                    curr = curr.parent
                else:
                    curr = curr.children[dirname]
            if command == "$ ls":
                self.build_ls(curr)
        while curr.parent:
            curr = curr.parent
        return curr

    def compute_sizes(self, curr):
        for child in curr.children.values():
            if child.is_file():
                curr.size += child.size
            else:
                curr.size += self.compute_sizes(child)
        return curr.size
    
    def print_node(self, node, depth):
        print(depth * "  " + node.name)
        for child in node.children.values():
            if child.is_file():
                print((depth + 1) * "  " + child.name)
            else:
                self.print_node(child, depth + 1)

    def print(self):
        self.print_node(self.root, 0)

def sum_small_dirs(dirs):
    small_dirs = filter(lambda d: d.size < 100000, dirs)
    return sum(map(lambda d: d.size, small_dirs))

fs = FileSystem(TEST)
assert sum_small_dirs(fs.dirs) == 95437
assert 70000000 - fs.root.size == 21618835

fs = FileSystem(commands)
print(sum_small_dirs(fs.dirs))

free_space = 70000000 - fs.root.size
need_to_free = 30000000 - free_space
print(min([d.size for d in fs.dirs if d.size >= need_to_free]))
