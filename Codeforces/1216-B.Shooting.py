def main():
    l = int(input())
    s = list(map(int, input().split()))
    x = [[j, i] for i, j in enumerate(s)]
    x.sort(reverse=True)
    ans = 0
    idx = []
    for n, m in enumerate(x):
        ans += (m[0] * n + 1)
        idx.append(m[1] + 1)
    print(ans)
    print(*idx)


main()
