import pygame 
import math

pygame.init()
screen = pygame.display.set_mode((600,400))

#color - the background in Azure the players and ball in white
Azure = (240, 255, 255)
white = (255, 255, 255)

#icon from flaticon, caption, background, font
pygame.display.set_caption("Pong")
icon = pygame.image.load(r"C:\Users\Arian\Documents\Programming\Python\Pong\icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font(r"C:\Users\Arian\Documents\Programming\Python\Pong\font.ttf", 32)

#the variables and picture of the rectangles for the player
def drawrect(x,y):
    pygame.draw.rect(screen, white, [x, y, 8, 80])
rect1_x = 8          #rect1 is the left player
rect1_y = 320
rect1_change = 0
rect2_x = 584        #rect2 is the right player
rect2_y = 320
rect2_change = 0

#variables and picture of the ball 
def drawball(x,y):
    pygame.draw.rect(screen, white, [x, y, 12, 12])
ballX = 300
ballY = 200
ballx_change = -0.1
global bally_change
bally_change = 0.0


#this is the function for detecting if the ball has collided with the left player
#I needed to create two functions because the ball must be a certain distance away from the rectangle and pass a certain x-cord
def ballcollision1(rectX, rectY, ballx, bally):
    global bally_change
    distance = math.sqrt(math.pow(rectX-ballx,2))+math.sqrt(math.pow(rectY-bally,2))
    ydistance = rectY-bally
    
    if distance<90 and ballx<16 and ydistance<10:
        for i in range(10, -80, -1):                #if the ball hits the upper rectangle it goes up
            if int(ydistance)==i:                   #so I created a for loop which identifies where the ball collided
                bally_change = -(i+40)*0.001        #and creates the slope of the ball after the collision -(i+40)*0.001 

        return True
    else:   
        False

#this is the function for detecting if the ball has collided with the left player
def ballcollision2(rectX, rectY, ballx, bally):
    global bally_change
    distance = math.sqrt(math.pow(rectX-ballx,2))+math.sqrt(math.pow(rectY-bally,2))
    ydistance = rectY-bally
    
    if distance<90 and ballx>580 and ydistance<10:
        for i in range(10, -80, -1):
            if int(ydistance)==i:
                bally_change = -(i+40)*0.005

        return True

#background
def drawboder(x,y):
    pygame.draw.rect(screen, Azure, [x, y, 600, 8])
def drawmiddle(x,y):
    pygame.draw.rect(screen, Azure, [x, y, 8, 8])
    

#score, font from dafont.com
score1 = 0
score2 = 0
def showscore(scorevalue,x,y):
    score = font.render(str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x,y))


running=True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #You move the left rectangle with the arrow-keys and the right on with w and s
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: 
                rect2_change = 0.1
            if event.key == pygame.K_UP:
                rect2_change = -0.1

            if event.key == pygame.K_w:
                rect1_change = -0.1
            if event.key == pygame.K_s:
                rect1_change = 0.1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                rect2_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                rect1_change = 0

    rect1_y += rect1_change
    rect2_y += rect2_change
    
    #rectangles touching the borders
    if rect1_y >= 311:
        rect1_y = 311
    if rect1_y <= 1:
        rect1_y = 1
    if rect2_y >= 311:
        rect2_y = 311
    if rect2_y <= 1:
        rect2_y = 1
    
    #ball touching the border
    if ballY>=386:
        bally_change = -bally_change
    if ballY<=1:
        bally_change = -bally_change
    
    #ball touching player
    collision1 = ballcollision1(rect1_x, rect1_y, ballX, ballY)
    collision2 = ballcollision2(rect2_x, rect2_y, ballX, ballY)
    
    if collision1:
       ballx_change = 0.1
    if collision2:
        ballx_change = -0.1
    
    ballX += ballx_change
    ballY += bally_change

    #drawing the players
    drawrect(rect1_x,rect1_y)
    drawrect(rect2_x,rect2_y)
    drawball(ballX, ballY)

    #scores
    if ballX>600:
        score1 +=1
        ballX = 300
        ballY = 200
        ballx_change = -0.1
        bally_change = 0
    elif ballX<0:
        score2+=1
        ballX = 300
        ballY = 200
        ballx_change = 0.1
        bally_change = 0

    #drawing the background 
    drawboder(0, 1)
    drawboder(0, 391)
    for i in range(12, 384, 16):
        drawmiddle(300, i)
    showscore(score1, 40, 10)
    showscore(score2, 540, 10)

    pygame.display.update()