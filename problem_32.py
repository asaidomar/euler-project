# -*- coding: utf-8; -*-
#
# alisaidomar <saidomarali@mail.com>
# 2019-06-04


def get_a_candidate(limit):
    a = 0
    while a <= limit:
        a += 1
        str_a = format(a)
        if len(set(str_a)) == len(str_a) and not str_a.endswith("0"):
            yield a


def process(limit):
    result = set()
    candidates = get_a_candidate(limit**0.5)
    for a in candidates:
        for b in range(int(limit**0.5), a, -1):
            c = a * b
            str_op = format(a) + format(b) + format(c)
            if len(str_op) == len(format(limit)) and set(str_op) == set(format(limit)):
                result.add(c)
    return result


def main(limit):
    return process(limit)


if __name__ == '__main__':
    print(main(123456789))

