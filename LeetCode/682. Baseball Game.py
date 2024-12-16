class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = []
        for i in operations:
            print(i)
            if i == '+':
                result.append(sum(result[-2:]))
            elif i == 'D':
                result += [result[-1] * 2]
            elif i == 'C':
                result = result[:-1]
            else:
                result.append(int(i))

            print(result)
        return sum(result)