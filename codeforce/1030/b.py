# https://codeforces.com/problemset/problem/1030/B

import sys

lines = sys.stdin.readlines()


def read_two_nums(line):
    [n1, n2] = list(map(int, line.strip().split(" ")))
    return n1, n2


def read_a_num(line):
    n = int(line.strip())
    return n


def check_position(x, y):
    if (y >= -x + d) and (y <= x + d) and (y <= -x + 2 * n - d) and (y >= x - d):
        return True
    else:
        return False


n, d = read_two_nums(lines[0])
nums = read_a_num(lines[1])
for line in lines[2:]:
    x, y = read_two_nums(line)
    if check_position(x, y):
        print("YES")
    else:
        print("NO")
