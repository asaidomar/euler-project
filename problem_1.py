def _get_multiple(end, number):
    current = 1
    while True:
        multiple = current * number
        if multiple <= end:
            yield multiple
        else:
            return
        current += 1


def get_sum_multiple(end, *numbers):
    result = set()
    for number in numbers:
        result |= set(_get_multiple(end, number))
    return result


if __name__ == '__main__':
    print(sum((get_sum_multiple(999, 3, 5))))

# 266333
