import math
from functools import reduce


def pgcd(a, b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b != 0:
        a, b = b, a % b
    return a


def pgcdn(*n):
    """Calcul du 'Plus Grand Commun Diviseur' de n valeurs entières (Euclide)"""
    p = pgcd(n[0], n[1])
    for x in n[2:]:
        p = pgcd(p, x)
    return p


def divisible(n, *args):
    """
    >>> divisible(2520, *list(range(10, 1)))
    True

    :param n:
    :param args:
    :return:
    """
    result = all(n % i == 0 for i in args)
    return result


def get_min_all_divisible():
    numbers = [i for i in range(1, 21) if i % 2 == 0]

    max_m = reduce(lambda x, y: x * y, numbers)
    pgcdn_ = pgcdn(*numbers)

    return max_m/pgcdn_


if __name__ == '__main__':
    print(get_min_all_divisible())
