I = input; P= print
for _ in range(int(I())):
    n = int(I())
    lst = list(map(int, input().split()))
    count = 0; maxii = 0; summ = 0
    for i in range(n):
        summ += lst[i]
        maxii = max(maxii,lst[i])
        if summ - (2 * maxii) == 0:count += 1;
    P(count)