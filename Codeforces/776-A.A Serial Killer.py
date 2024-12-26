def main():
    a = input().split()
    print(*a)
    for _ in range(int(input())):
        x, y = input().split()
        if x in a: a.remove(x);a.append(y)
        else: a.remove(y);a.append(x)
        print(*a)
main()