class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)): return False;
        dic = dict()
        for i, j in zip(s, t):
            if i in dic and dic[i] != j: return False;
            dic[i] = j
        print(dict)
        return True

