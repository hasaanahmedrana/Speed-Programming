def epicgame():
    a, b, n = map(int, input().split())
    while n > 0:
        i = 1
        subtraction = 0
        while i <= n:
            if a % i == 0 and n % i == 0:
                subtraction = i
            i += 1

        n -= subtraction
        if n == 0:
            print('0')
            return
        k = 1
        subtraction = 0
        while k <= n:
            if b % k == 0 and n % k == 0:
                subtraction = k
            k += 1
        n -= subtraction
        if n == 0:
            print('1')
            return
epicgame()
