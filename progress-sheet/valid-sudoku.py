class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxes = {
            1 : [],
            2 : [],
            3 : [],
            4 : [],
            5 : [],
            6 : [],
            7 : [],
            8 : [],
            9 : [],
        }    

        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != '.':
                    row.append(board[i][j])
                    if i < 3 and j < 3:
                        boxes[1].append(board[i][j])
                    elif i < 3 and 3 <= j < 6:
                        boxes[2].append(board[i][j])
                    elif i < 3 and 6 <= j:
                        boxes[3].append(board[i][j])
                    elif 3 <= i < 6 and j < 3:
                        boxes[4].append(board[i][j])
                    
                    elif 3 <= i < 6 and j < 6:
                        boxes[5].append(board[i][j])
                    
                    elif 3 <= i < 6 and 6 <= j:
                        boxes[6].append(board[i][j])
                    
                    elif 6 <= i and j < 3:
                        boxes[7].append(board[i][j])
                    
                    elif 6 <= i and 3 <= j < 6:
                        boxes[8].append(board[i][j])
                    
                    elif 6 <= i  and 6 <= j:
                        boxes[9].append(board[i][j])
            
            if len(set(row)) != len(row):
                return False
        
        for val in boxes.values(): 
            if len(set(val)) != len(val):
                return False

        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != '.':
                    col.append(board[j][i])
            if len(set(col)) != len(col):
                return False
        print(boxes)

        return True
        