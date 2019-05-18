data="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def populate_tab():
    result = list()
    for l in data.splitlines():
        result.append([int(i) for i in l.split()])
    return result


def recurcive_route(tab, i, j, result=None):
    if result is None:
        result = list()
    try:
        _ , _= tab[i+1], tab[j+1]
    except IndexError:
        return result
    result.append(tab[i][j])
    recurcive_route(tab, i+1, j, result)

    recurcive_route(tab, i+1, j+1, result)


def route(tab):
    result = list()
    prev_i = -1
    for i in range(0, len(tab)):
        if len(tab[i]) == 1:
            candidate = tab[i][prev_i]
            prev_i = 0
        else:
            candidate = max(tab[i][prev_i:prev_i+2])
            prev_i = tab[i].index(candidate)

        result.append(int(candidate))
    return result


def route2():
    tab = populate_tab()
    tab.reverse()
    for i in range(1, len(tab)):
        sub_tab = tab[i]
        for j in range(len(sub_tab)):
            tab[i][j] += max((tab[i-1][j], tab[i-1][j+1]))
    return tab[-1][-1]


def main():
    tab = populate_tab()
    result = route(tab)
    return result

if __name__ == '__main__':
    print(route2())




#75, 95, 47, 87, 82, 75, 73, 28, 83, 47, 43, 73, 91, 67, 98
