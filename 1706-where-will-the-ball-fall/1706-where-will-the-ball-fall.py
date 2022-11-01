class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M: int = len(grid)
        N: int = len(grid[0])
        result: List[int] = [-1] * N

        for col in range(N):
            ball: int = col

            for row in range(M):
                if grid[row][ball] == 1 and ball < N-1 and grid[row][ball+1] == 1:
                    ball += 1
                elif grid[row][ball] == -1 and ball > 0 and grid[row][ball-1] == -1:
                    ball -= 1
                else:
                    break

                if row == M-1:
                    result[col] = ball

        return result