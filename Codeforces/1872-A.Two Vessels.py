import math
def main():
    a, b, c = map(int, input().split())
    if a == b:return 0;
    if c > abs(a - b): return 1;
    n = abs(a - b) / 2
    return math.ceil(n / c)


for _ in range(int(input())):
    print(main())
