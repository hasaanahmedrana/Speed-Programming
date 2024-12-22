def main():
    s = int(input())
    x = list(map(int, input().split()))
    y = sorted(x)
    for i in range(s):
        if x[i] % 2 != y[i] % 2:
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    print(main())
