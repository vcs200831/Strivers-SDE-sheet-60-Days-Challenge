class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #build the graph O(n) time and space
        adj_list = defaultdict(set)
        for stone in stones:
            x, y = stone
            adj_list[(x,'x')].add(tuple(stone))
            adj_list[(y,'y')].add(tuple(stone))
            
        #DFS to connect the graph/islands O(n) time
        def dfs(stone):
            x, y = stone
            visited.add(stone)
            neighbors = adj_list[(x, 'x')].union(adj_list[(y, 'y')])
            for nei in neighbors-visited:
                dfs(nei)
                
        #iterate every stone and DFS to get the connected components
        visited = set()
        ans = len(stones)
        for stone in stones:
            if tuple(stone) not in visited:
                dfs(tuple(stone))
                ans -= 1
        #every component needs atleast one node, so subtracting it from total stones is the answer
        return ans