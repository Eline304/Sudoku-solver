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


def solve(board : list[list[int]]):
    """Solve a 9x9 sudoku by filling in all empty (0) squares in the given 2D array.

    Return True when successful or False otherwise.
    """

    # TODO!

    # Hints:
    # - Pick an empty (0) square. In a loop try to put 1 through 9 in the square.
    #   Check if this doesn't violate any Sudoku-conditions. If not, recurse! If the
    #   recursive solve() was successful, we're done. If not, remove the number, and
    #   continue searching.
    # - For each step do this to understand what's going on:
    #     print_board(board)
    #     sleep(sleep_time)
    # - You will want to create a couple of helper function to keep your code understandable.
    
    return False # Not solvable



if __name__ == "__main__":
    print_board(board)
    if solve(board):
        print("Solved!")
    else:
        print("No solution.")
