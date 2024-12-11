def main():
    n, a, b = map(int, input().split())
    if n == 2: return [a, b];
    x = [i for i in range(1, n + 1) if i != a and i != b]
    y = x[:(n - 2) // 2];
    z = x[(n - 2) // 2:]
    if max(y) >= b or min(z) <= a:
        return -1
    else:
        ans = [a] + z + [b] + y
        return ans


for _ in range(int(input())):
    result = main()
    print(result) if result == -1 else print(*result)
