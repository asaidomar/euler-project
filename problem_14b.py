import math


memoize_dict = {}


def step(start):
    if start % 2 == 0:
        start = int(start / 2)
    else:
        start = 3 * start + 1
    return start


def is_power_of_two(number):
    value = math.log(number, 2)
    return math.floor(value) == math.ceil(value)


def cycle_len(start):
    if start == 1:
        return 1
    if start in memoize_dict:
        return memoize_dict[start]

    if start % 2 == 0:
        memoize_dict[start] = 1 + cycle_len(start/2)
    else:
        memoize_dict[start] = 2 + cycle_len((3 * start + 1) / 2)

    return memoize_dict[start]


def main(end):
    j = 0
    max_l = 0
    for i in range(2, end):
        length = cycle_len(i)
        # print(i, length)
        if length > max_l:
            max_l = length
            j = i
    return max_l, j


if __name__ == '__main__':
    print(main(1_000_000))
