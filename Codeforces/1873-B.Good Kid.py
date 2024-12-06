def main():
    n = int(input())
    x = sorted(list(map(int, input().split())))
    x[0] += 1
    result = 1
    for i in x:
        result *= i
    return result


for _ in range(int(input())):
    print(main())