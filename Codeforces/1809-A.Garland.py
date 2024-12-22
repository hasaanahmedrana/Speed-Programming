def main():
    x = list(input())
    y = [x.count(i) for i in list(set(x))]
    return -1 if max(y) == 4 else 6 if max(y) == 3 else 4


for _ in range(int(input())):
    print(main())
