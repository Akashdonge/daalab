class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])

        def helper(ans, start, target, cur_count, M, visited, grid):
            if start == target:
                if cur_count == M:
                    return ans + 1
                else:
                    return ans
                
            x, y = start
            for i in range(4):
                next_x, next_y = x + directions[i], y + directions[i + 1]

                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y] and grid[next_x][next_y] != -1:
                    visited[next_x][next_y] = True
                    ans = helper(ans, (next_x, next_y), target, cur_count + 1, M, visited, grid)
                    visited[next_x][next_y] = False
                
            return ans
        
        start, target = None, None
        M = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    target = (i, j)
                elif grid[i][j] == -1:
                    M += 1

        M = m * n - M
                
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[start[0]][start[1]] = True
        return helper(0, start, target, 1, M, visited, grid)



