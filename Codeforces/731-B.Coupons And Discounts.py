n = int(input())
lst = list(map(int, input().split()))
f = True
for i in range(n):
    if i == n - 1 and lst[i] % 2:
            f = False
    elif lst[i] % 2 and lst[i + 1] < 1:
        f = False
    elif lst[i] % 2:
        lst[i + 1] -= 1

print('YES') if f else print('NO')