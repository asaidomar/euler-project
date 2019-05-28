# -*- coding: utf-8; -*-
#
# 2019-05-28
import string


def get_dict_order():
    return {l: i for i, l in enumerate(string.ascii_uppercase, start=1)}


def process_name(file):
    result = list()
    with open(file, newline="") as fin:
        for line in fin:
            names = line.split(",")
            result.extend(n.strip('"') for n in names)
    return result


def process_order(ordered_list):
    result = 0
    dict_order = get_dict_order()

    for i, name in enumerate(ordered_list, start=1):
        result += sum(dict_order[l] for l in name) * i
    return result


def main():
    file = "/Users/alisaidomar/PycharmProjects/euler-project/p022_names.txt"
    unordered = process_name(file)
    return process_order(sorted(unordered))


if __name__ == '__main__':
    print(main())
