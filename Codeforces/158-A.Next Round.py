def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    x = nums[k - 1]
    y = [i for i in nums if (i >= x and i > 0)]
    return len(y)


print(main())