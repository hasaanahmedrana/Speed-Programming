for _ in range(int(input())):
    n, k = map(int,input().split())
    s = [i for i in input()]
    set_s = list(set(s))
    counts = [s.count(i) for i in set_s]
    odds = [i for i in counts if i % 2]
    print('YES') if len(odds) - k <= 1 else print('NO')
