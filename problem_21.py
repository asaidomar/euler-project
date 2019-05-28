# -*- coding: utf-8; -*-
#
# 2019-05-28


def get_multiples(n):
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            yield i


def get_d(n):
    return sum(get_multiples(n))


def main(N):
    result = list()
    for i in range(1, N+1):
        d = get_d(i)
        d1 = get_d(d)
        if N > d > i == d1:
            result.extend((i, d))
    return sum(result)


if __name__ == '__main__':
    print(main(10_000))


