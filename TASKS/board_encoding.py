# board_encoding.py

# function to convert a base-10 number to base-3
def base_three(n):
    # array to hold the digits
    to_return = ""
    # base-10 to base-3 algorithm
    while n > 0:
        x = n // 3
        y = n % 3
        rem = str(y)
        to_return = to_return + rem
        n = x
    return to_return


# function to convert a base-3 number to a tic-tac-toe board
def main(x):
    # create a blank board
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    # convert the input to base three (string)
    three = base_three(x)
    # set initial row and column to the last element of the board
    row = 2
    col = 2
    # iterate through the base three string and set X's and O's accordingly
    for i in three:
        if i == "2":
            board[row][col] = "O"
        elif i == "1":
            board[row][col] = "X"
        # adjust rows and columns to move backwards through the board
        col = col - 1
        if col == -1:
            col = 2
            row = row - 1
    print(*board, sep="\n")
    print(f"This is the board for {x} decoded")


# check the boards as assigned
main(2271)
main(1638)
main(12065)
