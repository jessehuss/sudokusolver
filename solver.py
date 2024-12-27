from visualizer import SudokuVisualizer
from backtracking import solve_sudoku as backtracking_solve
from advancedsolver import solve_sudoku as advanced_solve
from optimizedsolver import solve_sudoku as optimized_solve
from optimizedonk import solve_sudoku as optimized_onk_solve
from logicaldeduction import solve_sudoku as logical_solve
from constraintpropagation import solve_sudoku as constraint_solve

def main():
    # Example Sudoku board
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

    # Available solvers
    solvers = {
        '1': ('Constraint Propagation - O(n * 27)', constraint_solve),
        '2': ('Advanced - O(n log n)', advanced_solve),
        '3': ('Optimized - O(n log n)', optimized_solve),
        '4': ('Logical Deduction - O(n^k)', logical_solve),
        '5': ('Optimized ONK - O(n^k)', optimized_onk_solve),
        '6': ('Backtracking - O(9^n)', backtracking_solve)
    }

    # Print solver options
    print("\nAvailable Solvers:")
    for key, (name, _) in solvers.items():
        print(f"{key}. {name}")

    # Get user choice for solver
    solver_choice = input("\nChoose a solver (1-6): ")
    while solver_choice not in solvers:
        solver_choice = input("Invalid choice. Please choose 1-6: ")

    # Get visualization preference
    vis_choice = input("Use visualization? (y/n): ").lower()
    while vis_choice not in ['y', 'n']:
        vis_choice = input("Invalid choice. Use visualization? (y/n): ").lower()

    # Create a copy of the board
    board = [row[:] for row in sudoku_board]
    
    # Setup visualizer if requested
    visualizer = SudokuVisualizer() if vis_choice == 'y' else None

    # Solve the puzzle
    solver_name, solver_func = solvers[solver_choice]
    print(f"\nSolving with {solver_name} solver...")
    
    if solve_with_solver(solver_func, board, visualizer):
        print("\nSolution found!")
        print_board(board)
    else:
        print("\nNo solution exists.")

def print_board(board):
    """Print the Sudoku board in a readable format"""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num, end=" ")
        print()

def solve_with_solver(solver_func, board, visualizer=None):
    """Wrapper to handle different solver function signatures"""
    try:
        return solver_func(board, visualizer)
    except TypeError:
        # If solver doesn't accept visualizer parameter, call without it
        return solver_func(board)

if __name__ == "__main__":
    main() 