# -*- coding: utf-8; -*-
#
# 2019-06-01


def process(lines):
    result = 0
    for i in range(lines, 2, -2):
        top = i * i
        left = top - i + 1
        bottom = left - i + 1
        right = bottom - i + 1
        result += top + left + bottom + right
    return result + 1


def main(l):
    return process(1001)


if __name__ == '__main__':
    print(main(5))
