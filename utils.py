def is_safe(board, row, col):
    """
    بررسی می‌کند که آیا قرار دادن وزیر در خانه (row, col) امن است یا نه.
    """

    # بررسی ستون
    for i in range(row):
        if board[i] == col:
            return False

    # بررسی قطر چپ بالا
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def print_board(board):
    """
    چاپ صفحه شطرنج با چیدمان وزیرها
    """
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()