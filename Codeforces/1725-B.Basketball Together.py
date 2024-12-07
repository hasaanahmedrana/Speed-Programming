import math
def main():
    n, m = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    m += 1;count = 0
    while len(x) > 0:
        i = math.ceil(m/x[-1])
        if len(x) >= i:
            count += 1
        x.pop(-1)
        del x[:i -1 ]
    return count


print(main())