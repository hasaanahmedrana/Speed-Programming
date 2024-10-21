def rabbits():
    x, y, a, b = map(int, input().split())

    if (y - x) % (a + b) == 0:
        return (y - x) // (a + b)
    else:
        return -1
t = int(input())
for _ in range(t):
    print(rabbits())
