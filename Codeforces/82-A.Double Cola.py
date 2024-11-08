def find(n):
    i = 0
    d = {'Sheldon': 1,
         'Leonard': 1,
         'Penny': 1,
         'Rajesh': 1,
         'Howard': 1}
    lst = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

    while n > 0:
        if i == 5:
            i = 0
        x = lst[i]
        val = d.get(x)
        if n <= val: break
        n -= val
        i += 1
        d[x] *= 2

    return lst[i]


n = int(input())
idx = find(n)
print(idx)