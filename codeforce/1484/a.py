import sys


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def read_two_num(line):
    [n1, n2] = list(map(int, line.strip().split(" ")))
    return n1, n2


lines = sys.stdin.readlines()

t = read_a_num(lines[0])

for line in lines[1 : t + 1]:
    a, b = read_two_num(line)
    print(a * b)
