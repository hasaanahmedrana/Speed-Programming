def main():
    l = int(input())
    c = 0
    s = input()
    for i in range(l//2):
        if s[i] != s[(-1 * (i + 1))]:
            c += 1
        else: break;
    return l - (c * 2)


for _ in range(int(input())):
    print(main())

