def main():
    n = int(input())
    k=2
    while n%(2**k-1)!=0:
        k+=1
    return n//(2**k-1)
for _ in range(int(input())):
    print(main())
