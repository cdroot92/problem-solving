# https://codeforces.com/problemset/problem/1030/A

import sys

i = sys.stdin.readlines()
o = "EASY"
ii = i[1].strip().split(" ")
for s in ii:
    if s == "1":
        o = "HARD"

print(o)
