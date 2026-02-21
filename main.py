print("Hfrom utils import is_safe, print_board")

N = 8  # تعداد وزیرها

def solve_queens(board, row):
    
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            if solve_queens(board, row + 1):
                return True

            board[row] = -1  # Backtrack

    return False


def main():
    board = [-1] * N

    if solve_queens(board, 0):
        print("A valid solution was found:\n")
        print_board(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()