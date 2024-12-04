def main():
    l = int(input())
    x = list(map(int,input().split()))
    y =sorted(x); x.reverse();y.reverse();
    for i in range(l):
        if x[i]!=y[i]:
            return max(x[i:])
    return 0
for _ in range(int(input())):
    print(main())


