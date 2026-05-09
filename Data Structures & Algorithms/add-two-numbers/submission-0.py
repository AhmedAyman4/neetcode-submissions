# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Convert linked list to number
        def toNumber(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        # Step 2: Convert number back to linked list
        def toLinkedList(num):
            # Edge case: if num = 0
            if num == 0:
                return ListNode(0)

            dummy = ListNode()
            curr = dummy

            while num > 0:
                digit = num % 10
                curr.next = ListNode(digit)
                curr = curr.next
                num //= 10

            return dummy.next

        # Convert both lists to integers
        num1 = toNumber(l1)
        num2 = toNumber(l2)

        # Sum them
        total = num1 + num2

        # Convert result back to linked list
        return toLinkedList(total)