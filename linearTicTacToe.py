from tkinter import *

BOARD_SIZE = 6

global playerMove
playerMove = 0

def generateEmptyBoard(length):
    global board
    board = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(-1)

        board.append(row)
    return board

board = generateEmptyBoard(BOARD_SIZE)

def checkWin():
    for i in range(BOARD_SIZE):
        if(checkRow(i)!=-1):
            return checkRow(i)
        elif(checkColumn(i)!=-1):
            return checkColumn(i)

    if(checkDiagonal1()!=-1):
        return checkDiagonal1()
    elif(checkDiagonal2()!=-1):
        return checkDiagonal2()

    return -1

def checkRow(row):
    global board
    for i in range(1, BOARD_SIZE):
        if(board[row][i - 1] != board[row][i]):
            
            return -1

    if(board[row][0] != -1):
        return board[row][0]
    else:
        return -1

def checkColumn(column):
    global board
    for i in range(1, BOARD_SIZE):
        if(board[i][column] != board[i - 1][column]):
            return -1

    if(board[0][column] != -1):
        print(board)
        return board[0][column]
    else:
        return -1

def checkDiagonal1():
    for i in range(1, BOARD_SIZE):
        if(board[i][i] != board[i - 1][i - 1]):
            return -1

    if(board[0][0] != -1):
        return board[0][0]
    else:
        return -1

def checkDiagonal2():
    for i in range(1, BOARD_SIZE):
        if(board[i][BOARD_SIZE - i - 1] != board[i - 1][BOARD_SIZE - i]):
            return -1

    if(board[0][BOARD_SIZE - 1] != -1):
        return board[0][BOARD_SIZE - 1]
    else:
        return -1

def playMove(buttons, row, column, playerMove):
    global gameWindow, boardCanvas
    buttons[row][column].place_forget()

    canvasLength = gameWindow.winfo_screenheight() // 4 * 3

    if(playerMove == 0):
        boardCanvas.create_oval(row * canvasLength//BOARD_SIZE + 5, \
                                column * canvasLength//BOARD_SIZE + 5, \
                                (row+1) * canvasLength//BOARD_SIZE - 5, \
                                (column+1) * canvasLength//BOARD_SIZE - 5)
    else:
        boardCanvas.create_line(row * canvasLength//BOARD_SIZE, \
                                column * canvasLength//BOARD_SIZE, \
                                (row+1) * canvasLength//BOARD_SIZE, \
                                (column+1) * canvasLength//BOARD_SIZE)
        boardCanvas.create_line((row+1) * canvasLength//BOARD_SIZE, \
                                column * canvasLength//BOARD_SIZE, \
                                row * canvasLength//BOARD_SIZE, \
                                (column+1) * canvasLength//BOARD_SIZE)
    
    boardCanvas.update()
    
    board[row][column] = playerMove
    switchPlayer()

    if(checkWin() != -1):
        winScreen(checkWin())
    #gameWindow.update()

def emptyCanvas():
    global boardCanvas
    boardCanvas.delete("all")

    global buttons
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            buttons[i][j].place_forget()

def generateCanvas():
    global boardCanvas, board

    canvasLength = gameWindow.winfo_screenheight() // 4 * 3

    for i in range(1, BOARD_SIZE):
        boardCanvas.create_line(i * canvasLength / BOARD_SIZE, 0, i * canvasLength / BOARD_SIZE, 2 * canvasLength)
        boardCanvas.create_line(0, i * canvasLength / BOARD_SIZE, 2 * canvasLength, i * canvasLength / BOARD_SIZE)
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if(board[i][j] == 1):
                boardCanvas.create_line(i * canvasLength//BOARD_SIZE, \
                    j * canvasLength//BOARD_SIZE, \
                    (i+1) * canvasLength//BOARD_SIZE, \
                    (j+1) * canvasLength//BOARD_SIZE)
                boardCanvas.create_line((i+1) * canvasLength//BOARD_SIZE, \
                    j * canvasLength//BOARD_SIZE, \
                    i * canvasLength//BOARD_SIZE, \
                    (j+1) * canvasLength//BOARD_SIZE)
            elif(board[i][j] == 0):
                boardCanvas.create_oval(i * canvasLength//BOARD_SIZE + 5, \
                    j * canvasLength//BOARD_SIZE + 5, \
                    (i+1) * canvasLength//BOARD_SIZE - 5, \
                    (j+1) * canvasLength//BOARD_SIZE - 5)
            else:
                buttons[i][j].place(x=i*canvasLength // BOARD_SIZE, y=j*canvasLength // BOARD_SIZE)
    boardCanvas.update()

def transpose(row, column):
    global board
    temp = board[row+1][column]
    board[row+1][column] = board[row][column+1]
    board[row][column+1] = temp
    switchPlayer()

    emptyCanvas()
    generateCanvas()

    global option
    option.destroy()

    if(checkWin()!=-1):
        winScreen(checkWin())

def option1():
    global gameWindow
    global option
    option = Toplevel(gameWindow)

    columnString = StringVar()
    columnLabel = Label(option, text = "Enter the column of the upper left element of your 2x2 matrix: ")
    columnTextBox = Entry(option, textvariable = columnString)

    columnLabel.grid(row = 0, column = 0)
    columnTextBox.grid(row = 0, column = 1)
    
    rowString = StringVar()
    rowLabel = Label(option, text = "Enter the row of the upper left element of your 2x2 matrix: ")
    rowTextBox = Entry(option, textvariable = rowString)

    rowLabel.grid(row = 1, column = 0)
    rowTextBox.grid(row = 1, column = 1)

    button = Button(option, text="Done", command=lambda: transpose(int(columnString.get()) - 1, int(rowString.get()) - 1))

    button.grid(row = 2, columnspan = 2)
    
    option.grab_set()
    option.mainloop()

def rowSwap(row, column):
    global board
    for i in range(2):
        temp = board[row+i][column]
        board[row + i][column] = board[row+i][column+1]
        board[row+i][column+1] = temp

    emptyCanvas()
    generateCanvas()

    global option
    option.destroy()

    if(checkWin()!=-1):
        winScreen(checkWin())

def option2():
    global gameWindow
    global option
    option = Toplevel(gameWindow)

    columnString = StringVar()
    columnLabel = Label(option, text = "Enter the column of the upper left element of your 2x2 matrix: ")
    columnTextBox = Entry(option, textvariable = columnString)

    columnLabel.grid(row = 0, column = 0)
    columnTextBox.grid(row = 0, column = 1)
    
    rowString = StringVar()
    rowLabel = Label(option, text = "Enter the row of the upper left element of your 2x2 matrix: ")
    rowTextBox = Entry(option, textvariable = rowString)

    rowLabel.grid(row = 1, column = 0)
    rowTextBox.grid(row = 1, column = 1)

    button = Button(option, text="Done", command=lambda: rowSwap(int(columnString.get()) - 1, int(rowString.get()) - 1))

    button.grid(row = 2, columnspan = 2)
    
    option.grab_set()
    option.mainloop()

def switchPlayer():
    global playerMove
    playerMove = (playerMove+1)%2

def startMenu():
    startWindow = Tk()

    twoPlayer(startWindow)

def singlePlayer():
    pass

def twoPlayer(startWindow):
    startWindow.destroy()
    global gameWindow
    gameWindow = Tk()
    gameWindow.resizable(width=False, height=False)

    pixelVirtual = PhotoImage(width=1, height=1)

    canvasLength = gameWindow.winfo_screenheight() // 4 * 3

    global boardCanvas
    boardCanvas = Canvas(gameWindow, \
                         height = canvasLength, \
                         width = canvasLength, \
                         borderwidth = 2, \
                         relief="solid")

    for i in range(1, BOARD_SIZE):
        boardCanvas.create_line(i * canvasLength / BOARD_SIZE, 0, i * canvasLength / BOARD_SIZE, 2 * canvasLength)
        boardCanvas.create_line(0, i * canvasLength / BOARD_SIZE, 2 * canvasLength, i * canvasLength / BOARD_SIZE)

    global buttons
    buttons = []
    
    for i in range(BOARD_SIZE):
        buttonRow = []
        for j in range(BOARD_SIZE):
            if(board[i][j] == -1):
                button = Button(boardCanvas, \
                                image = pixelVirtual, \
                                height = canvasLength // BOARD_SIZE, \
                                width = canvasLength // BOARD_SIZE, \
                                command=lambda i=i, j=j: playMove(buttons, i, j, playerMove))
                button.place(x=i*canvasLength // BOARD_SIZE, y=j*canvasLength // BOARD_SIZE)
                buttonRow.append(button)
            else:
                buttonRow.append(None)
        buttons.append(buttonRow)
    
    boardCanvas.grid(column = 1, row = 1, rowspan = 2, padx = (5, 5), pady = (5, 5))
    
    option1Button = Button(gameWindow, text="Transpose", command = option1)
    option1Button.grid(column = 2, row = 1)

    option2Button = Button(gameWindow, text="[a b; c d] -> [c d; a b]", command = option2)
    option2Button.grid(column = 2, row = 2)

    gameWindow.mainloop()

def winScreen(winner):
    win = Toplevel(gameWindow)

    canvasLength = gameWindow.winfo_screenheight() // 4 * 3

    label = Label(win, text="Winner")
    label.pack()
    
    winCanvas = Canvas(win, \
                         height = canvasLength//6, \
                         width = canvasLength//6, \
                         borderwidth = 2, \
                         relief="solid")

    if(winner == 1):
        winCanvas.create_line(0 * canvasLength//BOARD_SIZE, \
            0* canvasLength//BOARD_SIZE, \
            canvasLength//BOARD_SIZE, \
            canvasLength//BOARD_SIZE)
        winCanvas.create_line((0+1) * canvasLength//BOARD_SIZE, \
            0 * canvasLength//BOARD_SIZE, \
            0 * canvasLength//BOARD_SIZE, \
            (0+1) * canvasLength//BOARD_SIZE)
    else:
        winCanvas.create_oval(0 * canvasLength//BOARD_SIZE + 5, \
            0 * canvasLength//BOARD_SIZE + 5, \
            (0+1) * canvasLength//BOARD_SIZE - 5, \
            (0+1) * canvasLength//BOARD_SIZE - 5)

    winCanvas.pack()
    
    gameWindow.quit()

startMenu()


