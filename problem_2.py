import time

dict_result = {}


def fibo(n):
    if n in dict_result:
        return dict_result[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibo(n-1) + fibo(n - 2)
    if n not in dict_result:
        dict_result[n] = result
    return result


def get_million_even_term(N):
    ts = time.time()
    i = 0
    while True:
        r = fibo(i)
        if r > N:
            print("took ", time.time() - ts)
            return
        if r % 2 == 0:
            yield r
        i += 1


if __name__ == '__main__':
    print(sum(get_million_even_term(4_000_000)))

# 266333
