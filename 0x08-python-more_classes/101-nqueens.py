#!/usr/bin/python3
"""
Function to solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
"""

import sys

def is_safe(board, row, col, N):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return (False)

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return (False)

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return (False)

    return (True)

def solve_nqueens_util(board, row, N, solutions):
    """
    Util function to solve N-Queens problem using backtracking.
    """
    if row == N:
        solutions.append([[i, j] for i, row in enumerate(board) for j, col in enumerate(row) if col == 1])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0  # Backtrack

def solve_nqueens(N):
    """
    Solve N-Queens problem and print the solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
