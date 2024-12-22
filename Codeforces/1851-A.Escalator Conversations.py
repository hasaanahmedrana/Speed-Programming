def main():
    n, m, k, h = map(int, input().split())
    x = list(map(int, input().split()))
    y = [i*k for i in range(1, m)]
    for i in range(n):
        if abs(x[i]-h) in y:
            x[i] = 'x'
    return x.count('x')


for _ in range(int(input())):
    print(main())