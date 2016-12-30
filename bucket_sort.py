import random
import functools

def insert(link, i):
    if len(link) == 0:
        link.append(i)
        return
    for j in range(len(link)):
        if i <= link[j]:
            link.insert(j,i)
            break
    else:
        print(link,j,i)
        link.insert(j+1,i)

a = [random.randrange(0, 100) for _ in range(10)]
print(a)
b = [[] for _ in range(10)]

for i in a:
    # print(i,i//10)
    link = b[i//10]
    # print(link)
    insert(link,i)
    print(b)


print(functools.reduce(lambda m,l: m+l, b))