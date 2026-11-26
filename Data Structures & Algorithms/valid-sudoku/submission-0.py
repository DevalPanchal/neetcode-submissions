class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = set()
        colSeen = set()
        boxSeen = set()

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                # empty cells never conflict
                if digit == ".":
                    continue

                box = (row // 3, col // 3)

                # already seen in this row, column, box
                if (row, digit) in rowSeen:
                    return False
                if (col, digit) in colSeen:
                    return False
                if (box, digit) in boxSeen:
                    return False

                rowSeen.add((row, digit))
                colSeen.add((col, digit))
                boxSeen.add((box, digit))

        # no conflict
        return True