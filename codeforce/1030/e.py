# https://codeforces.com/problemset/problem/1030/E

import math
import sys

lines = sys.stdin.readlines()


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def read_n_nums(line, n):
    return list(map(lambda a: bin(int(a)).count("1"), line.strip().split(" ")))


n = read_a_num(lines[0])
a = read_n_nums(lines[1], n)

output = 0

dp = {}
for l in range(n):
    for r in range(l + 1, n):
        k = f"{l}~{r}"
        if l == r - 1:
            if a[l] == a[r]:
                output += 1
            dp[k] = range(abs(a[l] - a[r]), a[l] + a[r] + 1, 2)
        else:
            last_k = f"{l}~{r-1}"
            if a[r] in dp[last_k]:
                output += 1
            dp[k] = range(abs(dp[last_k][0] - a[r]), dp[last_k][-1] + a[r] + 1, 2)

print(output)
