def main():
    n = int(input())
    x = list(map(int,input().split()))
    y = 1 if x[0]!=1 else 2
    for i in range(1,n):
        if y+1 ==x[i]:
            y+=2
        else:
            y+=1
    return y
for _ in range(int(input())):
    print(main())

