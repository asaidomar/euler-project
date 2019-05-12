
dict_result = dict()


def count_routes(m, n):
    if (m, n) in dict_result:
        return dict_result[(m, n)]
    if m == 0 or n == 0:
        return 1
    else:
        dict_result[(m, n)] = count_routes(m-1, n) + count_routes(m, n -1)
        return dict_result[(m, n)]


if __name__ == '__main__':
    print(count_routes(20, 20))
