n = int(input())
s = input()
a = s[:n]; b = s[n:]
a = [int(i) for i in a]
b = [int(i) for i in b]
a.sort(); b.sort()
less = False
high = False
for i in range(n):
    if a[i] < b[i]:
        less = True
        if high:
            print('NO')
            exit()
    elif a[i] > b[i]:
        high = True
        if less:
            print('NO')
            exit()
    else:
        print('NO')
        exit()
print('YES')
