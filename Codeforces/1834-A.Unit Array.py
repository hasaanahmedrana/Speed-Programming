I = input
P = print
for _ in range(int(I())):
    n = I()
    x = list(map(int, I().split()))
    neg = x.count(-1)
    pos = x.count(1)
    count = 0
    while True:
        if neg % 2:
            neg -= 1
            pos += 1
            count += 1
        if neg > pos:
            neg -= 1
            pos += 1
            count += 1
        else:
            P(count)
            break
