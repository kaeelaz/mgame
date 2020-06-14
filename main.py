import pygame as pg
import random 

#setting some values in variables
#--------------colors-----------

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)              #comment added for test
red=(255,0,0)


#---------------------------images-------------

firstpic=pg.image.load('data/circle.png')
secpic=pg.image.load('data/sphere.png')
explosion=pg.image.load('data/exp.png')
menubg=pg.image.load('data/menubg.png')
op1=pg.image.load('data/tile1.png')
op2=pg.image.load('data/tile2.png')
op1op=pg.image.load('data/t1.png')
op2op=pg.image.load('data/t2.png')
#------------------------------------------------

turn=0
score=0
screenx=1300
screeny=720
screensize=(screenx,screeny)
#---------------------------------------------
#--------initialize-------------
pg.init()
win=pg.display.set_mode(screensize)
pg.display.set_caption("Minestep")
#-------------------------------------
#-------sounds------------------
mined=pg.mixer.Sound('data/mined.wav')
pop=pg.mixer.Sound('data/clicksound.wav')

#----------------------
#--------font--------------
text=pg.font.Font('freesansbold.ttf',40)
gameType="onep "
#----------------------------
running=True     #to run the loop
Firstrun=True    #to check if the program is running for the first time to show game menu

#--------------initialize dictionary that contains grid-----------
Grid={} #this grid will contain a tuple denoting row and colume as a key,and the state "clicked" or "unclicked" as value

        #these will store the drawing cordinate of each grid
bombed_grid=(random.randint(0,6),random.randint(0,6))

#--------functions-------------------

#ruin when game is over----
def game_over(gtype):
    global score
    global turn
    global Firstrun
    global bombed_grid
    Firstrun=True
    if gtype=="onep":
        run=True
        while run:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
                    make_grid()
                    
                    
                    run=False
                    
                    break
                    
            msg=text.render("YOU LOSE",True,black)
            msg1=text.render("YOUR SCORE: "+ str(score),True,black)
            win.fill(white)
            win.blit(msg,(600,300))
            win.blit(msg1,(600,500))
           
            
            pg.display.update()
            
    if gtype=="mulp":
        run=True
         
        while run:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
                    make_grid()
                   
                  
                    run=False
                    
                    break
                 
            msg=text.render("player "+str(turn+1)+" DIED",True,black)
            
            win.fill(white)
            win.blit(msg,(600,300))
            
            pg.display.update()   

    return
#this function finds what grid is being clicked-------
def find_gridadd(mx,my):
    x=(mx-335)//100  #mx and my are mouse cordinates
    y=(my-0)//100
    return (x,y)

#this function assigns values to grid

def make_grid():
    global Grid
    for i in range(0,7,1):
        for j in range(0,7,1):
            Grid[(i,j)]="UC"

#this function draws grids

def draw_grid():
    global Grid
    for i in range(0,7,1):
        for j in range(0,7,1):
            if Grid[(i,j)]=="C":
                
                win.blit(secpic,(i*100+335,j*100))
            else:
                win.blit(firstpic,(i*100+335,j*100))
  

#this function checks if the clicked grid is safe

def is_safe(x,y):
    global bombed_grid
    testx,testy=bombed_grid
    if testx==x and testy==y:
        return False
    else:
        return True

#------create menu-------------

def menu():
    global Firstrun,op1,op2,menubg,op1op,op2op,running,gameType,bombed_grid,turn,score
    run=True
    x1=585
    y1=300
    x1e=785
    y1e=400
    x2=585
    y2=500
    x2e=785
    y2e=600
    firstop=op1
    secop=op2
    while run:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
                running=False
                break
            if event.type==pg.MOUSEBUTTONDOWN:
             
                mx,my=pg.mouse.get_pos()
                if (mx>x1 and mx<x1e) and (my>y1 and my<y1e):
                    run=False
                    Firstrun=False
                    bombed_grid=(random.randint(0,6),random.randint(0,6))
                    score=0
                    gameType="onep"
                   
                elif (mx>x2 and mx<x2e) and (my>y2 and my<y2e):
                    run=False
                    Firstrun=False
                    bombed_grid=(random.randint(0,6),random.randint(0,6))
                    turn=0
                    gameType="mulp"
                   
        mx,my=pg.mouse.get_pos()
        if (mx>x1 and mx<x1e) and (my>y1 and my<y1e):
            firstop=op1op
        elif (mx>x2 and mx<x2e) and (my>y2 and my<y2e):
            secop=op2op
        else:
             firstop=op1
             secop=op2
        win.blit(menubg,(0,0))
        win.blit(firstop,(585,300))
        win.blit(secop,(585,500))
        pg.display.update()

    return
        
 #-------------------------------------------------



#---------------main loop-----------------
make_grid()

while running==True:
   
    win.fill(white)
    for event in pg.event.get():
        if Firstrun==True:
            menu()
        if event.type==pg.QUIT:
                running=False
        if event.type==pg.MOUSEBUTTONDOWN:
                pop.play()
                mx,my=pg.mouse.get_pos()
                if (mx>335 and mx<1035) and (my>0 and my<700):

                   
                    row,col=find_gridadd(mx,my)
                    
                    if Grid[(row,col)]=="UC":
                        if is_safe(row,col) != True:
                            pg.time.delay(1000)
                            mined.play()
                            game_over(gameType)
                        else:
                             Grid[(row,col)]="C"
                             score+=1
                             turn=(turn+1)%2
                             
                           
 
  
    
    
        
        
            
           
    draw_grid()
    
    if gameType=="onep":
        scoreshow=text.render("YOUR SCORE: "+ str(score),True,black)
        win.blit(scoreshow,(0,200))
        
    if gameType=="mulp":
        turnshow=text.render("player "+str(turn+1),True,black)
        win.blit(turnshow,(0,200))
        turnshow2=text.render("is selecting.. ",True,black)
        win.blit(turnshow2,(0,300))
       

    pg.display.update()