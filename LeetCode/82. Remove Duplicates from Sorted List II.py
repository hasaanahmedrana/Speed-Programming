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
        count = dict()
        temp = head
        while temp:
            if str(temp.val) not in count:
                count[str(temp.val)] = 1
            else:
                count[str(temp.val)] += 1

            temp = temp.next
        fake = ListNode(-1)
        fake_head = fake
        temp = head
        while temp:
            if count[str(temp.val)] == 1:
                fake.next = temp
                fake = fake.next
            temp = temp.next

        fake.next = None

        return fake_head.next



