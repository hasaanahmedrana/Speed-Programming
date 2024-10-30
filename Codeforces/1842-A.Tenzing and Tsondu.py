def compete(x, y):
    a = x - y
    b = y - x
    return a, b


def who_win():
    n1, n2 = map(int, input().split())
    a2 = input().split()
    a = [int(i) for i in a2]
    b2 = input().split()
    b = [int(i) for i in b2]

    while True:
        a[0], b[0] = compete(a[0], b[0])
        if a[0] <= 0:
            a.remove(a[0])
        if b[0] <= 0:
            b.remove(b[0])
        if a == [] and b == []:
            print("Draw")
            return
        elif a == []:
            print("Tenzing")
            return
        elif b == []:
            print("Tsondu")
            return


t = int(input())
for i in range(t):
    who_win()