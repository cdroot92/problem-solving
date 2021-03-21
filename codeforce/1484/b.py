import sys


def read_a_num(line):
    [n] = list(map(int, line.strip().split(" ")))
    return n


def read_nums(line):
    return list(map(int, line.strip().split(" ")))


def get_c(diff_set):
    for d in diff_set:
        if d > 0:
            return d


lines = sys.stdin.readlines()

t = read_a_num(lines[0])

for i in range(1, 2 * t + 1, 2):
    n = read_a_num(lines[i])
    array = read_nums(lines[i + 1])
    if n <= 2:
        print(0)
        continue
    diff = []
    diff_set = set()
    for ai in range(n - 1):
        diff.append(array[ai + 1] - array[ai])
        diff_set.add(array[ai + 1] - array[ai])

    if n == 3:
        if diff[0] == 0 and diff[1] == 0:
            print(0)
            continue
        if diff[0] * diff[1] >= 0:
            print(-1)
            continue
        m = abs(diff[0]) + abs(diff[1])
        c = max(diff[0], diff[1])

        def check_array():
            for a in array:
                if m <= a:
                    print(-1)
                    return True
            return False

        if check_array():
            continue
        print(f"{m}, {c}")

    diff_diff = []
    diff_diff_set = set([])
    for di in range(n - 2):
        diff_diff.append(diff[di + 1] - diff[di])
        diff_diff_set.add(abs(diff[di + 1] - diff[di]))

    if (0 in diff_diff_set and len(diff_diff_set) > 2) or (
        0 not in diff_diff_set and len(diff_diff_set) > 1
    ):
        print(-1)
        continue

    def check_diffdiff():
        before = None
        m = None
        for dd in diff_diff:
            if before is None:
                before = dd
                if dd != 0:
                    m = abs(dd)
                continue
            if before != 0:
                if dd != 0 and dd * before > 0:
                    print(-1)
                    return True, m
                m = abs(dd)
                before = dd
            else:
                before = dd
        return False, m

    isTrue, m = check_diffdiff()
    if isTrue:
        continue
    c = get_c(diff_set)

    print(f"{m} {c}")
