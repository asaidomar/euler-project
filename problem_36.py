# -*- coding: utf-8; -*-
#
# 2019-06-13


def base2(number):
    result = list()
    while number != 0:
        number, rest = int(number / 2), number % 2
        result.append(rest)
    result.reverse()
    return result


def is_palindrome(list_number):
    return list(list_number) == list(reversed(list_number))


def process(limit):
    result = list()
    for number in range(limit):
        base2_repr = base2(number)
        if is_palindrome(format(number)) and is_palindrome(base2_repr):
            result.append(number)
    return result


def main(number):
    return sum(process(number))


if __name__ == '__main__':
    print(main(1_000_000))
