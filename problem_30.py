# -*- coding: utf-8; -*-
#
# 2019-06-01


def process():
    result = list()
    c_number = 1
    while True:
        c_number += 1
        str_number = format(c_number)
        sum_number = sum(int(i)**5 for i in str_number)
        # if sum_number > c_number:
        #     print("SUP", c_number, sum_number)
        # else:
        #     print("INF", c_number, sum_number)
        if c_number == sum_number:
            result.append(c_number)
        if len(str(c_number)) > 6:
            break

    return result


def main():
    return process()


if __name__ == '__main__':
    print(main())
