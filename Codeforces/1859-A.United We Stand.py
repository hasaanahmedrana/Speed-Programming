def main():
    l = int(input())
    x = list(map(int,input().split()))
    y = [i for i in x if i==min(x)]
    z = [i for i in x if i!=min(x)]
    if z == []:
        return -1,-1
    print(f'{len(y)} {len(z)}')
    return y,z

for _ in range(int(input())):
    a,b = main()
    if a==b:
        print(b)
    else:
        print(*a)
        print(*b)

