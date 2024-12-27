from heapq import heappush, heappop

def solve_sudoku(board):
    """
    Optimized Sudoku solver using bitmasking, advanced logical techniques, and heuristics.
    :param board: 9x9 2D list representing the Sudoku board
    :return: True if solved, False otherwise
    """
    # Initialize possibilities with bitmasking
    possibilities = initialize_possibilities(board)
    
    # Priority queue: Focus on cells with the fewest possibilities (MRV heuristic)
    pq = initialize_priority_queue(possibilities, board)

    while pq:
        _, (row, col) = heappop(pq)

        # Skip if already solved
        if board[row][col] != 0:
            continue

        # Get possibilities using bitmask
        options = possibilities[row][col]
        bit_count = bin(options).count("1")

        if bit_count == 1:
            # Only one possibility: solve it
            num = options.bit_length()
            board[row][col] = num
            update_possibilities(board, possibilities, row, col, num)
            pq = initialize_priority_queue(possibilities, board)
        else:
            return False  # No logical solution exists

    return is_solved(board)


def initialize_possibilities(board):
    """
    Initialize the possibilities for each cell using bitmasking.
    :param board: 9x9 2D list
    :return: 9x9 matrix of bitmask possibilities
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
    :param possibilities: 9x9 bitmask matrix of possibilities
    :param board: 9x9 2D list
    :return: Priority queue (list of tuples)
    """
    pq = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                bit_count = bin(possibilities[row][col]).count("1")
                if bit_count > 0:
                    heappush(pq, (bit_count, (row, col)))
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
