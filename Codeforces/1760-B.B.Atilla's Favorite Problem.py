def main():
    l=int(input())
    s=list(input())
    s.sort()
    return ord(s[-1])-96
for _ in range(int(input())):
    print(main())
