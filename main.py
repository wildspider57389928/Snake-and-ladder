import pygame
from random import randint
from time import sleep
print("hello to my game.im bardia mehrju.")
print("rules:")
print("1.if you have six you will have a second turn.")
print("2.if you have 3 sixes you will go to first block.")
print("coming soon:if you go on another player's block you will have three more turns.")
print("4.now we have to play game.")
sleep(10)
print("preparing...")
sleep(4)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("snake.mp3")
screen=pygame.display.set_mode((660,660))
screen.fill((255,255,255))
pygame.display.set_caption("snake and ladder")
p1=pygame.image.load("player1.png")
p2=pygame.image.load("player2.png")
dice1=pygame.image.load("dice1.png")
dice2=pygame.image.load("dice2.png")
dice3=pygame.image.load("dice3.png")
dice4=pygame.image.load("dice4.png")
dice5=pygame.image.load("dice5.png")
dice6=pygame.image.load("dice6.png")
screen.fill((255,255,255))
pygame.display.update() 
clock=pygame.time.Clock()
clock.tick(60)
board=pygame.image.load("board.png")  
screen.blit(board,(0,0))
screen.blit(p1,(5,594))
screen.blit(p2,(30,594))
pygame.display.flip()
p1up=[(599,594),(5,528),(599,462),(5,396),(599,330),(5,264),(599,198),(5,132),(599,66)]
p1left=[528,396,264,132,0]
p1right=[594,462,330,198,66]
p1ladder=[(203,594),(533,528),(401,528),(71,462),(5,330),(401,264)]
p1ladderup=[(269,264),(599,330),(335,264),(137,264),(71,132),(467,66)]
p1snake=[(467,462),(203,396),(467,330),(335,132),(401,0),(269,0)]
p1snakedown=[(599,594),(137,594),(269,528),(533,396),(599,132),(71,330)]
p2up=[(624,594),(30,528),(624,462),(30,396),(624,330),(30,264),(624,198),(30,132),(624,66)]
p2left=[528,396,264,132,0]
p2right=[594,462,330,198,66]
p2ladder=[(228,594),(558,528),(426,528),(96,462),(30,330),(426,264)]
p2ladderup=[(294,264),(624,330),(360,264),(162,264),(96,132),(492,66)]
p2snake=[(492,462),(228,396),(492,330),(360,132),(426,0),(294,0)]
p2snakedown=[(624,594),(162,594),(294,528),(558,396),(624,132),(96,330)]
p1x,p1y=5,594
p2x,p2y=30,594
turn=1
six=0
pygame.mixer.music.play(99)
while True:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit() 
       if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RETURN:
         if turn==1:  
           if (p1x,p1y)==(5,0):
                print("player 1 won the game")
                break
           dicen=randint(1,6)
           move=dicen*66
           if dicen==1:
               screen.blit(dice1,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==2:
               screen.blit(dice2,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==3:
               screen.blit(dice3,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==4:
               screen.blit(dice4,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==5:
               screen.blit(dice5,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==6:
               screen.blit(dice6,(264,264))
               pygame.display.update()
               sleep(2)
               six+=1
           while True:
            if six==3:
                six=0
                p1x,p1y=5,594
                screen.blit(board,(0,0))
                screen.blit(p2,(p2x,p2y))
                screen.blit(p1,(p1x,p1y))
                turn=2
                break
            if move==0:break
            if (p1x,p1y) in p1up:
                p1y-=66
                screen.blit(board,(0,0))
                screen.blit(p2,(p2x,p2y))
                screen.blit(p1,(p1x,p1y))
            elif p1y in p1left:
                p1x-=66
                screen.blit(board,(0,0))
                screen.blit(p2,(p2x,p2y))
                screen.blit(p1,(p1x,p1y))            
            elif p1y in p1right:
              p1x+=66
              screen.blit(board,(0,0))
              screen.blit(p2,(p2x,p2y))
              screen.blit(p1,(p1x,p1y))
            if (p1x,p1y) in p1ladder or (p1x,p1y) in p1snake:
             for i in p1ladder:
                if (p1x,p1y)==i and move==66:
                    p1x=p1ladderup[p1ladder.index(i)][0]
                    p1y=p1ladderup[p1ladder.index(i)][1]
                    screen.blit(board,(0,0))
                    screen.blit(p2,(p2x,p2y))
                    screen.blit(p1,(p1x,p1y))
             for i in p1snake:
                if (p1x,p1y)==i and move==66:
                    p1x=p1snakedown[p1snake.index(i)][0]
                    p1y=p1snakedown[p1snake.index(i)][1]
                    screen.blit(board,(0,0))
                    screen.blit(p2,(p2x,p2y))
                    screen.blit(p1,(p1x,p1y))        
            if (p1x,p1y)==(5,0):
                print("player 1 won the game")
                break        
            move-=66
            if dicen!=6:
             turn=2
         elif turn==2:
           if (p2x,p2y)==(5,0):
                print("player 2 won the game")
                break
           dicen=randint(1,6)
           move=dicen*66
           if dicen==1:
               screen.blit(dice1,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==2:
               screen.blit(dice2,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==3:
               screen.blit(dice3,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==4:
               screen.blit(dice4,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==5:
               screen.blit(dice5,(264,264))
               pygame.display.update()
               sleep(2)
               six=0
           elif dicen==6:
               screen.blit(dice6,(264,264))
               pygame.display.update()
               sleep(2)
               six+=1
           while True:
            if six==3:
                six=0
                p2x,p2y=30,594
                screen.blit(board,(0,0))
                screen.blit(p2,(p2x,p2y))
                screen.blit(p1,(p1x,p1y))
                turn=1
                break
            if move==0:break
            if (p2x,p2y) in p2up:
                p2y-=66
                screen.blit(board,(0,0))
                screen.blit(p2,(p2x,p2y))
                screen.blit(p1,(p1x,p1y))
            elif p2y in p2left:
                p2x-=66
                screen.blit(board,(0,0))
                screen.blit(p2,(p2x,p2y))
                screen.blit(p1,(p1x,p1y))            
            elif p2y in p2right:
              p2x+=66
              screen.blit(board,(0,0))
              screen.blit(p2,(p2x,p2y))
              screen.blit(p1,(p1x,p1y))
            if (p2x,p2y) in p2ladder or (p2x,p2y) in p2snake:
             for i in p2ladder:
                if (p2x,p2y)==i and move==66:
                    p2x=p2ladderup[p2ladder.index(i)][0]
                    p2y=p2ladderup[p2ladder.index(i)][1]
                    screen.blit(board,(0,0))
                    screen.blit(p2,(p2x,p2y))
                    screen.blit(p1,(p1x,p1y))
             for i in p2snake:
                if (p2x,p2y)==i and move==66:
                    p2x=p2snakedown[p2snake.index(i)][0]
                    p2y=p2snakedown[p2snake.index(i)][1]
                    screen.blit(board,(0,0))
                    screen.blit(p2,(p2x,p2y))
                    screen.blit(p1,(p1x,p1y))        
            if (p2x,p2y)==(5,0):
                print("player 2 won the game")
                break        
            move-=66
            if dicen!=6:
             turn=1
    pygame.display.update()
