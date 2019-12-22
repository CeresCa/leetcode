class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        return (
            self.isValidRow(board)
            and self.isValidColumn(board)
            and self.isValidSquare(board)
        )

    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True

    def isValidColumn(self, board):
        for column in zip(*board):
            if not self.isValidUnit(column):
                return False
        return True

    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValidUnit(square):
                    return False
        return True

    def isValidUnit(self, unit):
        unit = [i for i in unit if i != "."]
        return len(set(unit)) == len(unit)
