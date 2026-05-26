class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visit = set()
        components = 0

        def dfs(node):
            visit.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visit:
                dfs(node)
                components += 1
        return components