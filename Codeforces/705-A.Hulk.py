def hulk():
    n = int(input(''))
    i = 1
    while i <= n:
        if i % 2 != 0:
            print('I hate', end=' ')
        else:
            print('I love', end=' ')
        if i < n:
            print('that', end=' ')
        if i == n:
            print('it')
        i += 1
hulk()