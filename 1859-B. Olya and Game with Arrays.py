def main():
    mini = []
    maxi = []
    n = int(input())
    for _ in range(n):
        t = int(input())
        x = sorted(list(map(int, input().split())))
        mini.append(x[0])
        maxi.append(x[1])
    maxi.sort()
    mini.append(maxi[0])
    return min(mini) + sum(maxi[1:])
for _ in range(int(input())):
    print(main())

