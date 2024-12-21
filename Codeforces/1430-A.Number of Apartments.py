def main():
    n = int(input())
    if n < 3: return -1
    if n % 7 == 0: return [0, 0, n // 7];
    if n % 5 == 0: return [0, n // 5, 0]
    if n % 3 == 0: return [n // 3, 0, 0]
    ans = [0, 0, 0]
    for i in range(3, 8, 2):
        m = n - i
        if m < 3: return -1
        if m % 3 == 0:
            ans[0] = m // 3
        elif m % 5 == 0:
            ans[1] = m // 5
        elif m % 7 == 0:
            ans[2] = m // 7
        if m % 3 == 0 or m % 5 == 0 or m % 7 == 0:
            if i == 3: ans[0] += 1;
            if i == 5: ans[1] += 1;
            if i == 7: ans[2] += 1;
            return ans
    return -1


for _ in range(int(input())):
    z = main()
    if z == -1:
        print(-1);
    else:
        print(*z)

