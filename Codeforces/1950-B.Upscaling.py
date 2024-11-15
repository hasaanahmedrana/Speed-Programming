for _ in range(int(input())):
    has = '##';
    dot = '..'
    n = int(input())
    first = [dot if i % 2 else has for i in range(n)]
    sec = [dot if not i % 2 else has for i in range(n)]
    for i in range(n):
        if not i % 2:
            print(''.join(first))
            print(''.join(first))
        else:
            print(''.join(sec))
            print(''.join(sec))
