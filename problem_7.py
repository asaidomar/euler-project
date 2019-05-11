def prime_numbers(limit=1000000):
    '''Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
    using Sieve of Eratosthenes.
    '''
    yield 2
    sub_limit = int(limit ** 0.5)
    flags = [False, False] + [True] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i] is False:
            #        if flags[i] is True:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i * 3, limit, i << 1):
                flags[j] = False


#                flags[j] = True


def get_primes2(N):
    primes = set([2] + list(range(3, N, 2)))
    for n in range(3, int(N ** 0.5) + 1, 2):
        primes.difference_update( set(range(n * n, n, 2 * n) ))

    return sorted(list(primes))

print(get_primes2(100))

if __name__ == '__main__':
    pass
    #print(list(prime_numbers())[10000])