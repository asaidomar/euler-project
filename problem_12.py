from collections import Counter
from functools import reduce


def decompose(n):
    result = list()
    i = 2
    while n > 1:
        while n % i == 0:
            result.append(i)
            n = n / i
        i += 1
    return result


def prod(*args):
    return reduce(lambda x,y: x*y, args)


def get_div_number(divs):

    """

    >>> get_div_number([2, 2, 3])
    6

    :param divs:
    :return:
    """
    if not divs:
        return 0
    conters = Counter(divs)
    return prod(*[v + 1 for k, v in conters.items()])


def main():
    i = 1
    while True:
        ret = sum_trian(i)
        num_div = get_div_number(decompose(ret))
        if num_div >= 500:
            return ret
        i += 1


def sum_trian(n):
    return int(n*(n+1)/2)


if __name__ == '__main__':
    print((main()))
