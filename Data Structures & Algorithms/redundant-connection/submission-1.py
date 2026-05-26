class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # Number of nodes = number of edges (since it's a tree + 1 edge)
        
        # Step 1: Create adjacency list to represent the graph
        adj = [[] for _ in range(n + 1)]
        
        def dfs(node, parent):
            """
            DFS to detect if there's a cycle.
            Returns True if cycle is found.
            """
            # Step 2: If we visit a node that's already visited → Cycle detected!
            if visit[node]:
                return True
            
            # Mark current node as visited
            visit[node] = True
            
            # Step 3: Visit all neighbors
            for nei in adj[node]:
                if nei == parent:
                    continue  # Skip the parent (avoid going back immediately)
                
                # If we find a cycle in any subtree, return True
                if dfs(nei, node):
                    return True
            
            return False  # No cycle found from this path
        
        # Step 4: Add edges one by one and check for cycle
        for u, v in edges:
            
            # Add current edge to the graph
            adj[u].append(v)
            adj[v].append(u)
            
            # Reset visited array before each DFS check
            visit = [False] * (n + 1)
            
            # Step 5: Check if adding this edge creates a cycle
            # We start DFS from u. If we can reach any already visited node (except parent),
            # it means there's already a path between u and v → cycle!
            if dfs(u, -1):
                return [u, v]  # This edge is redundant
        
        # If no redundant edge found (should not happen as per problem)
        return []