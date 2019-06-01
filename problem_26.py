# -*- coding: utf-8; -*-
#
# 2019-05-28


def get_chunks(str_float):
    parts = str_float.split(".")[-1]
    for i in range(1, int(len(parts)/2)):
        yield parts[:i], parts[i:i*2]


def get_max_cycle_len(cycle_chunck):
    candidate = None
    for couple in cycle_chunck:
        if candidate is None and couple[1] == couple[0]:
            candidate = couple
        if couple[1] == couple[0] and len(couple[0]) > len(candidate[0]) and len(set(couple[0])) > 1:
            candidate = couple
    return candidate


def get_cycle(float_dec):
    chuncks_iter = get_chunks(format(float_dec, '.64'))
    return get_max_cycle_len(chuncks_iter)


def main(limit, list_numner=None):
    max_len = 0
    for i in list_numner or range(1, limit):
        cycle = get_cycle(1/i)
        if not cycle:
            continue

        if len(cycle[0]) >= 8:
            print(i)
            print(format(1/i, '.64'))
            print(cycle)
            print(len(cycle[0]))
            print()
        if len(cycle[0]) > max_len:
            max_len = len(cycle[0])
    return max_len


def main2():
    # from https://www.lucaswillems.com/fr/articles/52/project-euler-26-solution-python
    def cycle_length(den):
        reste = 10
        i = 0
        # Calcul des décimales tant que le reste n'est pas égal à 10
        while reste != 10 or i < 1:
            reste = (reste % den) * 10
            i += 1
        return i

    longest = 0
    for i in range(2, 1000):
        if i % 2 != 0 and i % 5 != 0:
            length = cycle_length(i)
            if length > longest:
                longest = length
                resultat = i
    print(resultat)


if __name__ == '__main__':
    print(main(1000))
