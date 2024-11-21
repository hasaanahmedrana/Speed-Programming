class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        maxii = 0
        for i in range(len(s)):
            pairs = {s[i]:1}
            for j in range(i + 1, len(s)):
                if s[j] in pairs:
                    break
                pairs[s[j]] = 1
            maxii = max(maxii, len(pairs))
            pairs = {}
        return maxii

