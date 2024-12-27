# Sudoku Solver

Saw a reel where someone wrote a sudoku solver that brute forced the puzzle and wanted to write my own solvers using different techniques and algorithms.

## Requirements

- Python 3.10+
- pip install -r requirements.txt


## Usage

Run the solver.py file to see the different solvers and their time complexities with a visualizer.

__Example__

<code>solver.py</code>

__Output__

Available Solvers:
1. Constraint Propagation - O(n * 27)
2. Advanced - O(n log n)
3. Optimized - O(n log n)
4. Logical Deduction - O(n^k)
5. Optimized ONK - O(n^k)
6. Backtracking - O(9^n)

Choose a solver (1-6):

Use visualization? (y/n):


## Solvers

| **Technique**                  | **Time Complexity**         | **Description**                                                                                 | **When to Use**                                                                                       |
|--------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Constraint Propagation**     | O(n * 27)                  | Solves Sudoku using constraint propagation and priority-based cell selection.     | Effective for most human-solvable puzzles with logical patterns.                                    |
| **Advanced Solver**           | O(n log n)     | Enhanced Sudoku solver with advanced logical techniques, dynamic updates, and limited backtracking.       | Use for most scenarios; balances performance with versatility, especially for larger grids.          |
| **Optimized Solver**           | O(n log n)     | Optimized Sudoku solver using bitmasking, advanced logical techniques, and heuristics.       | Use for most scenarios; balances performance with versatility, especially for larger grids.          |
| **Logical Deduction**         | O(n<sup>k</sup>) (k ≈ 2)             | Solves the Sudoku puzzle using logical deduction only.                              | Suitable for puzzles that can be solved with logical deduction alone.                              |
| **Optimized O(n<sup>k</sup>)**           | O(n<sup>k</sup>)     | Optimized Sudoku solver using constraint propagation, logical deduction, and limited backtracking.       | This implementation ensures 𝑘 is minimized through logical techniques and efficient constraint propagation, making it competitive for practical puzzles.          |
| **Backtracking**         | O(9<sup>n</sup>)                     | Solves the Sudoku puzzle using backtracking.             | Rarely practical. Use only as a simple example or for puzzles with very few empty cells.             |




