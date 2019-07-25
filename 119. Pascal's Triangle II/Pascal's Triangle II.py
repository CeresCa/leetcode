class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}

    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex + 1):
            row = list(map(lambda x, y: x + y, [0] + row, row + [0]))
        return row