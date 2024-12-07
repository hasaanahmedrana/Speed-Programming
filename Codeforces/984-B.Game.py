def main():
    n = int(input())
    x = sorted(list(map(int, input().split())))
    return x[n // 2] if n % 2 else x[(n // 2) - 1]
print(main())
