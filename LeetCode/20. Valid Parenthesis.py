class Solution(object):
    def isValid(self, s):
        from collections import deque
        stack = deque([])
        matching = {'[': ']', '{': '}', '(': ')'}
        for i in s:
            if i in matching:
                stack.append(i)
            else:
                if not stack or matching[stack.pop()] != i:
                    return False
        return not stack

