class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create indegree map of course prerequsites (topological sort)
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visit set to check for cycles
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []: # no prerequisites
                return True # this course can be completed
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True