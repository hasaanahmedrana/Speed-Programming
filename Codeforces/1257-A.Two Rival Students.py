for _ in range(int(input())):
    n, x, a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    diff = a - b
    n -= diff + 1
    while x != 0 and n != 0:
        diff += 1
        n -= 1
        x -= 1
    print(diff)
