from heapq import heappush, heappop

def solve_sudoku(board):
    """
    Solves Sudoku using constraint propagation and priority-based cell selection.
    :param board: 9x9 2D list representing the Sudoku board
    :return: True if the board is solvable, False otherwise
    """
    possibilities = initialize_possibilities(board)
    pq = initialize_priority_queue(possibilities)

    while pq:
        _, (row, col) = heappop(pq)

        # Skip if already solved
        if board[row][col] != 0:
            continue

        # Get remaining possibilities for this cell
        options = possibilities[row][col]
        if len(options) == 1:
            num = options.pop()
            board[row][col] = num
            update_possibilities(board, possibilities, row, col, num)
            pq = initialize_priority_queue(possibilities)  # Rebuild queue
        else:
            return False  # No solution found logically

    return is_solved(board)


def initialize_possibilities(board):
    """
    Initialize the possibilities for each cell.
    :param board: 9x9 2D list
    :return: 9x9 list of sets representing possible values for each cell
    """
    possibilities = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                possibilities[row][col] = set()  # Already solved
    update_all_possibilities(board, possibilities)
    return possibilities


def update_all_possibilities(board, possibilities):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                update_possibilities(board, possibilities, row, col, board[row][col])


def update_possibilities(board, possibilities, row, col, num):
    """
    Remove `num` from the possibilities of affected cells.
    """
    # Remove from row and column
    for i in range(9):
        possibilities[row][i].discard(num)
        possibilities[i][col].discard(num)

    # Remove from 3x3 subgrid
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            possibilities[i][j].discard(num)


def initialize_priority_queue(possibilities):
    """
    Initialize a priority queue based on the number of possibilities per cell.
    :param possibilities: 9x9 list of sets representing possible values
    :return: Priority queue (list of tuples)
    """
    pq = []
    for row in range(9):
        for col in range(9):
            if possibilities[row][col]:
                heappush(pq, (len(possibilities[row][col]), (row, col)))
    return pq


def is_solved(board):
    """
    Checks if the Sudoku puzzle is completely solved.
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
