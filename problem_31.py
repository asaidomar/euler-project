# -*- coding: utf-8; -*-
#
# 2019-06-02

tree = [1, 2, 5, 10, 20, 50, 100]
count = 0


# credit https://medium.com/@jschapir/coinsum-algorithm-for-dummies-e3f73394bc11
def coinsum(total):
    count = 0

    def make_change(current_total):
        nonlocal count
        if current_total == total:
            count += 1
            # print(count)
            return
        if current_total > total:
            return

        for c in tree:
            make_change(current_total + c)

    make_change(0)
    return count


def _walk(index=0, sum_=0, path=None, ):
    global count
    path = path or []
    new_sum_ = sum_ + tree[index]
    path.append(index)
    if new_sum_ == 200:
        path = list()
        count += 1
    if new_sum_ > 200:
        return
    for j in range(index, len(tree)):
        _walk(index=j, sum_=new_sum_, path=path)
    return count


def main():
    return _walk()


def main2():
    return coinsum(200)


if __name__ == '__main__':
    print(main2())
