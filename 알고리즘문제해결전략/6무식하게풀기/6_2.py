# 0 ~ n-1의 값을 갖는 n개의 원소 중 m개 고르는 경우의 수

count = 0


def pick(n, m, picked):
    if m == 0:
        global count
        count += 1
        return
    smallest = 0 if len(picked) == 0 else picked[-1] + 1
    for i in range(smallest, n):
        picked.append(i)
        pick(n, m - 1, picked)
        picked.pop()


pick(4, 2, [])
print(count)
