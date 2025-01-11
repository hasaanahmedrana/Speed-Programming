n ,k = map(int, input().split())
x = (n + 1)//2
if k <= x:
    print(2 * k - 1)
else:
    print((k - x) * 2)
