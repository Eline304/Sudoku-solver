from time import sleep

board = [
    [1, 4, 8, 0, 7, 0, 0, 0, 0],
    [9, 5, 7, 0, 2, 8, 0, 0, 0],
    [6, 3, 0, 5, 9, 1, 8, 4, 7],

    [0, 9, 5, 2, 3, 0, 0, 0, 1],
    [0, 0, 1, 0, 4, 6, 0, 5, 3],
    [0, 7, 0, 1, 0, 0, 0, 0, 0],

    [7, 2, 0, 8, 6, 9, 4, 0, 0],
    [0, 1, 9, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0]
] # This one should solve in a couple seconds (with sleep_time of 0.05)

unsolvable_board = [
    [2, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],

    [5, 0, 2, 6, 0, 0, 4, 0, 7],
    [0, 0, 0, 0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 9, 8, 0, 2, 3],

    [0, 0, 0, 0, 0, 3, 0, 8, 0],
    [0, 0, 5, 0, 1, 4, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0]
] # This one should take roughly 1 minute to detect it's not solvable (comment out the print and sleep statements)

test_board = [
    [0, 1, 4, 0, 7, 0, 8, 0, 0],
    [3, 5, 0, 2, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
    [1, 0, 9, 0, 0, 3, 0, 0, 7],

    [0, 4, 0, 3, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 3, 4, 0, 0, 0, 0, 0]
] # This one should take roughly 1 minute to detect it's not solvable (comment out the print and sleep statements)


empty_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 3, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
] # This is an empty board




sleep_time = 0.5

def print_board(board):
    "Pretty print a 9x9 sudoku board given as 2D array."
    for row_num, row in enumerate(board):
        if row_num % 3 == 0 and row_num != 0:
            print("-"*29)
        for col_num, col in enumerate(row):
            if col_num % 3 == 0 and col_num != 0:
                print("|", end="")
            print(f" {col} " if col else "   ", end="")
        print("")
    print("")


def is_row_valid(board, row, num):
    if num in board[row]:
        return False
    return True


def is_column_valid(board, column, num):
    for number in range(9):
        if board[number][column] == num:
            return False
    return True

def is_square_valid(board, row, column, number):
    squarex = row //3
    squarey = column //3

    for row in range(squarex*3, squarex*3+3):
        for column in range(squarey*3, squarey*3+3):
            if board[row][column] == number:
                return False
    return True

def is_valid(board, row, column, number):
    return is_row_valid(board, row, number) and is_column_valid(board, column, number) and is_square_valid(board, row, column, number)


def find_empty_square(board):
    for row_num, row in enumerate(board):
        for col_num, col in enumerate(row):
            if not col:
                return row_num, col_num

      
def solve(board : list[list[int]]):
    """Solve a 9x9 sudoku by filling in all empty (0) squares in the given 2D array.

    Return True when successful or False otherwise.
    """
    if not find_empty_square(board):
        return True
    
    empty_square = find_empty_square(board)

    for number in range(1, 10):
        if is_valid(board, empty_square[0], empty_square[1], number):
            board[empty_square[0]][empty_square[1]] = number
            print_board(board)
            sleep(0.05)
            if solve(board):
                return True
            board[empty_square[0]][empty_square[1]] = 0
    return False

if __name__ == "__main__":
    print_board(board)
    if solve(board):
        print("Solved!")
        print_board(board)
    else:
        print("No solution.")
