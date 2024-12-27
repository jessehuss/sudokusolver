def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using backtracking.
    :param board: 9x9 2D list representing the Sudoku board
    :return: True if the board is solvable, False otherwise
    """
    empty = find_empty_cell(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If it works, return success

            board[row][col] = 0  # Undo and backtrack

    return False  # No solution found


def find_empty_cell(board):
    """
    Finds an empty cell in the Sudoku board.
    :param board: 9x9 2D list
    :return: Tuple (row, col) of the empty cell, or None if no empty cell
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, num, pos):
    """
    Checks if placing a number in a given position is valid.
    :param board: 9x9 2D list
    :param num: Number to place (1-9)
    :param pos: Tuple (row, col) representing the position
    :return: True if valid, False otherwise
    """
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True


# Example usage:
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
