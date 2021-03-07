# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        output, share = self.addTwoNumber(l1, l2, 0)
        l1, l2 = self.moveNext(l1, l2)
        if output.val == 0 and share == 0 and l1 is None and l2 is None:
            return output
        tmp_output = output
        while True:
            if l1 is None and l2 is None and share == 0:
                break
            tmp_output.next, share = self.addTwoNumber(l1, l2, share)
            tmp_output = tmp_output.next
            l1, l2 = self.moveNext(l1, l2)
        return output

    def addTwoNumber(self, l1: ListNode, l2: ListNode, last_share: int) -> (ListNode, int):
        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val
        sum_l1l2 = l1_val + l2_val + last_share
        share, remain = divmod(sum_l1l2, 10)
        output = ListNode(remain)
        return output, share

    def moveNext(self, l1: ListNode, l2: ListNode) -> (ListNode, ListNode):
        next_l1 = None if l1 is None else l1.next
        next_l2 = None if l2 is None else l2.next
        return next_l1, next_l2
