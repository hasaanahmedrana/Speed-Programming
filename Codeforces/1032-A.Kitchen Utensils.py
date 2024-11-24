n,m = map(int,input().split())
lst = list(map(int, input().split()))
x = list(set(lst))
dishes = [[i,lst.count(i)] for i in x]
sorted_dishes = sorted(dishes, key=lambda x:x[1])
maxi = sorted_dishes[-1][1]
if maxi % m == 0:
    num = maxi
else:
    num = maxi + (m - (maxi % m))
summ = 0
for i in sorted_dishes:
    summ += (num - i[1])
print(summ)

