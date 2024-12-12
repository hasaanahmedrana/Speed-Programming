# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def length(l1):
    x = 0
    temp = l1
    while temp:
        x += 1
        temp = temp.next
    return x


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = length(l1);
        len2 = length(l2)
        out = [0] * ((max(len1, len2)) + 1)
        i = 0
        temp1 = l1
        temp2 = l2
        while temp1:
            out[i] += temp1.val
            temp1 = temp1.next
            i += 1
        i = 0
        while temp2:
            out[i] += temp2.val
            temp2 = temp2.next
            i += 1

        for i in range(len(out)):
            if out[i] > 9:
                out[i] = out[i] - 10
                out[i + 1] += 1
        if out[-1] == 0: out = out[:-1];
        head = ListNode(out[0])
        temp = head
        i = 1
        while i < len(out):
            temp.next = ListNode(out[i])
            i += 1
            temp = temp.next

        return head

