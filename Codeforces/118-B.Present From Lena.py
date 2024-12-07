n = int(input())
for k in range(n * 2 + 1):
    x = k if k <= n else n - (k - n)
    for _ in range(n - x):
        print(end='  ')
    for i in range(x + 1):
        print(i, end=' ') if (k != 0 and k != n * 2) else print(i, end='')
    for j in range(x - 1, -1, -1):
        print(j, end=' ') if j != 0 else print(j, end='')
    print()
