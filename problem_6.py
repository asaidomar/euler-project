def get_sum(*args):
    return sum(i**2 for i in args)


def get_sum_sqrt(*args):
    return sum(args) **2


def main(n):
    args = list(range(1, n))
    return get_sum_sqrt(*args) - get_sum(*args)


if __name__ == '__main__':
    print(main(101))
