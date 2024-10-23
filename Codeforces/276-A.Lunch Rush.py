n, k = map(int, input().split())
joy = []
for i in range(n):
    f, t = map(int, input().split())
    ans = f - (t - k)
    if t > k:
        joy.append(ans)
    else:
        joy.append(f)
print(max(joy))
