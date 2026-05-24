class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Create adjacency list
        # Example:
        # prerequisites = [[1,0]]
        # means: to take course 1, you must first take 0
        #
        # prereq will look like:
        # {
        #   0: [],
        #   1: [0]
        # }
        prereq = {c: [] for c in range(numCourses)}

        # Fill the adjacency list
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # Stores the final valid course order
        output = []

        # cycle -> tracks nodes currently in DFS path
        # visit -> tracks nodes already completely processed
        cycle, visit = set(), set()

        # DFS function to check if we can finish this course
        def dfs(crs):

            # If course already in current DFS path,
            # then we found a cycle
            # Example: 1 -> 2 -> 1
            if crs in cycle:
                return False

            # If already processed before,
            # no need to do work again
            if crs in visit:
                return True

            # Add current course to current DFS path
            cycle.add(crs)

            # Visit all prerequisites first
            for pre in prereq[crs]:

                # If prerequisite creates a cycle,
                # return False immediately
                if dfs(pre) == False:
                    return False

            # Finished processing current course,
            # remove from current DFS path
            cycle.remove(crs)

            # Mark course as completely processed
            visit.add(crs)

            # Add course after prerequisites are done
            # This gives topological order
            output.append(crs)

            return True

        # Run DFS for every course
        for c in range(numCourses):

            # If cycle exists, impossible to finish courses
            if dfs(c) == False:
                return []

        # Return valid order of courses
        return output