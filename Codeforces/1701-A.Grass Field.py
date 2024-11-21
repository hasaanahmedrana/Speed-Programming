for _ in range(int(input())):
    x = list(map(int, input().split()))
    x += list(map(int, input().split()))
    if sum(x) == 0:print(0)
    elif sum(x) == 4:print(2)
    else: print(1)


