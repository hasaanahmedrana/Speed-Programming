class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dic = {}
        s_dic = {}
        p_len = len(p)
        s_len = len(s)
        idx = []
        for each in p:
            p_dic[each] = p_dic.get(each, 0) + 1
        popp = 0
        n = 0
        for i in range(s_len):

            if s[i] in p:
                s_dic[s[i]] = 1 + s_dic.get(s[i], 0)
            if n == p_len:
                if s[popp] in p:
                    s_dic[s[popp]] = s_dic.get(s[popp],0) - 1
                popp += 1
                n -= 1
            if s_dic == p_dic:
                idx += [i + 1- len(p)]
                print()

            n += 1
        return idx