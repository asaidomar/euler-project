date="""
75
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


class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

    def __str__(self):
        return self.data


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
        self.last = self.root
        self.previous = None

    def add_left(self, left_node_value, parent_node=None, node=None):
        current_node = node or Node(left_node_value)
        self.previous = self.last
        if parent_node:
            parent_node.l_child = current_node
        else:
            self.last.l_child = current_node
        return self.last

    def add_right(self, r_child_value, parent_node=None, node=None):
        current_node = node or Node(r_child_value)
        if parent_node:
            parent_node.r_child = r_child_value
        else:
            self.last.r_child = current_node
        return self.last


def make_tree():
    t = Tree(75)
    l = t.add_left(95, parent_node=t.root)
    r = t.add_right(64, parent_node=t.root)

    n_l = t.add_left(17, parent_node=l)
    n_r = t.add_right(47, parent_node=l)

    n_l = t.add_left("", parent_node=r, node=n_r)
    n_r = t.add_right(82, parent_node=r)





    return t

if __name__ == '__main__':
    t = make_tree()
    print(t)




