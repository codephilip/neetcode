class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        # iterative
        curr, prev = head, None

        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

        return prev  # this is now the new head of the return list.
