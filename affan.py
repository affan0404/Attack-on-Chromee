#affan

import random
import pygame
from pygame import *
from math import *
pygame.init()



# game constants

RED =(255,0,0)   
GREEN =(0,255,0)
BLACK =(0,0,0)
WHITE = (255,255,255)   
YELLOW = (255,255,0)
ORANGE = (255,165,0)
BLUE = (39,59,226)
BLANK = (178,34,34,0.2)
WIDTH = 800
HEIGHT = 600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

# game variables

ground=Rect(0, 500 ,1600, 200)

score = 0
highscore = 0
player_x = 50
player_y = 440
y_change = 0
x_change = 0
gravity = 1
lives = 3
level = 0
enemy = [850,1750,1850]
enemy0_speed = 1
enemy1_speed = 1.3
enemy2_speed = 10
path_speed = 4
ammo = 3
ammo_speed = 3
coin_speed = 1
slow_speed = 6
ground_speed = 4
active = False
jump=False

#images

newtitle= pygame.image.load("pics/newtitle.png")
renewtitle=pygame.transform.scale(newtitle,(400,100))

mani= pygame.image.load("pics/man1.png")
remani=pygame.transform.scale(mani,(WIDTH, HEIGHT))

book= pygame.image.load("pics/book.png")
rebook=pygame.transform.scale(book,(30,20))

play= pygame.image.load("pics/play.png")
replay=pygame.transform.scale(play,(30,20))

mark= pygame.image.load("pics/mark.png")
remark=pygame.transform.scale(mark,(30,20))

free= pygame.image.load("pics/free.png")
refree=pygame.transform.scale(free,(30,20))

man22= pygame.image.load("pics/noman.png")
reman22=pygame.transform.scale(man22,(WIDTH, HEIGHT))

man11= pygame.image.load("pics/ner(1).png")
reman11=pygame.transform.scale(man11,(WIDTH, HEIGHT))

stage1= pygame.image.load("pics/lvl1.png") 
restage1=pygame.transform.scale(stage1,(WIDTH, HEIGHT)) 

stage2= pygame.image.load("pics/new222.jpg") 
restage2=pygame.transform.scale(stage2,(WIDTH, HEIGHT)) 

stage3= pygame.image.load("pics/lvl3.png") 
restage3=pygame.transform.scale(stage3,(WIDTH, HEIGHT)) 

end= pygame.image.load("pics/endless.png") 
reend=pygame.transform.scale(end,(WIDTH, HEIGHT)) 

path= pygame.image.load("pics/block.png") 
repath=pygame.transform.scale(path,(1600, 200)) 

eren= pygame.image.load("pics/eren000.png")
reeren=pygame.transform.scale(eren,(40,70))

levi= pygame.image.load("pics/ded.png")
relevi=pygame.transform.scale(levi,(140,90))

coin= pygame.image.load("pics/coin.png")
recoin=pygame.transform.scale(coin,(40,40))

aammoo= pygame.image.load("pics/aammoo.png")
reaammoo=pygame.transform.scale(aammoo,(40,40))

slow= pygame.image.load("pics/boost.png")
reslow=pygame.transform.scale(slow,(50,40))

titans= pygame.image.load("pics/lmob2.png")
retitans=pygame.transform.scale(titans,(90,50))

bigt= pygame.image.load("pics/smob2.png")
rebigt=pygame.transform.scale(bigt, (60,80))

loss= pygame.image.load("pics/LOSS.png")
reloss=pygame.transform.scale(loss,(WIDTH, HEIGHT))

#powerups

coverRect = pygame.Rect(0,0,800,600)
ammoRect = pygame.Rect(random.randint(800, 900), 200, 40, 40) 
coinRect = pygame.Rect(random.randint(800, 900), 300, 40, 50)
slowRect = pygame.Rect(random.randint(800, 900), 450, 50, 50)

print(ammoRect)
print(slowRect)  
print(coinRect)


#sounds

explosion = pygame.mixer.Sound('pics/timerSound_sounds_boom.wav')
coins = pygame.mixer.Sound('pics/cash.wav')
motion = pygame.mixer.Sound('pics/moo.wav')
blast = pygame.mixer.Sound('pics/blast.wav')
audio = pygame.mixer.Sound('pics/song.mp3')
audio1 = pygame.mixer.Sound('pics/click.wav')


#background,fps, and title

screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("Attack On Chrome")
background = BLACK
fps = 60
font = pygame.font.Font("freesansbold.ttf",16)
timer = pygame.time.Clock()
frame=0
frame1=0

#functions

def instructions():
    running = True
    inst = pygame.image.load("pics/instructions.png")
    inst = pygame.transform.smoothscale(inst, screen.get_size())
    pygame.draw.rect(screen,ORANGE,(0,0,800,600))            
    screen.blit(inst,(0,0))
    while running:
        print("instructions")
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]:
            running = False
        display.flip()
    return "menu"

def story():
    running = True
    story = pygame.image.load("pics/newstory.png")
    story = pygame.transform.smoothscale(story, screen.get_size())
    pygame.draw.rect(screen,WHITE,coverRect)
    screen.blit(reman11,(0, 0))
    screen.blit(story,(0,0))
    while running:
        print("story")
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]:
            running = False
        display.flip()
    return "menu"

def items():
    running = True
    story = pygame.image.load("pics/items(1)(2).png")
    story = pygame.transform.smoothscale(story, screen.get_size())
    screen.blit(remani,(0, 0))
    screen.blit(story,(0,0))
    while running:
        print("items")
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]:
            running = False
        display.flip()
    return "menu"


def coin():
    global coinRect,score,coin
    if coinRect[0] < 0: 
        coinRect = pygame.Rect(random.randint(860, 1060),random.randint(200,300),40, 40)
        
    screen.blit(recoin,(coinRect[0], coinRect[1] + 2.5))
    if active:
        coinRect[0] -= coin_speed
    if player.colliderect(coinRect):
        coins.play()
        coinRect = pygame.Rect(random.randint(860, 1060),random.randint(200,300),40, 40)
        score += 40
        
def slow():
    global slowRect,score,enemy0_speed, enemy1_speed, enemy2_speed
    if slowRect[0] < 0:
        slowRect = pygame.Rect(random.randint(2000, 3000), 450, 50, 50)

    screen.blit(reslow,(slowRect[0], slowRect[1] + 5))
    if active and level >= 3:
        slowRect[0] -= slow_speed
    if player.colliderect(slowRect):
        motion.play()
        slowRect = pygame.Rect(random.randint(2000, 3000), 450, 50, 50)
        enemy0_speed -= 0.20
        enemy1_speed -= 0.20
        enemy2_speed -= 0.20

def high():
    global highscore
    if highscore <= score: 
        highscore = score


def ammoo():
    global ammoRect,ammo,score
    if ammoRect[0] < 0:
        ammoRect = pygame.Rect(random.randint(860, 1660), random.randint(180,280), 40, 40)

    screen.blit(reaammoo,(ammoRect[0], ammoRect[1] + 2.5))
    if active and level >= 2:
        ammoRect[0] -= ammo_speed
    if player.colliderect(ammoRect):
        blast.play()
        ammoRect = pygame.Rect(random.randint(1500, 2000), random.randint(185,280), 40, 40)
        enemy[0] = random.randint(1060, 1560)
        enemy[1] = random.randint(1060, 1560)
        enemy[2] = random.randint(1060, 1560)
        score += 25

    
def lvls():
    global level
    if score >= 0 and score <= 150:
        
        screen.blit(restage1,(0, 0))
        level = 1
        
    elif score >= 150 and score <= 300:
        screen.blit(restage2,(0, 0))
        level = 2
        
    elif score >= 300 and score <= 500:
        screen.blit(restage3,(0, 0))
        level = 3
        
    else:
        screen.blit(reend,(0, 0))
        level = 4

def game():
    global active,player_x,player_y,enemy,jump,frame,score,x_change,y_change,player,ground_speed,coinRect,slowRect,ammoRect,enemy0_speed,enemy1_speed,enemy2_speed
    running=True

    #timer and instructions before game start
        
    running = True
    while running:
        
        timer.tick(fps)
        screen.fill(background)
        if not active:
            start_text = font.render(f'Space To Start', True, WHITE, BLACK)
            screen.blit(start_text, (500, 100))
            start_text2 = font.render(f'Space Bar Jumps. Left/Right Moves', True, WHITE, BLACK)
            screen.blit(start_text2, (100, 100))
            
            

    #Shapes
            
        floor = pygame.draw.rect(screen, RED, [0,500,900,5])
        player = pygame.draw.rect(screen,GREEN, [player_x, player_y, 35, 60])
        shot = pygame.draw.rect(screen,GREEN, [player_x, player_y, 35, 35]) ###
        enemy0 = pygame.draw.rect(screen,RED, [enemy[0], 450, 90, 50])
        enemy1 = pygame.draw.rect(screen,ORANGE, [enemy[1], 250, 40, 40])
        enemy2 = pygame.draw.rect(screen,YELLOW, [enemy[2], 420, 60, 80])
        

    #prints background before objects
        
        lvls()
         
    #animates character
        
        print(jump)
        if jump:
            if int(frame) == 8:
                jump=False
                frame=0
                
            else:

                frame += 0.2
                somepath="pics/eren00"+(str(int(frame))+".png")
                eren= pygame.image.load(somepath)
                reeren=pygame.transform.scale(eren,(40,70))

        else:
                

            frame+=0.2
            if(int(frame) == 10):
                frame=0
            somepath="pics/eren00"+(str(int(frame) + 8)+".png")
            print(somepath)
            eren= pygame.image.load(somepath)
            reeren=pygame.transform.scale(eren,(40,70))
            
            

    #blits objects onto screen

        if active:
            ground[0] -= 1
            if ground[0] == -800:
                ground[0] = 0
                
        #screen.blit(repath,(900, 5)) 
        screen.blit(reeren,(player_x,player_y))
        screen.blit(relevi,(enemy[1] -45, 250))
        screen.blit(retitans,(enemy[0], 450))
        screen.blit(rebigt,(enemy[2], 420))
        screen.blit(repath,(ground[0],ground[1]))
        score_text = font.render(f'Score: {score}', True, WHITE, BLANK)
        screen.blit(score_text, (700, 500))
        level_text = font.render(f'Level: {level}', True, WHITE, BLUE)
        screen.blit(level_text, (500, 500))
        high_text = font.render(f'HIGHSCORE: {highscore}', True, WHITE, ORANGE)
        screen.blit(high_text, (200, 500))
        lives = 3

    #resets after lose and inital start
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not active:
                 if event.key == pygame.K_SPACE:
                    enemy = [950,950,950]
                    player_x = 50
                    score = 0
                    path_speed = 4
                    enemy0_speed = 1
                    enemy1_speed = 1.5
                    enemy2_speed = 2
                    audio.play()
                    active = True
    #movement
                    
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_w and y_change == 0:
                    y_change = 22.5
                    frame=0
                    jump=True
                if event.key == pygame.K_d:
                    x_change = 2
                if event.key == pygame.K_a:
                    x_change = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_a:
                    x_change = 0


    #enemy movment
             
        for i in range(len(enemy)):
            if active:
                enemy[0] -= enemy0_speed
                
            if active and level >= 2:
                enemy[1] -= enemy1_speed 
            if active and level >= 3:
                enemy[2] -= enemy2_speed
                
            if enemy[0] < -20:
                enemy[0] = random.randint(860, 1560)
                score += 15
                ground_speed += 1
                enemy0_speed += 0.050
            if enemy[1] < -20:
                enemy[1] = random.randint(860, 1560)
                score += 15
                ground_speed += 1
                enemy1_speed += 0.050
            if enemy[2] < -20:
                enemy[2] = random.randint(860, 1560)
                score += 15
                ground_speed += 1
                enemy2_speed += 0.050

    #checks for collision and resets game

            if player.colliderect(enemy0):
                coinRect = pygame.Rect(random.randint(860, 1060),random.randint(200,300),40, 40)
                slowRect = pygame.Rect(random.randint(2000, 3000), 450, 50, 50)
                ammoRect = pygame.Rect(random.randint(1500, 2000), random.randint(185,280), 40, 40)
                explosion.play()
                audio.stop()
                lives -= 1
                print("hello",lives)
                
                enemy[0] = random.randint(860, 1060)

            elif player.colliderect(enemy1):
                coinRect = pygame.Rect(random.randint(860, 1060),random.randint(200,300),40, 40)
                slowRect = pygame.Rect(random.randint(2000, 3000), 450, 50, 50)
                ammoRect = pygame.Rect(random.randint(1500, 2000), random.randint(185,280), 40, 40)
                explosion.play()
                audio.stop()
                lives -= 1
                print("hello",lives)
                enemy[1] = random.randint(860, 1060)

            elif player.colliderect(enemy2):
                coinRect = pygame.Rect(random.randint(860, 1060),random.randint(200,300),40, 40)
                slowRect = pygame.Rect(random.randint(2000, 3000), 450, 50, 50)
                ammoRect = pygame.Rect(random.randint(1500, 2000), random.randint(185,280), 40, 40)
                explosion.play()
                audio.stop()
                lives -= 1
                print("hello",lives)
                enemy[2] = random.randint(860, 1060)
                
            if lives == 0:
                active = False
            if active == False:
                screen.blit(reloss,(0, 0))
                
                    
                    
    #limits player movement so no offsides
                
        if 0 <= player_x <= 750:
            player_x += x_change
        if player_x < 0:
            player_x = 0
        if player_x > 750:
            player_x = 750
            
    #jump and gravity
            
        if y_change > 0 or player_y < 440:
            player_y -= y_change
            y_change -= gravity
        if player_y > 440:
            player_y = 440
        if player_y == 440 and y_change < 0:
            y_change = 0
            
        
        ammoo()
        slow()
        coin()
        high()
        
        display.flip()

    return "menu"  

def menu(): 
    running = True
    myClock = pygame.time.Clock()
    buttons=[pygame.Rect(150+x*150,450,80,40) for x in range(4)]#creating the buttons
    while running:
        print("menu")
        for evnt in event.get():            
            if evnt.type == QUIT:
                return "exit"
        screen.fill(0)
        screen.blit(reman22,(0, 0))
        screen.blit(renewtitle,(200, 50))
        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        for b in buttons:
            pygame.draw.rect(screen,WHITE,b)
            pygame.draw.rect(screen,BLACK,b,8)
            screen.blit(rebook,(625, 460))
            screen.blit(remark,(475, 460))
            screen.blit(refree,(325, 460))
            screen.blit(replay,(175, 460))

        if mb[0]==1:
            if buttons[0].collidepoint(mx,my):
                return "game"
            if buttons[1].collidepoint(mx,my):
                return "items"
            if buttons[2].collidepoint(mx,my):
                return "instructions"
            if buttons[3].collidepoint(mx,my):
                return "story" 
            
        display.flip()
        myClock.tick(60)
        
screen = display.set_mode((800, 600))
running = True

x,y = 0,0
OUTLINE = (150,50,30)
page = "menu"
while page != "exit":
    if page == "menu":
        audio1.play()
        page = menu()
        
    if page == "game":
        audio1.play()
        page = game()
        
    if page == "items":
        audio1.play()
        page = items()
        
    if page == "instructions":
        audio1.play()
        page = instructions()
        
    if page == "story":
        audio1.play()
        page = story()



    display.flip()

quit()
