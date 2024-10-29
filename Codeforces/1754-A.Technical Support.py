def technical_support():
    num = int(input())
    for i in range(num):
        length = int(input(''))
        inp = input('')
        q = unanswered = 0
        for j in range(length):
            a = inp[j]
            if a == 'Q' or a == 'q':
                q += 1
            else:
                q -= 1
            if q < 0:
                q = 0
        unanswered += q
        if unanswered == 0:
            print('YES')
        else:
            print('NO')

technical_support()

