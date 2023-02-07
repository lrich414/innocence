import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((0,0,120))
pygame.display.set_caption('Tic Tac Toe')
running = True
boxSize = 100
margin = 50
turn = "X"
winner = None
def changeTurn(turn):
  return "X" if turn == "O" else "O"
board = [[None, None, None],[None, None, None],[None, None, None]]
def drawBoard(boxSize):
  pygame.draw.line(screen, (255, 255, 255), (50,150), (350,150), 5)
  pygame.draw.line(screen, (255, 255, 255), (50,250), (350,250), 5)
  pygame.draw.line(screen, (255, 255, 255), (150,50), (150,350), 5)
  pygame.draw.line(screen, (255, 255, 255), (250,50), (250,350), 5)
def boxClicked(box,board,winner):
  fontObj = pygame.font.SysFont('tahoma', 96)
  fontSurfaceObj = fontObj.render(turn,  True, (255, 0, 0), (0, 0, 120))
  screen.blit(fontSurfaceObj, (box.topleft))
  if box == BOX1:
    board[0][0] = turn
  if box == BOX2:
    board[0][1] = turn
  if box == BOX3:
    board[0][2] = turn
  if box == BOX4:
    board[1][0] = turn
  if box == BOX5:
    board[1][1] = turn
  if box == BOX6:
    board[1][2] = turn
  if box == BOX7:
    board[2][0] = turn
  if box == BOX8:
    board[2][1] = turn
  if box == BOX9:
    board[2][2] = turn
  for row in board:
    if row[0] == row[1] and row[1] == row[2] and row[0] != None:
      winner = turn
  for i in range(0,3):
    if board[0][i] == board [1][i] and board[1][i] == board[2][i] and board[0][i] != None:
      winner = turn
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
    winner = turn
  if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != None:
    winner = turn

  if winner == turn:
    fontObj = pygame.font.SysFont('tahoma', 65)
    winMessage = f"{turn} WINS!"
    fontSurfaceObj = fontObj.render(winMessage,  True, (255, 255, 255), (0, 255, 0))
    screen.blit(fontSurfaceObj, (80, 160))
  return board,winner









  


BOX1 = pygame.Rect(50,50,100,100)
BOX2 = pygame.Rect(150,50,100,100)
BOX3 = pygame.Rect(250,50,100,100)
BOX4 = pygame.Rect(50,150,100,100)
BOX5 = pygame.Rect(150,150,100,100)
BOX6 = pygame.Rect(250,150,100,100)
BOX7 = pygame.Rect(50,250,100,100)
BOX8 = pygame.Rect(150,250,100,100)
BOX9 = pygame.Rect(250,250,100,100)

while running:
  mousePosition = ()


  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mousePosition = pygame.mouse.get_pos()
      mouseX = mousePosition[0]
      mouseY = mousePosition[1]
      
      if BOX1.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX1,board,winner)
        print("BOX1")
      if BOX2.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX2,board,winner)
        print("BOX2")
      if BOX3.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX3,board,winner)
        print("BOX3")
      if BOX4.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX4,board,winner)
        print("BOX4")
      if BOX5.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX5,board,winner)
        print("BOX5")
      if BOX6.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX6,board,winner)
        print("BOX6")
      if BOX7.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX7,board,winner)
        print("BOX7")
      if BOX8.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX8,board,winner)
        print("BOX8")
      if BOX9.collidepoint((mouseX,mouseY)):
        board,winner = boxClicked(BOX9,board,winner)
        print("BOX9")
      turn = changeTurn(turn)

  fontObj = pygame.font.SysFont('tahoma', 30)
  fontSurfaceObj = fontObj.render("Tic Tac Toes",  True, (255, 0, 0), (0, 0, 120))
  screen.blit(fontSurfaceObj, (125, 10))

  drawBoard(100)

  pygame.display.update()



  # if mouseX < (boxSize + margin):
      #   boxClickedX = [1,4,7]
      # elif mouseX > (boxSize + margin): 
      #   if mouseX < (boxSize + 2*margin):
      #     boxClickedX = [2,5,8]
      # elif mouseX > (boxSize + 2*margin):
      #   boxClickedX = [3,6,9]
      # if mouseY < (boxSize + margin):
      #   boxClickedY = [1,2,3]
      # elif mouseY > (boxSize + margin): 
      #   if mouseY < (boxSize + 2*margin):
      #     boxClickedY = [4,5,6]
      # elif mouseY > (boxSize + 2*margin):
      #   boxClickedY = [7,8,9]
      # print(boxClickedX)
      # print(boxClickedY)