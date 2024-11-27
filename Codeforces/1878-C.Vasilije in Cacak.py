def main():
    n, k, x = map(int, input().split())
    z = (n * k) - ((k - 1) * k) // 2
    z_ = k + (k * (k - 1) // 2)
    if z >= x >= z_:
        return 'YES'
    return 'NO'


for _ in range(int(input())):
    print(main())
