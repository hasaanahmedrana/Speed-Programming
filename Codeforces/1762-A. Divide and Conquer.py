def parity_change(i):
    c = 0
    if i % 2:
        while i % 2:
            i = i // 2
            c += 1
    else:
        while i % 2 == 0:
            i = i // 2
            c += 1
    return c


def main():
    l = int(input())
    x = list(map(int, input().split()));
    x.sort()
    if not sum(x) % 2: return 0
    for i in range(l):
        x[i] = parity_change(x[i])
    return min(x)


for _ in range(int(input())):
    print(main())