
# Sudoku Solver

Saw a reel where someone wrote a sudoku solver that brute forced the puzzle and wanted to write my own solvers using different techniques and algorithms.

| **Technique**                  | **Time Complexity**         | **Description**                                                                                 | **When to Use**                                                                                       |
|--------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Constraint Propagation**     | O(n * 27)                  | Reduces possibilities by enforcing Sudoku rules on rows, columns, and boxes incrementally.     | Effective for most human-solvable puzzles with logical patterns.                                    |
| **Naked/Hidden Pairs/Triples** | O(n^2)                     | Reduces candidates by identifying patterns of two or three cells sharing possibilities.        | For moderately difficult puzzles where logical deduction suffices without guessing.                 |
| **Pointing Pairs**             | O(n^2)                     | Eliminates candidates in rows/columns based on constraints confined to a box.                  | Effective for puzzles requiring advanced logic but no guessing.                                     |
| **Optimized Hybrid Solver**    | O(n^k) (k ≈ 2)             | Combines constraint propagation, advanced logical techniques, and minimal backtracking.        | Use for most scenarios; balances performance with versatility, especially for larger grids.          |
| **DLX (Dancing Links)**        | O(2^n) (worst-case)         | Transforms the Sudoku problem into an exact cover problem and solves it efficiently.           | Best for computationally solving very difficult or unsolvable puzzles.                              |
| **Backtracking with MRV**      | O(n^k)                     | Adds Minimum Remaining Values (MRV) heuristic to prioritize cells with fewer options.          | Suitable for simpler puzzles or as a fallback for advanced techniques.                              |
| **Naive Backtracking**         | O(9^n)                     | Tries every possible number for each empty cell recursively, with no optimization.             | Rarely practical. Use only as a simple example or for puzzles with very few empty cells.             |




