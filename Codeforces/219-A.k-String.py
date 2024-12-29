def main():
    k = int(input())
    s = list(input())
    set_s = list(set(s));
    set_s.sort()
    nums = [];
    x = []
    for each in set_s:
        i = s.count(each)
        if i % k != 0:
            return -1
        else:
            nums.append(i // k)
    for i in range(len(nums)):
        for j in range(nums[i]):
            x.append(set_s[i])
    x = x * k
    return ''.join(x)


print(main())