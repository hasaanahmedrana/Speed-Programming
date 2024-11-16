n, m = map(int, input().split())
dict = {}
lst = []
for i in range(m):
    a, b = input().split()
    if len(a) <= len(b):
        lst.append(a)
        dict[b] = a
    if len(a) > len(b):
        lst.append(b)
        dict[a] = b

x = list(input().split())
for each in x:
    if each in lst:
        print(each, end=' ')
    else:
        print(dict[each], end=' ')
