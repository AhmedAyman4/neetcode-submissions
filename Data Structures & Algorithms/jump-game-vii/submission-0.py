class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q, farthest = deque([0]), 0

        while q:
            i = q.popleft()

            start = max(i+minJump, farthest+1)
            end = min(i+maxJump, n-1)

            for j in range(start, end+1):
                if s[j] == "0":
                    if j == n-1:
                        return True
                    q.append(j)
                farthest = end
        # special case
        return n == 1