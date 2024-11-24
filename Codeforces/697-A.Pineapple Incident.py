t, s, x = map(int, input().split())
if x - t == 1:
    print('NO')
elif x < t:
    print('NO')
else:
    n = (x - t) % s
    sol = [0, 1]
    print('YES' if n in sol else 'NO')

