for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst.sort()
    if len(set(lst)) == 1:
        pass
    elif len(set(lst)) == 2:
        lst.sort()
        if lst[0] == lst[1]:
            if abs(lst[1] - lst[2]) > 1:
                lst[1] += 1
                lst[0] += 1
            lst[2] -= 1
        else:
            if abs(lst[0] - lst[2]) > 1:
                lst[1] -= 1
                lst[2] -= 1
            lst[0] += 1
    else:
        if lst[0] < lst[1]:
            lst[0] += 1
        if lst[2] > lst[1]:
            lst[2] -= 1
    print(sum([abs(lst[0] - lst[1]), abs(lst[0] - lst[2]), abs(lst[2] - lst[1])]))

