n = int(input())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
for i in range(1,n+1):
    x = coins[:i]
    y = coins[i:]
    if sum(x) > sum(y):
        print(i)
        break
