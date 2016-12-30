import random

def partition(a, p, r, rand = False):
    if rand:
        randIdx = random.choice(range(p,r))
        a[randIdx], a[r] = a[r], a[randIdx]
    x = a[r]
    i = p - 1
    for j in range(p,r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def qsort(a, p, r, rand = False):
    if p<r:
        q = partition(a,p,r, rand = rand)
        print(a)
        qsort(a,p,q-1, rand = rand)
        qsort(a,q,r, rand = rand)

if __name__ == '__main__':
    a = [random.randrange(0,10) for _ in range(10)]
    b = a[:]
    print('init: ', a)
    qsort(a,0,len(a)-1)
    print('sorted: ', a)

    print('init: ', b)
    qsort(b,0,len(a)-1)
    print('sorted: ', b)
