from random import randint

board = []

for x in range(5):  # Row 5 & 6 creates the board and the size of the board, then saves it to board-list.
    board.append(["O"] * 5)


def print_board(board):  # Removes " " at 0:s.
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print()  # Creates blank line
print_board(board)
print()  # Creates blank line


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print(ship_row)
# print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(4):
    print()
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print()  # Creates blank line
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print()
            print("Oops, that's not even in the ocean.")
            if turn == 3:
                print()  # fCreates blank line
                print("Game Over")
        elif board[guess_row][guess_col] == "X":
            print()  # Creates blank line
            print("You guessed that one already.")
            if turn == 3:
                print()  # Creates blank line
                print("Game Over")
        else:
            print()  # Creates blank line
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print()  # Creates blank line
                print("Game Over")

    print()  # Creates blank line
    print_board(board)
