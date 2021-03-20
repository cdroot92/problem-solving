import sys
from datetime import time


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def read_str(line):
    return line.strip()


lines = sys.stdin.readlines()

n = read_a_num(lines[0])
route = read_str(lines[1])

stack = [0]
count = 0
while stack:
    i = stack.pop()
    if i >= n or route[i] == "0":
        continue
    if i == n - 1:
        count += 1
    stack.append(i + 1)
    stack.append(i + 2)

print(count)
