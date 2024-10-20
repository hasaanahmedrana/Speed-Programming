def elevator():
    n = int(input(''))
    for i in range(n):
        a, b, c = map(int, input('').split())
        if a == 1:
            print('1')
        elif b > c:
            if b - 1 > (a - 1):
                print('1')
            elif b - 1 < (a - 1):
                print('2')
            elif b - 1 == a - 1:
                print('3')
        elif b < c:
            x = ((c - b) * 2) + (b - 1)
            if x > (a - 1):
                print('1')
            elif x < (a - 1):
                print('2')
            elif x == a - 1:
                print('3')
        else:
            print('3')
elevator()
