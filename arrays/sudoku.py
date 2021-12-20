class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        for row in board:
            for num in row:
                d[num] = d.get(num, 0) + 1
                if d[num] > 1 and num != ".":
                    return False
            d.clear()
        for col in range(9):
            for num in range(9):
                val = board[num][col]
                d[val] = d.get(val, 0 ) + 1
                if d[val] > 1 and val != ".":
                    return False
            d.clear()
        for box in range(9):
            start = self.fixBox(box)
            for num in range(9):
                if (box == 4):
                val = board[start + int(num/3)][num%3 + 3*(box%3)]
                d[val] = d.get(val,0) + 1
                if d[val] > 1 and val != ".":
                    #print(d)
                    return False
            d.clear()
        return True

    def fixBox(self, box):
        if box in [0,1,2]:
            row = 0
        elif box in [3,4,5]:
            row = 3
        else:
            row = 6
        return row
