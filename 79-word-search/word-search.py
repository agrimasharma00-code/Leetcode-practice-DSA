class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # Word completely found
            if k == len(word):
                return True

            # Check boundaries and character
            if (i < 0 or i >= m or j < 0 or j >= n
                or board[i][j] != word[k]):
                return False

            # Mark cell as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Explore all four directions
            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            # Backtrack: restore original character
            board[i][j] = temp

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False