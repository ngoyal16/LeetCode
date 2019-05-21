class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0

        for move in moves:
            if move == 'U':
                x = x - 1
            elif move == 'D':
                x = x + 1
            elif move == 'L':
                y = y + 1
            elif move == 'R':
                y = y - 1
                
        return x == 0 and y == 0
