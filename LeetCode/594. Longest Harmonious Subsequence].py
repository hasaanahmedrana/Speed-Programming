class Solution(object):
    def findLHS(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0;  end = 0;
        if len(set(arr)) == 1: return 0
        arr.sort()
        length = 0
        for i in range(len(arr)):
            if arr[end]-arr[start] > 1:
                start += 1
            if arr[end]-arr[start] == 1:
                length = end + 1 - start
            end += 1
        return length

