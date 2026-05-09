class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n , m = len(s1) , len(s2)
        # if len s1 > len s2 return false
        if n > m:
            return False
        s1_count = Counter(s1)
        window_count = Counter(s2[:n])

        if s1_count == window_count:
            return True
        
        for i in range(n, m):
            # add new char 
            window_count[s2[i]] += 1
            # remove left char
            window_count[s2[i-n]] -= 1
            if window_count[s2[i-n]] == 0:
                del window_count[s2[i-n]]
            # compare the s1 count with the current window of s2
            if s1_count == window_count:
                return True
        return False