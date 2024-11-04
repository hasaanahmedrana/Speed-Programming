def whoWins():
    n = int(input())
    s = list(map(int, input(). split ()))
    maxii = max(s)
    p = s.index(maxii)+1
    s.remove(maxii)
    maxii2 = max(s)
    print(f'{p} {maxii2}')
whoWins()
