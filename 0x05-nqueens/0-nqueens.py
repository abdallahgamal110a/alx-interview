#!/usr/bin/env python3
import sys

def print_usage_and_exit(message):
    print(message)
    sys.exit(1)

def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    This function checks the left side of the row, the upper diagonal, 
    and the lower diagonal to ensure no queens attack each other.
    """
    for i in range(col):
        if board[row] == i or abs(board[row] - i) == abs(row - board.index(i)):
            return False
    return True

def solve_nqueens(N, board=[], col=0):
    """
    Solve the N queens problem using backtracking.
    This function attempts to place queens on the board and prints each valid configuration.
    """
    if col == N:
        print([[i, board[i]] for i in range(N)])
        return

    for row in range(N):
        board[col] = row
        if is_safe(board, row, col):
            solve_nqueens(N, board, col + 1)
        board[col] = -1

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    # Initialize the board with -1 (empty positions)
    board = [-1] * N
    solve_nqueens(N, board)

if __name__ == "__main__":
    main()
