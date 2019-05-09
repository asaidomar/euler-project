def is_palindrome(n):
    """

    >>> is_palindrome(9009)
    True

    :param n:
    :return:
    """
    str_n = str(n)
    reversed_n = "".join(reversed(str_n))

    return str_n == reversed_n


def get_max_digit_palindrom(n):
    max_n = 10 ** n - 1

    for i in range(max_n, 1, -1):
        if i <= 10 ** (n - 1) - 1:
            break
        for j in range(max_n, 1, -1):
            if j <= 10 ** (n - 1) - 1:
                break
            value = i * j
            if is_palindrome(value):
                yield value


if __name__ == '__main__':
    print(max(list(get_max_digit_palindrom(3))))
