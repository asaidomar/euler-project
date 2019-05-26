# -*- coding: utf-8; -*-

dict_result = dict()


def facto(n):
    if n in dict_result:
        return dict_result[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    dict_result[n] = n * facto(n-1)
    return dict_result[n]


def main(n):
    result = facto(n)
    return sum(int(i) for i in str(result))

if __name__ == '__main__':
    print(main(100))
