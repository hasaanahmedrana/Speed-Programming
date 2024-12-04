def main():
    elems= []
    n,m =map(int,input().split())
    for _ in range(n*2):
        elems.append(list(map(int,input().split())))
    if m%2: return 'NO';
    for i in range(0,n*2-1,2):
        if  elems[i][1]==elems[i+1][0]:
            return 'YES'
    return 'NO'
for _ in range(int(input())):
    print(main())
