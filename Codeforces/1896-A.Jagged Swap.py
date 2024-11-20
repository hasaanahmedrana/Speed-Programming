I = input;
P = print
for _ in range(int(I())):
    n = int(I())
    x = list(map(int, I().split()))
    if x[0] != min(x):
        P('NO')
        continue
    P('YES')
