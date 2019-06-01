# -*- coding: utf-8; -*-
#
# 2019-06-01
from itertools import product


def process(limit_a, limit_b):
    return {a ** b for a, b in
            product(range(2, limit_a + 1), range(2, limit_b + 1))}


def main(limit_a, limit_b):
    return len(process(limit_a, limit_b))


if __name__ == '__main__':
    print(main(100, 100))
