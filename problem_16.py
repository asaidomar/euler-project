import math


def main(n):
    tab_result = []
    result_dec = 2 ** n

    return sum(int(i) for i in str(result_dec))

if __name__ == '__main__':
    print(main(1000))