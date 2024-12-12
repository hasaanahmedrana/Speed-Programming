# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        elems = []
        temp = head
        while temp:
            if temp.val not in elems:
                elems.append(temp.val)
            temp = temp.next
        if elems == []: return None
        new_head = ListNode(elems[0])
        temp = new_head
        i = 1
        while i < len(elems):
            temp.next = ListNode(elems[i])
            i += 1
            temp = temp.next
        return new_head


