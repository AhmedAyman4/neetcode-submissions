# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # They met → cycle exists

        return False  # fast reached None → no cycle

        # visited = set()
        # cur = head
        # while cur :
        #     if cur in visited:
        #         return True
        #     visited.add(cur)
        #     cur = cur.next
        # return False