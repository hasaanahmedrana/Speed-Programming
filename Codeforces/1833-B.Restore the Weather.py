def main():
    n, l = map(int, input().split())
    day = list(map(int, input().split()))
    w = list(map(int, input().split()));w.sort()
    days = []
    for idx, elem in enumerate(day):
        x = [elem, idx]
        days.append(x)
    days.sort()
    result = [0] * n
    for j in range(n):
        result[days[j][1]] = w[j]
    return result

for _ in range(int(input())):
    ans = main()
    print(*ans)
