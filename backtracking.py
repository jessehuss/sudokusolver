def solve_sudoku(board, visualizer=None):
    """
    Solves the Sudoku puzzle using backtracking.
    :param board: 9x9 2D list representing the Sudoku board
    :param visualizer: Optional visualizer instance
    :return: True if the board is solvable, False otherwise
    """
    empty = find_empty_cell(board)
    if not empty:
        return True
    
    row, col = empty
    
    # Show cell being considered
    if visualizer:
        if not visualizer.update(board, (row, col)):
            return False

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            # Show number placement
            if visualizer:
                if not visualizer.update(board, (row, col), num):
                    return False

            if solve_sudoku(board, visualizer):
                return True

            board[row][col] = 0
            # Show backtracking
            if visualizer:
                if not visualizer.update(board, (row, col)):
                    return False

    return False


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


