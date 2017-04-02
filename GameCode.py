from random import randint

board = []

for x in range(5): #rad 5 & 6 skapar spelbrädet och storleken på spelbrädet, sparar detta i board-list.
    board.append(["O"] * 5)

def print_board(board): #denna kod rensar bort " " runt O:sen.
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print() #för att få en blanklinje
print_board(board)
print() #för att få en blanklinje

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(4):
    print()
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print() #för att få en blanklinje
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print() #för att få en blanklinje
            print("Oops, that's not even in the ocean.")
            if turn == 3:
                print() #för att få en blanklinje
                print("Game Over")
        elif(board[guess_row][guess_col] == "X"):
            print() #för att få en blanklinje
            print("You guessed that one already.")
            if turn == 3:
                print() #för att få en blanklinje
                print("Game Over")
        else:
            print() #för att få en blanklinje
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print() #för att få en blanklinje
                print("Game Over")

    print() #för att få en blanklinje
    print_board(board)

