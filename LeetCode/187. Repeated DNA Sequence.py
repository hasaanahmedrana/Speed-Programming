class Solution(object):
    def findRepeatedDnaSequences(self,s):
        count = dict()
        lst = []
        result= []
        for i in range(len(s)-9):
            part = s[i:i+10]
            count[part] = 1 + count.get(part,0)
            if count.get(part,0) > 1:
                result += [part]
        return list(set(result))

