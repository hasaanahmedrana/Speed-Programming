from itertools import *


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        codes = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y','z'],
        }
        combinations = []

        if len(digits) == 0 or (not digits.isnumeric()):
            return combinations;
        else:
            lsts = [codes[int(each)] for each in digits]
            combinations = product(*lsts)
            combinations = [''.join(each) for each in list(combinations)]
            return combinations

#
# # Test cases
# test = Solution()
# print(test.letterCombinations('23'))