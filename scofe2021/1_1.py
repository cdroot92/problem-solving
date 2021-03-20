import sys
from datetime import time


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def read_from_to(line):
    times = line.strip().split(" ~ ")
    from_time = list(map(int, times[0].split(":")))
    to_time = list(map(int, times[1].split(":")))
    return time(from_time[0], from_time[1]), time(to_time[0], to_time[1])


lines = sys.stdin.readlines()

res_from = time(0, 0)
res_to = time(23, 59)
n = read_a_num(lines[0])
for line in lines[1 : n + 1]:
    ft, tt = read_from_to(line)
    if res_from >= tt or res_to <= ft:
        print(-1)
        sys.exit()
    if res_from <= ft and res_to >= tt:
        res_from = ft
        res_to = tt
    elif res_from >= ft and res_to >= tt:
        res_to = tt
    elif res_from <= ft and res_to <= tt:
        res_from = ft

print(f"{res_from.strftime('%H:%M')} ~ {res_to.strftime('%H:%M')}")
