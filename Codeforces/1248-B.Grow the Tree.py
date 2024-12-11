def main():
    l = int(input())
    x = list(map(int, input().split()))
    x.sort()
    n1 = sum(x[:l // 2])
    n2 = sum(x[l // 2:])
    print(n1 ** 2 + n2 ** 2)


main()