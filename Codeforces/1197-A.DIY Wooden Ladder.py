def main():
    l = int(input())
    y = list(map(int, input().split()))
    if l < 3 : return 0 ;
    maxi = max(y); y.remove(maxi)
    sec_maxi = max(y); y.remove(sec_maxi)
    if sec_maxi < 2: return 0;
    z = len(y)
    if z >= sec_maxi:
        z = sec_maxi-1
    return z


for _ in range(int(input())):
    print(main())
