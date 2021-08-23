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

def validTurnInput(input):
    try:
        int_in = int(input)
        if (int_in == 1 or int_in == 2):
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

def getBoardVal(val):
    if val < 0:
        return "-"
    elif val == 0:
        return "O"
    elif val == 1:
        return "X"

def playGame(turn):
    game_on = True
    won = False
    tie = False
    if (turn == 1):
        turn_num = 0
        while game_on:
            displayBoard()
            val_in = input("You are X's, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()
            while not validBoardInput(val_in):
                displayBoard()
                val_in = input("You are X's, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()

            board[val_in[0]][int(val_in[1]) - 1] = 1
            ret = isOver()
            if ret != 0:
                game_on = False
            else:
                makePlay(False, turn_num)
                ret = isOver()
                if ret != 0:
                    game_on = False
            
            if ret == 1:
                tie = True
            elif ret == 2:
                won = True
            
            turn_num += 1

    elif (turn == 2):
        turn_num = 0
        board["a"][0] = 0
        while game_on:
            displayBoard()
            val_in = input("You are X's, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()
            while not validBoardInput(val_in):
                displayBoard()
                val_in = input("You are X's, please enter where you'd like to play. Enter the coordinates (ex. a1 would be top left corner): ").lower()

            board[val_in[0]][int(val_in[1]) - 1] = 1
            ret = isOver()
            if ret != 0:
                game_on = False
            else:
                makePlay(True, turn_num)
                ret = isOver()
                if ret != 0:
                    game_on = False
            
            if ret == 1:
                tie = True
            elif ret == 2:
                won = True

            turn_num += 1

    displayBoard()
    if won:
        print("Uh-Oh, looks like you lost :(")
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

def makePlay(started, turn_num):
    if started and turn_num == 0:
        if board["c"][2] < 0:
            board["c"][2] = 0
        else:
            board["a"][2] = 0

        return

    if not started and turn_num == 0:
        if board["b"][1] < 0:
            board["b"][1] = 0
        else:
            board["a"][0] = 0

        return

    if not checkForTwo():
        if started:
            board["c"][0] = 0
            return
        else:
            if board["b"][1] == 1:
                if board["c"][0] < 0:
                    board["c"][0] = 0
                    return
            else:
                if board["b"][0] < 0:
                    board["b"][0] = 0
                    return
                elif board["a"][0] < 0:
                    board["a"][0] = 0
                    return
    
        for key in board:
            vals = [0,1,2]
            for val in vals:
                if board[key][val] < 0:
                    board[key][val] = 0
                    return

def checkForTwo():
    # diagonals
    num_twos = 0
    places = []
    XorO = []
    if board["a"][0] < 0 or board["a"][2] < 0 or board["c"][0] < 0 or board["c"][2] < 0 or board["b"][1] < 0:
        if board["a"][0] < 0 or board["c"][2] < 0 or board["b"][1] < 0:
            if board["a"][0] == board["c"][2] and board["a"][0] >= 0:
                num_twos += 1
                places.append("b1")
                XorO.append(board["a"][0])
            elif board["a"][0] == board["b"][1] and board["a"][0] >= 0:
                num_twos += 1
                places.append("c2")
                XorO.append(board["a"][0])
            elif board["b"][1] == board["c"][2] and board["b"][1] >= 0:
                num_twos += 1
                places.append("a0")
                XorO.append(board["b"][1])
        elif board["c"][0] < 0 or board["a"][2] < 0 or board["b"][1] < 0:
            if board["a"][2] == board["c"][0] and board["a"][2] >= 0:
                num_twos += 1
                places.append("b1")
                XorO.append(board["a"][2])
            elif board["a"][2] == board["b"][1] and board["a"][2] >= 0:
                num_twos += 1
                places.append("c0")
                XorO.append(board["a"][2])
            elif board["c"][0] == board["b"][1] and board["b"][1] >= 0:
                num_twos += 1
                places.append("a2")
                XorO.append(board["c"][0])

    # straights
    for key in board:
        if board[key][0] < 0 or board[key][1] < 0 or board[key][2] < 0:
            if board[key][0] == board[key][1] and board[key][0] >= 0:
                num_twos += 1
                places.append("{}2".format(key))
                XorO.append(board[key][0])
            if board[key][0] == board[key][2] and board[key][0] >= 0:
                num_twos += 1
                places.append("{}1".format(key))
                XorO.append(board[key][0])
            if board[key][1] == board[key][2] and board[key][1] >= 0:
                num_twos += 1
                places.append("{}0".format(key))
                XorO.append(board[key][1])
    
    vals = [0,1,2]
    for val in vals:
        if board["a"][val] < 0 or board["b"][val] < 0 or board["c"][val] < 0:
            if board["a"][val] == board["b"][val] and board["a"][val] >= 0:
                num_twos += 1
                places.append("c{}".format(val))
                XorO.append(board["a"][val])
            if board["a"][val] == board["c"][val] and board["a"][val] >= 0:
                num_twos += 1
                places.append("b{}".format(val))
                XorO.append(board["a"][val])
            if board["b"][val] == board["c"][val] and board["b"][val] >= 0:
                num_twos += 1
                places.append("a{}".format(val))
                XorO.append(board["b"][val])

    if num_twos > 1:
        indx = 0
        for item in XorO:
            if item == 0:
                board[places[indx][0]][int(places[indx][1])] = 0
                return True
            
            indx += 1
        
        board[places[0][0]][int(places[0][1])] = 0
        return True
    elif num_twos == 1:
        board[places[0][0]][int(places[0][1])] = 0
        return True
    else:
        return False

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

print("Welcome to Unwinnable Tic Tac Toe!")
while True:
    val_input = input("Would you like to try to win? [Y/N]: ").lower()
    while (not validStartInput(val_input)):
        val_input = input("Would you like to try to win? [Y/N]: ").lower()

    if (val_input == "n"):
        leaveGame()
    elif (val_input == "y"):
        val_input = input("Which turn would you like to go? [1/2]: ")
        while (not validTurnInput(val_input)):
            val_input = input("Which turn would you like to go? [1/2]: ")
            
        if (int(val_input) == 1):
            playGame(1)
        elif(int(val_input) == 2):
            started = True
            playGame(2)

        # reset board
        for col in board:
            nums = [0,1,2]
            for num in nums:
                board[col][num] = -1

    else:
        print("Something Very Bad Happened :(")
        sys.exit(-1)
