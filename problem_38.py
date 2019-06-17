# -*- coding: utf-8; -*-
#
# 2019-06-17


def get_pandigital(number, limit):
    result = "".join(map(str, (number * i for i in range(1, limit+1))))
    return result


def process(limit):
    max_p = 0
    for i in range(1, 98765):
        end = 2
        while True:
            pan_d = get_pandigital(i, end)
            if len(pan_d) > limit:
                break
            if set(pan_d) == set('123456789'):
                if int(pan_d) > max_p:
                    max_p = int(pan_d)
                    print(max_p)
            end += 1
    return max_p


def main():
    return process(9)


if __name__ == '__main__':
    print(main())
