def setup():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, removeSquare, startSquareX, startSquareY, numSquares
    global Cross, Circle, squareList, player1, playCounter, playerWin, row, col, gameDone, backGround

    allBoundaries = []
    startSquareX = 200
    startSquareY = 200
    squareXShow = startSquareX
    squareYShow = startSquareY
    squareHeight = 200
    squareWidth = 200
    numSquares = 9
    removeSquare = True
    whichSquare = -1
    size(1000, 1000)
    backGround = loadImage("background.jpg")
    Cross = loadImage("Cross.png")
    Circle = loadImage("Circle.png")
    player1 = True
    squareList = [ [" ", " " , " "] for i in range( 3 ) ] 
    playCounter = 0
    playerWin = False
    row = 3
    col = 3
    gameDone = False
    
    image(backGround,0,0,1000,1000)

    for i in range( row ):
        for j in range( col ):
            upperLeft =  [ squareXShow, squareYShow ]
            lowerRight = [ squareXShow + squareWidth, squareYShow + squareHeight ]
            clickBoundary = [ upperLeft, lowerRight ]
            allBoundaries.append( clickBoundary )
            squareXShow = squareXShow + squareWidth
        squareXShow = startSquareX
        squareYShow = squareYShow + squareHeight

    
    activeSquares = [ True for j in range( numSquares ) ]
    
    squareXShow = startSquareX
    squareYShow = startSquareY
    
    for i in range( row ):
        squareXShow = startSquareX
        for j in range( col ):
            fill ( 255 )
            rect( squareXShow, squareYShow, squareWidth, squareHeight )
            squareXShow = squareXShow + squareWidth
        squareYShow = squareYShow + squareHeight
        
        
#Restart the game when it's over    
def keyPressed():
    global gameDone,playCounter,playerWin
    
    if checkWin() or (playCounter == 9 and playerWin != True):
        if keyCode == 32:
            gameDone == False
            setup()

                
def mouseReleased():
    global allBoundaries, whichSquare, removeSquare, activeSquares, numSquares, validLocation

    whichSquare = - 1
    validLocation = False
    for i in range( numSquares ):        
        if activeSquares[ i ]:
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                whichSquare = i
                break
    if validLocation and removeSquare:
        activeSquares[ whichSquare ] = False

#Check the win conditions and declare a winner
def checkWin():
    global playerWin
    for i in range( 3 ):
        if squareList[i][0] == squareList[i][1] == squareList[i][2] and (squareList[i][0] != " "):
            playerWin = True
        if playerWin == True:
            return(playerWin)
            break
        else:
            for j in range( 3 ):
                if squareList[0][j] == squareList[1][j] == squareList[2][j] and (squareList[0][j] != " "):
                    playerWin = True
                if playerWin == True:
                    return(playerWin)
                    break
                else:
                    if squareList[0][0] == squareList[1][1] == squareList[2][2] and (squareList[0][0] != " "):
                        playerWin = True
                        return (playerWin)
                
                    if squareList[0][2] == squareList[1][1] == squareList[2][0] and (squareList[0][2] != " "):
                        playerWin = True
                        return (playerWin)

    
def draw():
    global allBoundaries, squareXShow, squareYShow, squareHeight, squareWidth, activeSquares, whichSquare, numSquares, squareChosen, removeSquare, startFill, startSquareX, startSquareY
    global Cross, Circle, player1, squareList, playCounter, playerWin, gameDone, backGround
    
    if whichSquare > -1:
        if player1:
            image (Cross ,startSquareX + (squareWidth * (whichSquare % 3)) , startSquareY + (squareHeight * (whichSquare//3)) , squareWidth , squareHeight)
            squareList[whichSquare % row][whichSquare // col] = "1"
            player1 = not player1
        else:
            image (Circle ,startSquareX + (squareWidth * (whichSquare % 3)) , startSquareY + (squareHeight * (whichSquare//3)) , squareWidth, squareHeight)
            squareList[whichSquare % row][whichSquare // col]  = "2" 
            player1 = not player1    

        playCounter += 1
        whichSquare = -1
        
        if playCounter >= 5:
            checkWin()
            if player1 and playerWin != False:
                gameDone = True
                if gameDone:
                    fill(123)
                    rect(400,100,200,80)
                    textSize(20)
                    fill(0)
                    text("Player 2 wins",433,150)
                    fill(123)
                    rect(270,850,480,80)
                    textSize(30)
                    fill(0)
                    text("Press spacebar to play again!", 300,900)
                    for i in range(numSquares):
                        activeSquares[i] = False
                    
            elif player1 == False and playerWin != False:
                gameDone = True
                if gameDone:
                    fill(123)
                    rect(400,100,200,80)
                    textSize(20)
                    fill(0)
                    text("Player 1 wins",430,150)
                    fill(123)
                    rect(270,850,480,80)
                    textSize(30)
                    fill(0)
                    text("Press spacebar to play again!", 300,900)
                    for i in range(numSquares):
                        activeSquares[i] = False
                    
        if playCounter == 9 and playerWin != True:
            gameDone = True
            if gameDone:
                fill(123)
                rect(400,100,200,80)
                textSize(20)
                fill(0)
                text("Tie",480,150)
                fill(123)
                rect(270,850,480,80)
                textSize(30)
                fill(0)
                text("Press spacebar to play again!", 300,900)
                for i in range(numSquares):
                    activeSquares[i] = False
    
    #Declare the winner
    if player1:
        fill(123)
        rect(400, 0, 200, 50)
        textSize(20)
        fill(0)
        text("Player 1's Turn", 430, 30)
    else:
        fill(123)
        rect(400, 0, 200, 50)
        textSize(20)
        fill(0)
        text("Player 2's Turn", 430, 30)
