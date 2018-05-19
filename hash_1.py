from collections import namedtuple
import random
import string


class HashTable:
    class _ele:
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next
        
        def __repr__(self):
            return f'[{self.key}, {self.value}, {self.next}]'

    def __init__(self, m = 10, p = 100):
        self.m = m
        self.p = p

        self.random = random.Random()
        self.a = random.randint(0,p)
        self.b = random.randint(0,p-1)

        self._table = [self._ele() for _ in range(m)]

    def hash(self, key):
        v = ((self.a * key + self.b) % self.p) % self.m
        return v

    def set(self, key, value):
        hash_value = self.hash(key)

        def set_ele(node, key, value):
            if node.key is None:
                node.key = key
                node.value = value
                node.next = self._ele()
            else:
                set_ele(node.next, key, value)

        set_ele(self._table[hash_value], key, value)

    def get(self, key):
        def search(node, key):
            if node.key == key:
                return node.value
            else:
                return search(node.next, key)
        
        hash_value = self.hash(key)
        return search(self._table[hash_value], key)

    def __repr__(self):
        return str(self._table)

    
t = HashTable()
for k,v in enumerate(string.ascii_letters, 1):
    t.set(k,v)
    print(t)

for k in range(1,27):
    print(t.get(k))
