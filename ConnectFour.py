def startGame():
    global currentPlayer
    global gameOver
    global board

    board = []
    for i in range(6):
        board.append(['-']*7)

    currentPlayer = 0

    gameOver = False


def validMove(column):
    global currentPlayer, board, playerSelect
    # player selects a column not on the board
    if column < 0 or column > 5:
        print("Invalid column")
        return False
    
    # if the selected column is full
    if board[0][column] != "-":
        print("Column is full")
        return False
    
    return True


def setChip(column):
    global currentPlayer, board, playerSelect

    if validMove(column) == True:
        # check the lowest position
        for row in range(6):
            if board[5-row][column] == "-":
                board[5-row][column] = playerSelect[currentPlayer]
                currentPlayer = (currentPlayer + 1) % 2
                break

    
def checkWin():
    global gameOver
    # column
    for i in range(7):
        for j in range(3):
            if board[j][i] == board[j+1][i]  and board[j+1][i] == board[j+2][i] and board[j+2][i] == board[j+3][i] and board[j][i] == playerSelect[(currentPlayer+1)%2]:
                print("Game Over. Player " + str((currentPlayer-1) % 2 + 1) + " wins!!")
                gameOver = True
                return "nothing"

    # row
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2] and board[i][j+2] == board[i][j+3] and board[i][j] == playerSelect[(currentPlayer+1)%2]:
                print("Game Over. Player " + str((currentPlayer-1) % 2 + 1) + " wins!!")
                gameOver = True
                return "nothing"
    
    # downward diagonal
    for i in range(3):
        for j in range(4):
            if board[i+3][j] == board[i+2][j+1] and board[i+2][j+1] == board[i+1][j+2] and board[i+1][j+2] == board[i][j+3] and board[i][j+3] == playerSelect[(currentPlayer+1)%2]:
                print("Game Over. Player " + str((currentPlayer-1) % 2 + 1) + " wins!!")
                gameOver = True
                return "nothing"
    
    # upward diagonal
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i][j] == playerSelect[(currentPlayer+1)%2]:
                print("Game Over. Player " + str((currentPlayer-1) % 2 + 1) + " wins!!")
                gameOver = True
                return "nothing"

    
def main(): 
    global currentPlayer
    global board
    global playerSelect

    playerSelect = ["X", "O"]
    global gameOver
    # reset board and the current player
    startGame()

    while gameOver == False:
        column = int(input("Which column? "))
        setChip(column)
        for row in board:
            print(row)
        checkWin()



if __name__=="__main__": 
    main()