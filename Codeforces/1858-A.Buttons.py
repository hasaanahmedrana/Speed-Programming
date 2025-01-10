def main():
    a, b, c = map(int, input().split())
    x = a + c
    y = b + c
    if x > y:
        print('First')
    elif y > x:
        print('Second')
    elif x == y:
        if c % 2 != 0:
            print('First')
        else:
            print('Second')


for _ in range(int(input())):
    main()