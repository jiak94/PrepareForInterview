class Solution(object):
    def exist(self, board, word):
        if not word:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, []):
                        return True
        return False
        
    def dfs(self, board, word, x, y, visited):
        if len(word) == 0:
            return True
        if (x, y) in visited:
            return False
        
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
    
        if board[x][y] != word[0]:
            return False
        else:
            visited.append((x, y))
        
        up = self.dfs(board, word[1:], x+1, y, visited)
        down = self.dfs(board, word[1:], x-1, y, visited)
        left = self.dfs(board, word[1:], x, y - 1, visited)
        right = self.dfs(board, word[1:], x, y+ 1, visited)
        
        if not (up or down or left or right):
            visited.pop()
            return False
        return True