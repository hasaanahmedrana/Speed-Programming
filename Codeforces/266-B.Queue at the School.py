def replace(n, l, t):
    for _ in range(t):
        i = 0
        while i < n - 1:
            if l[i] == "B" and l[i+1] == "G":
                l[i+1], l[i] = l[i], l[i+1]
                i += 1
            i += 1
    return l
n, t = map(int, input().split())
l = list(input())
ans = replace(n, l, t)
print(''.join(ans))
