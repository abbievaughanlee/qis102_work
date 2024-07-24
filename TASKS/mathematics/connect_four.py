# connect_four.py
# simple connect 4 game


# note: there are 6 rows, 6 columns, and 6 diagonals with 4+ entries

# check all rows for any 4 in a row
def check_rows(player, board):
    # iterate through the rows
    for i in range(0, 6):
        # iterate through the columns of each row
        for j in range(0, 3):
            # check for any 4 consecutive positions equal to the player number
            if (
                board[i][j]
                == board[i][j + 1]
                == board[i][j + 2]
                == board[i][j + 3]
                == player
            ):
                print("row")
                return True
    return False


# check all columns for any 4 in a row
# same as check_rows but iterates through columns first then rows
def check_columns(player, board):
    for j in range(0, 6):
        for i in range(0, 3):
            if (
                board[i][j]
                == board[i + 1][j]
                == board[i + 2][j]
                == board[i + 3][j]
                == player
            ):
                print("column")
                return True
    return False


# check each diagonal that has 4 or more entries for 4 in a row
def check_diag_one(player, board):
    # only focus on diagonals that have at least 4 entries
    # iterate through first 3 rows
    for i in range(0, 3):
        # iterate through first 4 columns
        for j in range(0, 4):
            # check for 4 consecutive diagonal entries equal to the player number
            if (
                board[i][j]
                == board[i + 1][j + 1]
                == board[i + 2][j + 2]
                == board[i + 3][j + 3]
                == player
            ):
                print("diag one")
                return True
    return False


# check the opposite diagonals
def check_diag_two(player, board):
    # only focus on diagonals that have at least 4 entries
    # iterate through last 3 rows
    for i in range(5, 2, -1):
        # iterate through last 4 columns
        for j in range(0, 4):
            # check for 4 consecutive diagonal entries in the opposite direction equal to the player number
            if (
                board[i][j]
                == board[i - 1][j + 1]
                == board[i - 2][j + 2]
                == board[i - 3][j + 3]
                == player
            ):
                print("diag two")
                return True
    return False


def check_winner(player, board):
    if (
        check_rows(player, board)
        or check_columns(player, board)
        or check_diag_one(player, board)
        or check_diag_two(player, board)
    ):
        return True
    return False


def print_winner(board):
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


def main():
    # should return player 1: diagonal two
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    # should return player 2: row
    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]

    print_winner(board2)

    # should return no winner
    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)

    # added for further testing:

    # should return player 2: column
    board4 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 2, 1, 1, 2, 2, 0],
        [1, 2, 2, 1, 2, 2, 0],
        [1, 2, 2, 2, 1, 1, 0],
        [1, 2, 1, 2, 1, 2, 0],
    ]
    print_winner(board4)

    # should return player 2: diagonal one
    board5 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1, 0, 0],
        [0, 2, 2, 2, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board5)


main()
