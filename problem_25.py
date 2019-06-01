# -*- coding: utf-8; -*-
#
# 2019-05-28
from itertools import permutations


def get_permutation(n):
    return permutations(range(n))


def get_permutations_list(iter_list):
    if not iter_list:
        return []
    if len(iter_list) == 1:
        return [iter_list]

    result = []
    for i in range(len(iter_list)):
        el = iter_list[i]
        rm_els = iter_list[:i] + iter_list[i+1:]

        for p in get_permutations_list(rm_els):
            result.append([el] + p)
    return result


def main(n):
    result = get_permutation(n)
    c = 0
    while True:
        p = next(result)
        c += 1
        if c == 1_000_000:
            print("".join(map(str, p)))


if __name__ == '__main__':
    print(main(10))
