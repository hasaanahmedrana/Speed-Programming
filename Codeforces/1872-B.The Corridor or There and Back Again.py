def main():
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst.sort()
    results = []
    for j in range(n):
        x = lst[j][0];y = lst[j][1]
        if y % 2 == 0: y -= 1;
        results.append(x + y // 2)
    return min(results)

for _ in range(int(input())):
    print(main())
