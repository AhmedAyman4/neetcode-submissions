from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        q = deque()  # stores indices (not values)

        for right in range(len(nums)):
            # 1. Remove smaller numbers from the back (not useful anymore)
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # 2. Add the current index
            q.append(right)

            # 3. Remove leftmost index if it's outside the window
            if q[0] < right - k + 1:
                q.popleft()

            # 4. Record the max once the first full window is formed
            if right >= k - 1:
                output.append(nums[q[0]])

        return output
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        q = deque()  # stores indices (not values)

        for right in range(len(nums)):
            # 1. Remove smaller numbers from the back (not useful anymore)
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # 2. Add the current index
            q.append(right)

            # 3. Remove leftmost index if it's outside the window
            if q[0] < right - k + 1:
                q.popleft()

            # 4. Record the max once the first full window is formed
            if right >= k - 1:
                output.append(nums[q[0]])

        return output
