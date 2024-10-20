def increaing():
    n = int(input(''))
    for i in range(n):
        input_length = int(input(''))
        inp = list(map(int, input().split()))
        b = set(inp)
        length_set = len(b)
        if length_set == input_length:
            print('YES')
        else:
            print('NO')
increaing()