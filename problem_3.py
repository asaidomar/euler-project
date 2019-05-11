def decompose(n):
    result = list()
    i = 2
    while n > 1:
        while n % i == 0:
            result.append(i)
            n = n / i
        i += 1
    return result


def main(n):
    return decompose(n)


if __name__ == '__main__':
    max_ = main(9438)
    print(max_)
