# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = l1
        total = 0
        carry = 0
        prev_l1 = l1
        while l1 and l2: 
            total = l1.val + l2.val + carry
            carry = 0
            if total > 9:
                carry = total // 10
                total = total % 10
            l1.val = total
            prev_l1 = l1
            l1 = l1.next
            prev_l1.next = l1
            l2 = l2.next
        while l1:   
            total = l1.val + carry 
            carry = 0
            if total > 9:
                carry = total // 10
                total = total % 10
            l1.val = total
            
            prev_l1 = l1
            l1 = l1.next
            prev_l1.next = l1
            
        while l2:
            total = l2.val + carry 
            carry = 0
            if total > 9:
                carry = total // 10
                total = total % 10
            l1 = ListNode(total)
            prev_l1.next = l1
            prev_l1 = l1
            l2 = l2.next
        if carry != 0:
            l1 = ListNode(carry)
            prev_l1.next = l1
            
        
        return result_node