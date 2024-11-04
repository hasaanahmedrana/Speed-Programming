for i in range (5):
     s = list(map(int, input().split()))
     if 1 in s:
         p = i
         break
for j in range(5):
     if p + j == 2 or p - j == 2:
         n1=j
         break
x = s.index(1)
for j in range(5):
    if x + j == 2 or x - j == 2:
        n2 = j
        break
print(n1 + n2)
