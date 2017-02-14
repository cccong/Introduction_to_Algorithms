import random


class Tree:
    _index = 0
    tree = {'root': None}

    def insert(self, z):
        print(self.tree)
        node = {'parent': None, 'left': None, 'right': None, 'key': z}

        x = 'root'
        y = None
        while self.tree[x] is not None:
            y = x
            if z < self.tree[x]['key']:
                x = self.tree[x]['left']
                if x is None:
                    self.tree[y]['left'] = self._index
                    break
            else:
                x = self.tree[x]['right']
                if x is None:
                    self.tree[y]['right'] = self._index
                    break
        else:
            self.tree['root'] = node
            return

        self.tree[self._index] = node
        node['parent'] = y
        self._index += 1

    def __init__(self, lis):
        for i in lis:
            self.insert(i)

    def in_order_walk(self):
        tree = self.tree

        def walk(node):
            if node is not None:
                walk(tree[node]['left'])
                print(tree[node]['key'])
                walk(tree[node]['right'])

        if tree['root']:
            walk('root')

    def minimum(self):
        node = 'root'
        minim = None
        while node is not None:
            minim = self.tree[node]
            node = self.tree[node]['left']
        return minim

    def maximum(self):
        node = 'root'
        maxim = None
        while node is not None:
            maxim = self.tree[node]
            node = self.tree[node]['right']
        return maxim

    def search(self, x):
        print('x: ----->', x)
        tree = self.tree
        node = 'root'
        result = []
        while node is not None:
            print('node:------> ', node)
            if tree[node]['key'] == x:
                result.append(tree[node])
                node = tree[node]['right']
            elif tree[node]['key'] > x:
                node = tree[node]['left']
            else:
                node = tree[node]['right']
        return result

    def successor(self, x):
        if self.tree[x]['right'] is not None:
            return self.minimum()


l = [random.randrange(1, 10) for _ in range(5)]
print(l)
t = Tree(l)
print(t.tree)
t.in_order_walk()

print(t.search(l[3]))

print('min: ---->', t.minimum())
print('max: ---->', t.maximum())

print(t.search(l[3]))
