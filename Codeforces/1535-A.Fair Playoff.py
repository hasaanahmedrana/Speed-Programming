def main():
    p = list(map(int,input().split()))
    x = [max(p[0],p[1]), max(p[2],p[3])]
    maxi = max(p); p.remove(maxi)
    maxi2 = max(p)
    return 'YES' if (maxi in x and maxi2 in x) else 'NO'

for _  in range(int(input())):
    print(main())