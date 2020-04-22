class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        rookX, rookY = [(ix, iy) for ix, row in enumerate(board) for iy, i in enumerate(row) if i == 'R'][0]
        
        count = 0
        
        for i in range(rookX-1, -1, -1):
            if board[i][rookY] == "p":
                count = count + 1
                break
            elif board[i][rookY] != ".":
                break
            
        for i in range (rookX + 1, 8):
            if board[i][rookY] == "p":
                count = count + 1
                break
            elif board[i][rookY] != ".":
                break
        for i in range(rookY-1, -1, -1):
            if board[rookX][i] == "p":
                count = count + 1
                break
            elif board[rookX][i] != ".":
                break
            
        for i in range (rookY + 1, 8):
            if board[rookX][i] == "p":
                count = count + 1
                break
            elif board[rookX][i] != ".":
                break
                
        return count
            
