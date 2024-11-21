class Solution:
    def twoSum(self,lst,target):
        hash_map = {}
        for inx,elem in  enumerate(lst):
            if target-elem in hash_map:
                return [inx,hash_map[(target-elem)]]
            else:
                hash_map[elem] = inx
        return [-1, -1]
