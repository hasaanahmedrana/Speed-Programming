def main():
    n, m = map(int, input().split())
    nums = []
    luckiness = []
    if n == m:
        return n
    for i in range(n, m + 1):
        str_i = str(i)
        x = [int(j) for j in str_i]
        z = max(x) - min(x)
        if z == 9:
            return i
        luckiness.append(z)
        nums.append(i)
    luckiest_idx = luckiness.index(max(luckiness))
    return nums[luckiest_idx]

for _ in range(int(input())):
    print(main())
