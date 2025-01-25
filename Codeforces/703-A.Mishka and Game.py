def main():
    n = int(input())
    m = c = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > b: m += 1;
        if b > a: c += 1;
    if m == c: return 'Friendship is magic!^^';
    return 'Mishka' if m > c else 'Chris'
print(main())