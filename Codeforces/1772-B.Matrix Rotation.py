def is_beautiful():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if (a < b and c < d) and (a < c and b < d):
        return "YES"
    else:
        for j in range(4):
            _a = a
            _b = b
            _c = c
            _d = d
            a = _b
            b = _d
            c = _a
            d = _c
            if (a < b and c < d) and (a < c and b < d):
                return 'YES'
        return "NO"
t = int(input())
for i in range(t):
    print(is_beautiful())
