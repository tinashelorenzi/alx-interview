import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same row to the left
    for i in range(col):
        if board[i] == row or \
           board[i] == row - (col - i) or \
           board[i] == row + (col - i):
            return False

    return True


def solve_nqueens_util(board, col, N):
    if col == N:
        # All queens are placed, print the solution
        print([[i, board[i]] for i in range(N)])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[col] = i
            solve_nqueens_util(board, col + 1, N)


def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens_util([0] * N, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
