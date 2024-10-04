n = int(input())
s = input()
pairs = dict()
for j in range(n-1):
    x = s[j] + s[j+1]
    if not pairs.get(x):
        pairs[x] = 1
    else:
        pairs[x] += 1
print(max(pairs, key=pairs.get))
