import pygame, sys, random, math, random, smtplib, numpy

recipient = raw_input("Your E-Mail Address please !!    ")
ROWS = int(raw_input("Number of Rows in game      "))
COLS = int(raw_input("Number of Cols in game      "))
SCORE = 0
grid = numpy.zeros((ROWS,COLS))
#print grid
gridWidth = 50
gridHeight = 50
MARGIN = 20
windowHeight = (MARGIN + gridHeight) * ROWS + MARGIN
windowWidht = (MARGIN + gridWidth) * COLS + MARGIN
gameExit = False
#initializing colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#initializing grid
initialRow = random.sample(xrange(0,ROWS), 2) #two diff rand number between (0, rows)
intitialCol = random.sample(xrange(0,COLS), 2)
grid[initialRow[0], intitialCol[0]] = 2
grid[initialRow[1], intitialCol[1]] = 2

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
gameDisplay = pygame.display.set_mode((windowWidht, windowHeight)) 
pygame.display.set_caption('2048') #name of window
pygame.display.update()	

def randomNumber():
	emptyRowList = []
	emptyColList = []
	for varow in range(ROWS):
		for vacol in range(COLS):
			if grid[varow, vacol] == 0:
				emptyRowList.append(varow)
				emptyColList.append(vacol)
	lenRowList = len(emptyRowList)
	lenColList = len(emptyColList)
	if lenColList > 0 and lenRowList > 0:
		randRow = random.randint(0, lenRowList-1)
		randCol = random.randint(0, lenColList-1)
		twoOrFour = random.randint(0, 3)
		if twoOrFour == 0:
			grid[emptyRowList[randRow], emptyColList[randCol]] = 4
		else:
			grid[emptyRowList[randRow], emptyColList[randCol]] = 2
def upgradeGrid(com):
	global SCORE
	movement = False
	if com == "left":
		for row in range(ROWS):
			for col in range(COLS):
				tempCol = col
				tempColVal = grid[row][tempCol]
				if tempColVal > 0:
					grid[row][tempCol] = 0
					while tempCol > 0 and grid[row][tempCol-1] == 0:
						tempCol -= 1
						movement = True
					grid[row][tempCol] = tempColVal 
				#print row, col, grid[row][col]
			for col in range(COLS):	
				if col > 0 and grid[row][col-1] == grid[row][col] and grid[row][col] > 0:
					grid[row][col-1] *= 2
					SCORE += grid[row][col-1]
 					grid[row][col] = 0
					movement = True
			for col in range(COLS):	
				tempCol = col
				tempColVal = grid[row][tempCol]
				if tempColVal > 0:
					grid[row][tempCol] = 0
					while tempCol > 0 and grid[row][tempCol-1] == 0:
						tempCol -= 1
						movement = True
					grid[row][tempCol] = tempColVal
	elif com == "up":
		for col in range(COLS):
			for row in range(ROWS):
				tempRow = row
				tempRowVal = grid[tempRow][col]
				if tempRowVal > 0:
					grid[tempRow][col] = 0
					while tempRow > 0 and grid[tempRow-1][col] == 0:
						tempRow -= 1
						movement = True
					grid[tempRow][col] = tempRowVal 
				#print row, col, grid[row][col]
			for row in range(ROWS):	
				if row > 0 and grid[row-1][col] == grid[row][col] and grid[row][col]>0:
					grid[row-1][col] *= 2
					SCORE += grid[row-1][col]
					grid[row][col] = 0
					movement = True
			for row in range(ROWS):	
				tempRow = row
				tempRowVal = grid[tempRow][col]
				if tempRowVal > 0:
					grid[tempRow][col] = 0
					while tempRow > 0 and grid[tempRow-1][col] == 0:
						tempRow -= 1
						movement = True
					grid[tempRow][col] = tempRowVal
	elif com == "right":
		for row in range(ROWS):
			for col in range(COLS):
				col = (COLS-1) - col
				tempCol = col
				tempColVal = grid[row][tempCol]
				if tempColVal > 0:
					grid[row][tempCol] = 0
					while tempCol < COLS-1 and grid[row][tempCol+1] == 0:
						tempCol += 1
						movement = True
					grid[row][tempCol] = tempColVal 
				#print row, col, grid[row][col]
			for col in range(COLS):
				col = (COLS -1) - col
				if col < COLS-1 and grid[row][col+1] == grid[row][col] and grid[row][col] > 0:
					grid[row][col+1] *= 2
					SCORE += grid[row][col+1]
					grid[row][col] = 0
					movement = True
			for col in range(COLS):
				col = (COLS -1) - col
				tempCol = col
				tempColVal = grid[row][tempCol]
				if tempColVal > 0:
					grid[row][tempCol] = 0
					while tempCol < COLS-1 and grid[row][tempCol+1] == 0:
						tempCol += 1
						movement = True
					grid[row][tempCol] = tempColVal
	elif com == "down":
		for col in range(COLS):
			for row in range(ROWS):
				row = (ROWS-1) - row
				tempRow = row
				tempRowVal = grid[tempRow][col]
				if tempRowVal > 0:
					grid[tempRow][col] = 0
					while tempRow < ROWS-1 and grid[tempRow+1][col] == 0:
						tempRow += 1
						movement = True
					grid[tempRow][col] = tempRowVal 
				#print row, col, grid[row][col]
			for row in range(ROWS):
				row = (ROWS -1) - row
				if row < ROWS-1 and grid[row+1][col] == grid[row][col] and grid[row][col] > 0:
					grid[row+1][col] *= 2
					SCORE += grid[row+1][col]
					grid[row][col] = 0
					movement = True
			for row in range(ROWS):
				row = (ROWS -1) - row
				tempRow = row
				tempRowVal = grid[tempRow][col]
				if tempRowVal > 0:
					grid[tempRow][col] = 0
					while tempRow < ROWS-1 and grid[tempRow+1][col] == 0:
						tempRow += 1
						movement = True
					grid[tempRow][col] = tempRowVal
	print SCORE
	#print movement
	if(movement == True):
	 	randomNumber()
def drawGrid(): 
	for row in range(ROWS):
		for column in range(COLS):
			color = WHITE
			pygame.draw.rect(gameDisplay,
							color,
                            [(MARGIN + gridWidth) * column + MARGIN,
                            (MARGIN + gridHeight) * row + MARGIN,
                            gridWidth,
                            gridHeight])
			if grid[row, column] == 0:
				num = ""
			else:
				num = str(int(grid[row, column]))
			text = font.render(num, 1, BLACK)
			numlen = len(num)
			font.set_bold(True)
			textpos = ((MARGIN + gridWidth ) * column + MARGIN + (4-numlen)*4), ((MARGIN + gridHeight) * row + 2*MARGIN-4)
			gameDisplay.blit(text, textpos)
def gamexit():
	emptyRowList = []
	emptyColList = []
	for varow in range(ROWS):
		for vacol in range(COLS):
			if grid[varow, vacol] == 0:
				emptyRowList.append(varow)
				emptyColList.append(vacol)
	lenRowList = len(emptyRowList)
	lenColList = len(emptyColList)
	for col in range(COLS):
		for row in range(ROWS):
			if row < ROWS-1 :
				if grid[row, col] == grid[row+1, col] :		
					return False
	for row in range(ROWS):
		for col in range(COLS):
			if col < COLS-1:
				if grid[row, col] == grid[row, col+1] :		
					return False
	if lenColList > 0 and lenRowList > 0:
		return False
	return True
def sendMail():
	body_of_email = ""
	GMAIL_USERNAME = "ug201311036@iitj.ac.in"
	GMAIL_PASSWORD = "chutiyaujjwal"   
	email_subject = "SCORE 2048 = " + str(int(SCORE))

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
	body_of_email = ""
	for i in range(ROWS):
		for j in range(COLS):
	 		body_of_email = body_of_email + str(int(grid[i,j])) + "    \t\r\t\r\t"
	 	body_of_email = body_of_email  + " <br>  "
	# 	body_of_email = body_of_email + (str(grid[i:])) + " " + " <PRE> " " <br> + " "  </PRE> " +  (str(grid[i+1:]))
	headers = "\r\n".join(["from: " + GMAIL_USERNAME,
	                       "subject: " + email_subject,
	                       "to: " + recipient,
	                       "mime-version: 1.0",
	                       "content-type: text/html"])

	content = headers + "\r\n\r\n" + body_of_email
	session.sendmail(GMAIL_USERNAME, recipient, content)
while not gameExit:
	#Drawing Grids
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				upgradeGrid("up")
			elif event.key == pygame.K_DOWN:
				upgradeGrid("down")
			elif event.key == pygame.K_LEFT:
				upgradeGrid("left")
			elif event.key == pygame.K_RIGHT:
				upgradeGrid("right")
		if gamexit()== True :
			gameExit = True
	gameDisplay.fill(BLACK)
	drawGrid()
	pygame.display.update()	
	clock.tick(60)
print grid
sendMail()
print ("GAME OVER")
#sendMail()
pygame.quit()
sys.exit(0)
quit()