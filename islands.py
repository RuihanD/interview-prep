

from collections import deque
class Solution:
    @staticmethod
    def findCountSameIslands(grid1, grid2):
        rows = len(grid1)
        cols = len(grid1[0])
        cnt = 0
        que1 = deque()
        que2 = deque()

        def bfs():
            tag = True
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while que1 and que2:
                r1, c1 = que1.popleft()
                r2, c2 = que2.popleft()
                if grid1[r1][c1] != grid2[r2][c2]:
                    tag = False
                for dr, dc in dirs:
                    R1 = r1 + dr
                    C1 = c1 + dc
                    R2 = r2 + dr
                    C2 = c2 + dc
                    if 0 <= R1 < rows and 0 <= C1 < cols and grid1[R1][C1] == 1:
                        grid1[R1][C1] = 0
                        que1.append([R1, C1])
                    if 0 <= R2 < rows and 0 <= C2 < cols and grid2[R2][C2] == 1:
                        grid2[R2][C2] = 0
                        que2.append([R2, C2])
            if que1 or que2:
                tag = False
            else:
                return tag

            while que1:
                r1, c1 = que1.popleft()
                for dr, dc in dirs:
                    R1 = r1 + dr
                    C1 = c1 + dc
                    if 0 <= R1 < rows and 0 <= C1 < cols and grid1[R1][C1] == 1:
                        grid1[R1][C1] = 0
                        que1.append([R1, C1])
            while que2:
                r2, c2 = que2.popleft()
                for dr, dc in dirs:
                    R2 = r2 + dr
                    C2 = c2 + dc
                    if 0 <= R2 < rows and 0 <= C2 < cols and grid2[R2][C2] == 1:
                        grid2[R2][C2] = 0
                        que2.append([R2, C2])
            return tag

        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 1 and grid2[r][c] == 1:
                    que1.append([r,c])
                    que2.append([r,c])
                    if bfs():
                        cnt += 1
        return cnt

    @staticmethod
    def main():
        grid1 = [[0,1,1], [0,1,1], [0,0,0]]
        grid2 = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
        print(Solution.findCountSameIslands(grid1, grid2))
        grid1 = [[0, 1, 0], [0, 1, 1], [0, 0, 0]]
        grid2 = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
        print(Solution.findCountSameIslands(grid1, grid2))
        grid1 = [[0,1,1], [0,1,1], [1,0,0]]
        grid2 = [[0, 1, 1], [0, 1, 1], [1, 0, 0]]
        print(Solution.findCountSameIslands(grid1, grid2))
        grid1 = [[0, 1, 0], [0, 1, 1], [1, 0, 0]]
        grid2 = [[0, 1, 1], [0, 1, 1], [1, 0, 0]]
        print(Solution.findCountSameIslands(grid1, grid2))

if __name__ == "__main__":
    Solution.main()
