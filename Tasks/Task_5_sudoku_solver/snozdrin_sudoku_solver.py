from typing import List, Tuple, Union


def print_board(board: List[List]) -> None:
    """Print Sudoku board.

    Args:
        board (List[List]): Board as 2-D array.
    """
    for row_idx in range(9):
        row = ""
        if row_idx in {3, 6}:
            print("-" * 21)

        for col_idx in range(9):
            if col_idx in {3, 6}:
                row += "| "

            row += f"{str(board[row_idx][col_idx])} "

        print(row)


def find_possition(board: List[List]) -> Union[Tuple, bool]:
    """Find empty possition.

    Args:
        board (List[List]): Board as 2-D array.

    Returns:
        Union[Tuple, bool]: Return tuple with empty cell coordinates or False.
    """
    for row_idx in range(9):
        for col_idx in range(9):
            if board[row_idx][col_idx] == 0:
                return row_idx, col_idx

    return False


def check_digit(board: List[List], row_idx: int, col_idx: int, digit: int) -> bool:
    """Check if digit is valid for given cell.

    Args:
        board (List[List]): Board as 2-D array.
        row_idx (int): Index of row.
        col_idx (int): Index of column.
        digit (int): Digit to check.

    Returns:
        bool: True -> Digit is valid to use in empty cell, False - > Digit is invalid for this cell.
    """
    if digit in board[row_idx]:
        return False

    if digit in (board[r_idx][col_idx] for r_idx in range(9)):
        return False

    row = row_idx // 3 * 3
    col = col_idx // 3 * 3
    if digit in (board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)):
        return False

    return True


def sudoku_solver(board: List[List]) -> bool:
    """Sudoku solver with backtracking algorithm.

    Args:
        board (List[List]): Board as 2-D array.

    Returns:
        bool: True -> algorithm found solution successfully, False -> will trigger backtrack.
    """
    possition = find_possition(board)
    if not possition:
        return True
    else:
        row, column = possition

    for digit in range(1, 10):
        if check_digit(board, row, column, digit):
            board[row][column] = digit

            if sudoku_solver(board):
                return True
            else:
                board[row][column] = 0

    return False


if __name__ == "__main__":
    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]

    print("\n", "Given Sudoku board".center(30, "-"), "\n")
    print_board(board)
    if sudoku_solver(board):
        print("\n", "Solved Sudoku board".center(30, "-"), "\n")
        print_board(board)
        print("\n")
