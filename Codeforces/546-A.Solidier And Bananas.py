def banana(k, w):
    ans = 0
    while w > 0:
        ans += w*k
        w -= 1
    return ans
def main():
    k, n, w = map(int, input().split())
    required = banana(k, w)
    return required - n if required > n else 0
print(main())
print(main())