def perfect_permutation():
    n = int(input())
    if n == 1:
        print('-1')
        return
    if n > 1 and n % 2 == 0:
        i = 1;c = 1;
        while c <= n // 2:
            print(i + 1,end=' ')
            print(i,end=' ')
            i += 2
            c = c+1
    else:
        print('-1')
perfect_permutation()