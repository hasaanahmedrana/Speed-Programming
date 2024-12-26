def main():
    l = int(input())
    elems = list(map(int, input().split()))
    x = [i for i in elems if i % 2 != 0]
    return 'NO' if len(x) % 2 != 0 else 'YES'

for _ in range(int(input())):
    print(main())