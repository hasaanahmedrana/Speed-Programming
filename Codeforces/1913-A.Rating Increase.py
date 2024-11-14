for _ in range(int(input())):
    n = input()
    f = 0
    for i in range(1, len(n) // 2 + 1):
        if int(n[:i]) and int(n[i:]) and int(n[:i]) < int(n[i:]) and int(n[i]) != 0:
            print(int(n[:i]), int(n[i:]))

            f = 1
        if f == 1:
            break
    if f == 0:
        print(-1)