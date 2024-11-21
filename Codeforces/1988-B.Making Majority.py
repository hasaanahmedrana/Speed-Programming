for _ in range(int(input())):
    n = int(input())
    lst = input()
    zeros = 0; ones = 0
    if lst[0] == '0': zeros = 1
    for i in range(n):
        if lst[i] == '1': ones += 1
        elif lst[i-1] == '1' and i > 0:
            zeros += 1
    print('YES') if ones > zeros else print('NO')


