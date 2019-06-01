# -*- coding: utf-8; -*-
#
# 2019-05-31


def primes_formula(a, b, n):
    return n ** 2 + a * n + b


def get_primes(limit):
    candidates = set(range(2, limit))
    for i in range(2, limit):
        candidates.difference_update({i * n for n in range(i, limit)})
    return candidates


def primes_below(end):
    if end < 2:
        return []
    lng = (end // 2) - 1
    primes = [True] * lng
    for i in range(int(lng ** 0.5)):
        if primes[i]:
            for j in range(2 * i * (i + 3) + 3, lng, 2 * i + 3):
                primes[j] = False
    return [2] + [i * 2 + 3 for i, j in enumerate(primes) if j]


def is_prime(n):
    for i in range(2, (abs(n) // 2) + 1):
        if n % i == 0:
            return False
    return True


def process():
    candidate_a = 0
    candidate_b = 0
    max_len = 0
    primes = list(get_primes(1000))
    result = dict()
    max_computed = list()

    for a in range(-999, 1000, 2):
        for b in primes:
            # a + b must be even
            if (a + b) % 2 == 1:
                continue
            computed_primes = list()
            n = 0
            while True:
                candidate_prime = primes_formula(a, b, n)
                if not is_prime(candidate_prime):
                    result[(a, b)] = computed_primes
                    if len(computed_primes) > max_len:
                        max_len = len(computed_primes)
                        candidate_a, candidate_b = a, b
                        max_computed = computed_primes
                    break
                else:
                    computed_primes.append(candidate_prime)
                n += 1
    return candidate_a, candidate_b, max_computed


def main():
    a, b, mac_c = process()
    return a, b, mac_c


def main2():
    # from https://www.lucaswillems.com/fr/articles/53/project-euler-27-solution-python
    def primes_below(end):
        if end < 2:
            return []
        lng = (end // 2) - 1
        primes = [True] * lng
        for i in range(int(lng ** 0.5)):
            if primes[i]:
                for j in range(2 * i * (i + 3) + 3, lng, 2 * i + 3):
                    primes[j] = False
        return [2] + [i * 2 + 3 for i, j in enumerate(primes) if j]

    # Obtention de la liste des nombres premiers inférieurs à 1000
    primes = primes_below(1000)
    longest = 0
    # b prend successivement la valeur des différents nombres premiers
    for b in primes:
        # a prend successivement la valeur de tous les nombres impairs de -999 à 2
        for a in range(-999, 1000, 2):
            image = b
            n = 0
            # Calcul du nombre consécutif de nombres premiers
            while is_prime(image):
                n += 1
                image = n ** 2 + a * n + b
            if n > longest:
                longest = n
                resultat = a * b
    return resultat


if __name__ == '__main__':
    print(main())

    # print(list(primes_formula(1, 41, i) for i in range(0, 40)))
