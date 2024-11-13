n = int(input())
lst = list(map(int, input().split()))
dic = {}
for i in lst:
    dic[i] = dic.get(i, 1)
count = 0
for j in range(1, n + 1):
    y = dic.get(j, 0)
    if y == 0:
        count += 1
print(count)
