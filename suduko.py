def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def check_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve(board, row=0, col=0):
    if row == 9 - 1 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if board[row][col] > 0:
        return solve(board, row, col + 1)
    for num in range(1, 10):
        if check_valid(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col + 1):
                return True
        board[row][col] = 0
    return False

def main():
    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    if solve(board):
        print_board(board)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()