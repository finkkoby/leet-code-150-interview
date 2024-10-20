# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            target = head
            target.checked = True
        else:
            return False
        while target.next:
            if getattr(target.next, "checked", None):
                return True
            else:
                target.next.checked = True
            target = target.next