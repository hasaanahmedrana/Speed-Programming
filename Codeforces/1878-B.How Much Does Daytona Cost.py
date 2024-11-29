def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    return 'YES' if k in x else'NO'
for _ in range(int(input())):
    print(main())

