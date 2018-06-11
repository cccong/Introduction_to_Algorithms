class Node:
    def __init__(self, seq):
        super().__setattr__('_attrs', {k:None for k in seq})
    
    def __getattr__(self, k):
        return self._attrs[k]

    def __setattr__(self, k, v):
        self._attrs[k] = v

    def __repr__(self):
        return repr(self._attrs)


if __name__ == '__main__':
    n = Node(['a','b'])
    print('init',n)

    n.a = 1
    print('set',n)

    n.c = Node(['a','b'])
    print('set',n)

