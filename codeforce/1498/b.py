import math
import sys


def read_a_num(line):
    n = int(line.strip())
    return n


def read_nums(line):
    return tuple(map(int, line.strip().split(" ")))


def calc_height(n, W, ws):
    box = [0 for i in range(len(format(W, "b")))]
    for w in ws:
        b = int(math.log2(w))
        box[b] += 1
    print(max(box))


lines = sys.stdin.readlines()


t = read_a_num(lines[0])

for i in range(1, 2 * t + 1, 2):
    n, W = read_nums(lines[i])
    ws = read_nums(lines[i + 1])
    calc_height(n, W, ws)
