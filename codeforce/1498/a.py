import math
import sys


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def gcdsum(n):
    s = 0
    for d in str(n):
        s += int(d)
    return math.gcd(n, s)


lines = sys.stdin.readlines()

t = read_a_num(lines[0])

for line in lines[1 : t + 1]:
    n = read_a_num(line)

    while True:
        res = gcdsum(n)
        if res > 1:
            print(n)
            break
        n += 1
