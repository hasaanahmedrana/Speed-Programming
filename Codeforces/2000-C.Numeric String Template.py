for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    for _ in range(int(input())):
        seq = {}
        chars = [i for i in input()]
        flag = True
        if len(chars) != n:
            print('No')
            continue
        for i in range(n):
            if (lst[i] in seq and seq[lst[i]] != chars[i]) or (chars[i] in seq and seq[chars[i]] != lst[i]):
                flag = False
            else:
                seq[lst[i]] = chars[i]
                seq[chars[i]] = lst[i]
        print('Yes') if flag else print('No')
