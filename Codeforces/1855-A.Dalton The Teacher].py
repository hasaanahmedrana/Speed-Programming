def main():
    l = int(input())
    elem = list(map(int,input().split()))
    x = sorted(elem)
    count = 0
    for i in range(l):
        if elem[i] == x[i]: count += 1
    return count//2 + count%2


for _ in range(int(input())):
    print(main())
