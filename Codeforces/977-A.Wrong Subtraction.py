def main():
    num, k = map(int, input().split())
    for j in range(k):
        if num % 10 == 0:
            num = num // 10
        else:
            num -= 1
    return num


print(main())