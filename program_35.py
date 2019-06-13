# -*- coding: utf-8; -*-
#
# 2019-06-13
from itertools import cycle


def is_prime(candidate):
    candidate = int(candidate)
    if candidate == 1:
        return False
    for i in range(2, int(candidate ** 0.5) + 1):
        if candidate % i == 0:
            return False
    return True


def _rotate(iter_):
    result = [None] * len(iter_)
    for i in range(len(iter_)):
        result[i] = iter_[(i + 1) % len(iter_)]
    return result


def rotate(iter_: list):
    rotated = iter_[:]
    yield rotated
    for i in range(1, len(iter_)):
        rotated = _rotate(rotated)
        yield "".join(rotated)


def process(limit):
    result = list()
    for number in range(2, limit):
        rotations = rotate(format(number))
        if all(map(is_prime, rotations)):
            result.append(number)
    return result


def main(limit):
    return len(process(limit))


if __name__ == '__main__':
    print(main(1_000_000))
