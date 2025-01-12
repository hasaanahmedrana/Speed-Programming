def equalize():
    l, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    if abs((nums[0] + k) - nums[0]) <= k and abs((nums[0] + k) - nums[-1]) <= k:
        return nums[0] + k
    else:
        return -1


for _ in range(int(input())):
    print(equalize())
