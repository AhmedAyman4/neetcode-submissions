class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we are going from the oceans to the inside 
        # the water flows from the high areas to low areas if we are going from inside out
        # if going reverse from out to inside then low to high
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r, c, visit, prevHeight):
            # define base cases
            if (r, c) in visit:
                return
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if heights[r][c] < prevHeight:
                return 

            visit.add((r, c))

            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if ((r,c) in atl and (r,c) in pac):
                    res.append([r,c])
        return res
            