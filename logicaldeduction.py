def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using logical deduction only.
    :param board: 9x9 2D list representing the Sudoku board
    :return: True if solved, False if unsolvable
    """
    while True:
        # Apply constraints and try to reduce possibilities
        changed = False
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    possibilities = find_possibilities(board, row, col)
                    if len(possibilities) == 1:
                        # Naked single (only one possible number)
                        board[row][col] = possibilities.pop()
                        changed = True

        if is_solved(board):
            return True  # Solved
        if not changed:
            break  # No further progress can be made logically

    # If we reach here, the puzzle is unsolvable with pure logic
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


# Example usage
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
