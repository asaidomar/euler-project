# -*- coding: utf-8; -*-
#
# 2019-06-12

cache = dict()


def facto(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    else:
        cache[n] = n * facto(n-1)
        return cache[n]


def factos(*args):
    return [facto(int(arg)) for arg in args]


def process(limit):
    result = list()
    for i in range(3, limit):
        str_i = format(i)
        if i == sum(factos(*str_i)):
            result.append(i)

    return result


def main(limit):
    return sum(process(limit))


if __name__ == '__main__':
    #print(facto(9))
    print(main(9_999_999))