def main():
    n = int(input())
    x = list(map(int, input().split()));x.sort()
    y = list(map(int, input().split()));y.sort()
    for j in range(n):
        if x[j] != y[j]:
            x[j] += 1
    return 'YES' if x == y else ('NO')


for _ in range(int(input())):
   print(main())
