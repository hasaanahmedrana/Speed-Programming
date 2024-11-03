n, d = map(int, input().split())
ans = []
count = 0
for i in range(d):
    inp = [int(j) for j in (input())]
    if sum(inp) == n:
        ans.append(count)
        count = 0
    else:
        count += 1
ans.append(count)
print(max(ans))
