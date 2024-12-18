def main():
    r, c = map(int, input().split())
    x = []
    for _ in range(r):
        x.append(input())
    name = ['v', 'i', 'k', 'a']
    p=0
    for j in range(c):
        for i in range(r):
            if x[i][j] == name[p]:
                p += 1
                break
        if p == 4:return 'YES' ;
    return 'NO'


for _ in range(int(input())):
    print(main())

