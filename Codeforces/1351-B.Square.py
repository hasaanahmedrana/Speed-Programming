for _ in range(int(input())):
    a,b = sorted(map(int,input().split()))
    c,d = sorted(map(int,input().split()))
    print('YES') if a+c == b == d else print('NO')