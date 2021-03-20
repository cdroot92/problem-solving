import sys
from datetime import time


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def read_str(line):
    return line.strip()


def check_space(space, size, x, y):
    x_to = x + size
    y_to = y + size
    if x_to > len(space) or y_to > len(space):
        return False
    for i in range(x, x_to):
        for j in range(y, y_to):
            if space[i][j] == "0":
                return False
    return True


lines = sys.stdin.readlines()

n = read_a_num(lines[0])
space = []
for line in lines[1 : n + 1]:
    space.append(read_str(line))

total_count = 0
counts = []
for size in range(1, n + 1):
    count = 0
    for i in range(n):
        for j in range(n):
            if check_space(space, size, i, j):
                count += 1
    counts.append(count)
    total_count += count

print(f"total: {total_count}")
for i, count in enumerate(counts):
    if count > 0:
        print(f"size[{i+1}]: {count}")
