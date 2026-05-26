from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        
        # Step 1: Build adjacency list representation of the graph
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Create a set to track visited nodes
        visited = set()

        # Step 3: Counter for connected components
        components = 0

        # Step 4: DFS function to visit all connected nodes
        def dfs(node):

            # Mark current node as visited
            visited.add(node)

            # Visit all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Step 5: Traverse all nodes in the graph
        for node in range(n):

            # If node is unvisited, it starts a new component
            if node not in visited:

                # Visit the entire connected component
                dfs(node)

                # Increment component count after DFS finishes
                components += 1

        # Step 6: Return total number of connected components
        return components