import re


def get_word(number):
    dict_number = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
     8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
     100: 'one hundred', 1000: 'one thousand'}

    return dict_number[number]



def decompose(number):
    result = list()
    while number > 0:
        result.append(number % 10)
        number = int(number / 10)
    return result


def _trans_dec(number):
    decomposed = decompose(number)
    if decomposed[0] > 0:
        return f"{get_word(decomposed[1])}-{get_word(decomposed[0])}"
    if decomposed[0] == 0:
        return get_word(number)


def _trans_dent(number):
    decomposed = decompose(number)

    number_dec = decomposed[0] + 10 * decomposed[1]
    if number_dec > 0:
        result = f"{trans_number_to_word(decomposed[-1])} hundred and {trans_number_to_word(number_dec)}"
    else:
        result = f"{trans_number_to_word(decomposed[-1])} hundred"

    return result


def trans_number_to_word(number):
    if number <= 20:
        return get_word(number)

    elif number < 100:
        decomposed = decompose(number)
        if decomposed[0] > 0:
            return f"{get_word(decomposed[1]*10)}-{get_word(decomposed[0])}"
        if decomposed[0] == 0:
            return get_word(number)

    elif number == 100:
        return get_word(number)

    elif number < 1000:
        return _trans_dent(number)

    elif number == 1000:
        return get_word(number)


def slug(s):
    return re.sub("[\s+\-]", "", s)


def main(end):
    result = []
    for i in range(1, end + 1):
        result.append(trans_number_to_word(int(i)))
        print(i, result[-1])
        print()
    #return sum([len(slug(i)) for i in result])
    return sum([len(slug(i)) for i in result])
    #return result


if __name__ == '__main__':
    print(main(1000))
