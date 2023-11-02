import sys

board = {
    "a": [ -1, -1, -1],
    "b": [ -1, -1, -1],
    "c": [ -1, -1, -1]
}

def validStartInput(input):
    try:
        if (input == "y" or input == "n"):
            return True
        else:
            print("Invalid Input")
            return False
    except:
        print("Invalid Input")
        return False
    
def validBoardInput(input):
    valid_letters = ["a", "b", "c"]
    valid_numbers = [1, 2, 3]
    try:
        if input[0] in valid_letters and int(input[1]) in valid_numbers:
            if board[input[0]][int(input[1]) - 1] < 0:   
                return True
            else:
                print("That Spot is Already Taken!")
                return False
        else:
            print("Invalid Coordinates")
            return False
    except:
        print("Invalid Coordinates")
        return False
    
def playGame():
    game_on = True
    won = False
    tie = False

    turn_num = 0
    while game_on:
        displayBoard()
        if turn_num % 2 == 0:
            val_in = input("Player 1 is X, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()
            while not validBoardInput(val_in):
                displayBoard()
                val_in = input("Player 1 is X, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()
        else:
            val_in = input("Player 2 is O, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()
            while not validBoardInput(val_in):
                displayBoard()
                val_in = input("Player 2 is O, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()

        board[val_in[0]][int(val_in[1]) - 1] = ((turn_num % 2) + 1) % 2
        ret = isOver()
        
        if ret == 1:
            tie = True
            game_on = False
        elif ret == 2:
            won = True
            game_on = False
        
        turn_num += 1

    displayBoard()
    if won:
        if turn_num % 2 == 0:
            print("Player 2 won!")
        else:
            print("Player 1 won!")
    elif tie:
        print("The game has ended in a tie!")

def isOver():
    # check for no space
    full = True
    for key in board:
        for val in board[key]:
            if val < 0:
                full = False

    # check for 3 in a row
    # first diagonals
    win = False
    if (board["a"][0] == board["b"][1] == board["c"][2] and board["a"][0] >= 0) or (board["a"][2] == board["b"][1] == board["c"][0] and board["a"][2] >= 0):
        win = True
    
    # now the rest
    for key in board:
        if board[key][0] == board[key][1] == board[key][2] and board[key][0] >= 0:
            win = True
        
    vals = [0, 1, 2]
    for num in vals:
        if board["a"][num] == board["b"][num] == board["c"][num] and board["a"][num] >= 0:
            win = True

    if win:
        return 2
    
    if full:
        return 1

    return 0

def getBoardVal(val):
    if val < 0:
        return "-"
    elif val == 0:
        return "O"
    elif val == 1:
        return "X"

def displayBoard():
    print("   a     b     c")
    print("      |     |")
    print("1  {}  |  {}  |  {}".format(getBoardVal(board["a"][0]), getBoardVal(board["b"][0]), getBoardVal(board["c"][0])))
    print(" _____|_____|_____")
    print("      |     |")
    print("2  {}  |  {}  |  {}".format(getBoardVal(board["a"][1]), getBoardVal(board["b"][1]), getBoardVal(board["c"][1])))
    print(" _____|_____|_____")
    print("      |     |")
    print("3  {}  |  {}  |  {}".format(getBoardVal(board["a"][2]), getBoardVal(board["b"][2]), getBoardVal(board["c"][2])))
    print("      |     |")

def leaveGame():
    print("Thanks for playing the game. See you next time ('-')7")
    sys.exit(0)

print("Welcome to Tic Tac Toe!")
print("This is a two player game so grab a friend.")
while True:
    val_input = input("Are you ready to play? [Y/N]: ").lower()
    while (not validStartInput(val_input)):
        val_input = input("Are you ready to play? [Y/N]: ").lower()

    if (val_input == "n"):
        leaveGame()
    elif (val_input == "y"):
        playGame()

        # reset board
        for col in board:
            nums = [0,1,2]
            for num in nums:
                board[col][num] = -1

    else:
        print("Something Very Bad Happened :(")
        sys.exit(-1)
