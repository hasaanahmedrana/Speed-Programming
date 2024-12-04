def main():
    n = int(input())
    x = list(map(int,input().split()));
    x = [i for i in x if i<=n]
    x.sort()
    y = [i for i in range(1,len(x)+1)]
    for i in range(len(x)-1,-1,-1):
        if x[i]<=y[i]:
            return i+2
    return 1
for _ in range(int(input())):
    print(main())
