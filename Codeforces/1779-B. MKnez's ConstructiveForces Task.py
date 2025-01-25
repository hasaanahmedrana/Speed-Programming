def hunger():
    n = int(input())
    if n == 3 or n == 1:
        return 'NO'
    if n % 2 != 0:
        a = n // 2 - 1;
        b = a + 1
        print('YES')
        l = []
        for i in range(n):
            if i % 2 == 0:
                l.append(a)
            else:
                l.append(-b)
        return l
    else:
        print('YES')
        l = []
        for i in range(n):
            if i % 2 == 0:
                l.append(1)
            else:
                l.append(-1)
        return l

for _ in range(int(input())):
    x = hunger()
    if x == 'NO':
        print(x);
    else:
        print(*x);