
def main():
    n = int(input())
    x = list(input())
    if n == 1 or (n == 2 and x[0] >= x[1]):return 'NO'
    print('YES')
    print(2)
    return f"{x[0]} {''.join(x[1:])} "


for _ in range(int(input())):
   print(main())
