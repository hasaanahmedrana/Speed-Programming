def main():
    l = int(input())
    y = list(map(int, input().split()))
    n = min([y[i] + y[i + 1] for i in range(l - 1)])
    return sum(y) - (2 * n)


for _ in range(int(input())):
    print(main())