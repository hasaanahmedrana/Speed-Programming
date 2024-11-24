for _ in range(int(input())):
    a,b=map(int,input().split())
    if abs(a-b)%2:
        print('Alice')
    else:
        print('Bob')

