from heapq import heappush, heappop
from itertools import product
from visualizer import SudokuVisualizer

def solve_sudoku(board, visualizer=None):
    """
    Enhanced Sudoku solver with Pygame visualization.
    :param board: 9x9 2D list representing the Sudoku board
    :param visualizer: SudokuVisualizer instance
    :return: True if solved, False otherwise
    """
    # Initialize possibilities with bitmasking
    possibilities = initialize_possibilities(board)
    pq = initialize_priority_queue(possibilities, board)
    
    # Show initial board state
    if visualizer:
        if not visualizer.update(board):
            return False

    while pq:
        _, (row, col) = heappop(pq)

        if board[row][col] != 0:
            continue

        options = possibilities[row][col]
        bit_count = bin(options).count("1")

        if bit_count == 1:
            num = options.bit_length()
            # Show cell being considered
            if visualizer:
                if not visualizer.update(board, (row, col)):
                    return False
                
            board[row][col] = num
            update_possibilities(board, possibilities, row, col, num)
            pq = dynamic_priority_update(pq, possibilities, row, col)
            
            # Show number placement
            if visualizer:
                if not visualizer.update(board, (row, col), num):
                    return False
        elif bit_count == 0:
            return False
        else:
            if not logical_deduction(board, possibilities, pq):
                return backtracking_solver(board, possibilities, visualizer)

    return is_solved(board)


def initialize_possibilities(board):
    """
    Initialize the possibilities for each cell using bitmasking.
    """
    possibilities = [[0b111111111 for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                possibilities[row][col] = 0  # Cell already solved
    update_all_possibilities(board, possibilities)
    return possibilities


def update_all_possibilities(board, possibilities):
    """
    Update all possibilities for the board.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                update_possibilities(board, possibilities, row, col, board[row][col])


def update_possibilities(board, possibilities, row, col, num):
    """
    Propagate constraints by removing the solved number from possibilities.
    """
    mask = ~(1 << (num - 1))  # Create a bitmask for elimination

    # Update row and column
    for i in range(9):
        possibilities[row][i] &= mask
        possibilities[i][col] &= mask

    # Update 3x3 subgrid
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            possibilities[i][j] &= mask


def initialize_priority_queue(possibilities, board):
    """
    Initialize the priority queue with the MRV heuristic.
    """
    pq = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                bit_count = bin(possibilities[row][col]).count("1")
                if bit_count > 0:
                    heappush(pq, (bit_count, (row, col)))
    return pq


def dynamic_priority_update(pq, possibilities, row, col):
    """
    Dynamically update the priority queue for affected cells.
    """
    affected_cells = [(row, i) for i in range(9)] + [(i, col) for i in range(9)]
    box_x, box_y = col // 3, row // 3
    affected_cells += [
        (i, j)
        for i, j in product(range(box_y * 3, box_y * 3 + 3), range(box_x * 3, box_x * 3 + 3))
    ]

    for r, c in affected_cells:
        if possibilities[r][c] > 0:
            bit_count = bin(possibilities[r][c]).count("1")
            heappush(pq, (bit_count, (r, c)))

    return pq


def logical_deduction(board, possibilities, pq):
    """
    Apply advanced logical techniques like Naked Pairs or Pointing Pairs.
    """
    # Implementing Naked Pairs as an example
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0 and bin(possibilities[row][col]).count("1") == 2:
                # Look for another cell in the same row/column/box with the same possibilities
                if find_naked_pairs(board, possibilities, row, col):
                    return True
    return False


def find_naked_pairs(board, possibilities, row, col):
    """
    Identify and handle Naked Pairs in the same unit.
    """
    pair = possibilities[row][col]
    # Check row
    for i in range(9):
        if i != col and possibilities[row][i] == pair:
            eliminate_from_row(possibilities, row, pair)
            return True
    # Check column
    for i in range(9):
        if i != row and possibilities[i][col] == pair:
            eliminate_from_column(possibilities, col, pair)
            return True
    return False


def backtracking_solver(board, possibilities, visualizer=None):
    """
    Fallback to backtracking with visualization support.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if possibilities[row][col] & (1 << (num - 1)):
                        # Show cell being considered
                        if visualizer:
                            if not visualizer.update(board, (row, col)):
                                return False
                        
                        board[row][col] = num
                        new_possibilities = [row[:] for row in possibilities]
                        update_possibilities(board, new_possibilities, row, col, num)
                        
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
    return True


def is_solved(board):
    """
    Checks if the Sudoku puzzle is completely solved.
    """
    for row in board:
        if any(cell == 0 for cell in row):
            return False
    return True

