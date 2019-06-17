# -*- coding: utf-8; -*-
#
# 2019-06-14


def is_prime(candidate):
    candidate = int(candidate)
    if candidate == 1:
        return False
    for i in range(2, int(candidate ** 0.5) + 1):
        if candidate % i == 0:
            return False
    return True


def r_trunc(number):
    return format(number)[:-1]


def l_trunc(number):
    return format(number)[1:]


def is_truncatable_number(number):
    l_number = number
    while True:
        l_number = l_trunc(l_number)
        if len(l_number) == 0:
            break
        if not is_prime(l_number):
            return False

    r_number = number
    while True:
        r_number = r_trunc(r_number)
        if len(r_number) == 0:
            break
        if not is_prime(r_number):
            return False

    return True


def process(nb_truncatable_primes):
    result = list()
    number = 3
    while True:
        number += 2

        if len(format(number)) == 1:
            continue

        if not is_prime(number):
            continue

        if is_truncatable_number(number):
            result.append(number)

        if len(result) == nb_truncatable_primes:
            break
    return result


def main(limit):
    return sum(process(limit))


if __name__ == '__main__':
    print(main(11))
