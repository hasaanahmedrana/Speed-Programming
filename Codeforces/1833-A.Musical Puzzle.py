for _ in range(int(input())):
    n = int(input())
    x = input()
    y = []
    for i in range(n - 1):
        y.append(x[i] + x[i + 1])
    print(len(set(y)))

