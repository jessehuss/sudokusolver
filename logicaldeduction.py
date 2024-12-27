def solve_sudoku(board, visualizer=None):
    """
    Solves the Sudoku puzzle using logical deduction only.
    :param board: 9x9 2D list representing the Sudoku board
    :param visualizer: Optional SudokuVisualizer instance
    :return: True if solved, False if unsolvable
    """
    while True:
        changed = False
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    # Update visualizer to show cell being checked
                    if visualizer:
                        if not visualizer.update(board, (row, col)):
                            return False

                    possibilities = find_possibilities(board, row, col)
                    if len(possibilities) == 1:
                        value = possibilities.pop()
                        board[row][col] = value
                        changed = True
                        
                        # Update visualizer to show number placement
                        if visualizer:
                            if not visualizer.update(board, (row, col), value):
                                return False

        if is_solved(board):
            # Show final state
            if visualizer:
                visualizer.update(board)
            return True
        if not changed:
            break

    return False


def find_possibilities(board, row, col):
    """
    Finds possible numbers for a cell based on Sudoku rules.
    :param board: 9x9 2D list
    :param row: Row index of the cell
    :param col: Column index of the cell
    :return: Set of possible numbers for the cell
    """
    if board[row][col] != 0:
        return set()  # Cell already filled

    possibilities = set(range(1, 10))

    # Remove numbers already in the row
    possibilities -= set(board[row])

    # Remove numbers already in the column
    possibilities -= {board[i][col] for i in range(9)}

    # Remove numbers already in the 3x3 subgrid
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            possibilities.discard(board[i][j])

    return possibilities


def is_solved(board):
    """
    Checks if the Sudoku puzzle is completely solved.
    :param board: 9x9 2D list
    :return: True if solved, False otherwise
    """
    for row in board:
        if any(cell == 0 for cell in row):
            return False
    return True

