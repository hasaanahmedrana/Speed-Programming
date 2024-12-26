def main():
    a, b = map(int, input().split())
    if a % 2 and b % 2:
        return (-(b - ((b - a) // 2)))
    elif a % 2 == 0 and b % 2 == 0:
        return (b - ((b - a) // 2))
    elif a % 2 == 0 and b % 2 != 0:
        return -((b - a) - ((b - a) // 2))
    else:
        return ((b - a) // 2) + 1


for _ in range(int(input())):
    print(main())