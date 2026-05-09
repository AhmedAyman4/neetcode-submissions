# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # arr to stor the linkedlist
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        # find and remove the nth element
        index_to_remove = len(arr)-n
        arr.pop(index_to_remove)

        # make sure arr is not empty
        if not arr:
            return None

        # make the new linkedlist after deleteing the nth element
        dummy = ListNode(0)
        cur = dummy
        for value in arr:
            cur.next = ListNode(value)
            cur = cur.next

        return dummy.next # new head of the list
