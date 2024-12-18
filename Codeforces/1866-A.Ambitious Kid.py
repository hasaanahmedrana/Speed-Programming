def main():
    n = int(input())
    nums = list(set(list(map(int,input().split()))))
    x = [abs(i) for i in nums]
    return min(x)
print(main())

