from heapq import heappush, heappop
from itertools import product

def solve_sudoku(board):
    """
    Optimized Sudoku solver using constraint propagation, logical deduction, and limited backtracking.
    """
    # Initialize possibilities and priority queue
    possibilities = initialize_possibilities(board)
    pq = initialize_priority_queue(possibilities, board)

    # Solve using advanced techniques
    if solve_with_techniques(board, possibilities, pq):
        return True

    # Fallback: Minimal backtracking for remaining unsolved cells
    return backtracking_solver(board, possibilities)


def initialize_possibilities(board):
    """
    Create a 9x9 grid of possibilities using bitmasking.
    """
    possibilities = [[0b111111111 for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                possibilities[row][col] = 0  # Cell is already solved
    update_all_possibilities(board, possibilities)
    return possibilities


def update_all_possibilities(board, possibilities):
    """
    Update possibilities for all cells on the board.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                update_possibilities(board, possibilities, row, col, board[row][col])


def update_possibilities(board, possibilities, row, col, num):
    """
    Remove 'num' as a possibility from the relevant row, column, and box.
    """
    mask = ~(1 << (num - 1))

    # Update row, column, and 3x3 subgrid
    for i in range(9):
        possibilities[row][i] &= mask
        possibilities[i][col] &= mask

    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            possibilities[i][j] &= mask


def initialize_priority_queue(possibilities, board):
    """
    Create a priority queue for cells based on the number of possibilities (MRV heuristic).
    """
    pq = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Only include unsolved cells
                heappush(pq, (bin(possibilities[row][col]).count('1'), (row, col)))
    return pq


def solve_with_techniques(board, possibilities, pq):
    """
    Apply logical techniques to solve the puzzle.
    """
    while pq:
        _, (row, col) = heappop(pq)

        if board[row][col] != 0:
            continue  # Skip solved cells

        # Single possibility
        if bin(possibilities[row][col]).count('1') == 1:
            num = possibilities[row][col].bit_length()
            board[row][col] = num
            update_possibilities(board, possibilities, row, col, num)
            pq = dynamic_priority_update(pq, possibilities, row, col)

        # Apply advanced logical techniques (Naked Pairs, Pointing Pairs)
        elif apply_logical_deductions(board, possibilities, pq):
            continue

        # If no progress, return False to trigger backtracking
        else:
            return False

    return is_solved(board)


def apply_logical_deductions(board, possibilities, pq):
    """
    Apply advanced logical techniques to reduce possibilities.
    """
    progress = False

    # Naked Pairs
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0 and bin(possibilities[row][col]).count('1') == 2:
                if eliminate_naked_pairs(board, possibilities, row, col):
                    progress = True

    # Pointing Pairs (eliminate candidates in row/column based on box constraints)
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            if eliminate_pointing_pairs(board, possibilities, box_row, box_col):
                progress = True

    return progress


def eliminate_naked_pairs(board, possibilities, row, col):
    """
    Eliminate possibilities using the Naked Pairs technique.
    """
    pair = possibilities[row][col]
    for i in range(9):
        if i != col and possibilities[row][i] == pair:
            # Eliminate the pair from other cells in the row
            mask = ~pair
            for j in range(9):
                if j != col and j != i:
                    possibilities[row][j] &= mask
            return True
    return False


def eliminate_pointing_pairs(board, possibilities, box_row, box_col):
    """
    Eliminate candidates in row/column based on box constraints (Pointing Pairs).
    """
    for num in range(1, 10):
        mask = 1 << (num - 1)
        cells = [(r, c) for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)
                 if possibilities[r][c] & mask]

        # If candidates are confined to one row/column within the box
        if len(cells) > 0:
            rows, cols = {r for r, _ in cells}, {c for _, c in cells}
            if len(rows) == 1:
                r = rows.pop()
                for c in range(9):
                    if c < box_col or c >= box_col + 3:
                        possibilities[r][c] &= ~mask
                return True
            if len(cols) == 1:
                c = cols.pop()
                for r in range(9):
                    if r < box_row or r >= box_row + 3:
                        possibilities[r][c] &= ~mask
                return True
    return False


def dynamic_priority_update(pq, possibilities, row, col):
    """
    Update the priority queue for cells affected by a new solution.
    """
    affected = [(row, i) for i in range(9)] + [(i, col) for i in range(9)]
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    affected += [(r, c) for r, c in product(range(box_row, box_row + 3), range(box_col, box_col + 3))]

    for r, c in affected:
        if possibilities[r][c] > 0:
            heappush(pq, (bin(possibilities[r][c]).count('1'), (r, c)))
    return pq


def backtracking_solver(board, possibilities):
    """
    Fallback to limited backtracking to resolve unsolved cells.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if possibilities[row][col] & (1 << (num - 1)):
                        board[row][col] = num
                        new_possibilities = [row[:] for row in possibilities]
                        update_possibilities(board, new_possibilities, row, col, num)
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def is_solved(board):
    """
    Check if the board is completely solved.
    """
    return all(all(cell != 0 for cell in row) for row in board)


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
