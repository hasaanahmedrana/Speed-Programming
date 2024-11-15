for _ in range(int(input())):
    lst = [*map(int, input().split())]
    p = 'NONE'
    if lst[0] < lst[1] < lst[2]:
        p = 'STAIR'
    if lst[0] < lst[1] > lst[2]:
        p = 'PEAK'
    print(p)
