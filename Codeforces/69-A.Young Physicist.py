def main():
    a, b, c = 0, 0, 0
    for _ in range(int(input())):
        x, y, z = map(int, input().split())
        a += x;b += y;c += z
    if a == b == c == 0:
        return 'YES'
    else: return 'NO';
print(main())
