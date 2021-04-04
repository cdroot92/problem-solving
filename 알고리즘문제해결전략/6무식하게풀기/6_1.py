# 재귀와 반복문으로 1 ~ n 까지의 합


def recursive_sum(n):
    if n == 1:
        return n
    return n + recursive_sum(n - 1)


def for_sum(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
    return ret


for n in range(1, 11):
    print(f"{recursive_sum(n)}, {for_sum(n)}")
