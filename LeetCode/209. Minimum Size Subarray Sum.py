class Solution(object):
    def minSubArrayLen(self, target, num):
        if max(num) >= target:
            return 1
        if num == []:
            return 0
        left = 0;
        summ = 0
        length = float('+inf')
        for right in range(len(num)):
            summ += num[right]
            while summ >= target:
                if (right - left + 1) < length:
                    length = right - left + 1
                summ -= num[left]
                left += 1
        return length if length <= len(num) else 0


