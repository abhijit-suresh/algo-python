# https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == ".":
                    continue
                if item in row_sets[r]:
                    return False
                if item in col_sets[c]:
                    return False
                if item in subgrid_sets[r // 3][c // 3]:
                    return False
                row_sets[r].add(item)
                col_sets[c].add(item)
                subgrid_sets[r // 3][c // 3].add(item)
        return True
