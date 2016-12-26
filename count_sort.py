def count_sort(a, k):
    c = [0] * k
    for i in a:
        c[i] = c[i] + 1
    print(c)
    for j in range(1,len(c)):
        c[j] += c[j-1]

    print(c)
    o = [0] * len(a)
    for m in a:
        o[c[m]-1] = m
        c[m] -= 1
        print(o)
    return o

if __name__ == '__main__':
    import random
    k = 10
    a = [random.randrange(1,10) for _ in range(10)]
    print(a)
    o = count_sort(a,k)
    print(o)
    
    
