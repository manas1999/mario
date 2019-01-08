import pygame
skyblue=(135,206,250)
yellow=(255,255,0)
brown=(139,69,19)
black=(255,255,255)
green=(0,255,0)
white=(0,0,0)
pygame.init()
screen=pygame.display.set_mode((1300,600))
pygame.display.set_caption('maneesh')
gameexit=False
x_change=0
y_change=0
x=0
y=425
jump=0
he=pygame.image.load('hero.png')
e1=pygame.image.load('enemy1.jpg')
#e2=pygame.image.load('')
def boundry_check(x,y,x_change,y_change):
      if x>500 and x<600 :
            y=375
            #pygame.draw.rect(screen,black,[570,300,40,300])
      return (x,y,x_change,y_change)
def enemy(x,y):
      if x>400:
            enemy1((x_bg)*-1,0)
            
def enemy1(x,y):
      screen.blit(e1,(x,350))
def mario(x,y):
      screen.blit(he,(x,y))
def bg1(x,y):
      screen.fill(skyblue)
      pygame.draw.rect(screen,brown,[0,600,1300,200])
      pygame.draw.rect(screen,green,[300,400,80,200])
      pygame.draw.rect(screen,yellow,[600,550,250,50])
      pygame.draw.rect(screen,yellow,[650,500,200,50])
      pygame.draw.rect(screen,yellow,[700,450,150,50])
      pygame.draw.rect(screen,yellow,[750,400,100,50])
      pygame.draw.rect(screen,skyblue,[380,600,100,200])



      
      mario(x,y)
def bg2():
      screen.fill(skyblue)
      pygame.draw.rect(screen,brown,[0,600,1300,200])
      x=x+x_change
      y=y+y_change
def hero(x,y):
      mario(x,y)
      
background=pygame.image.load('good.png').convert()
speed_bg=0
x_bg=0
y_bg=0
def bg0(x,y):
      screen.blit(background,(x,y))

clock=pygame.time.Clock()
while  not gameexit :
      
      for event in pygame.event.get():
            jump=0
            if event.type==pygame.QUIT:
                  gameexit=True
            if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_LEFT:
                        #x_change-=10
                        y_change=0
                        speed_bg+=10
                  if event.key==pygame.K_RIGHT:
                        #x_change+=10
                        y_change=0
                        speed_bg-=10
                  #if event.key==pygame.K_DOWN :
                   #     y_change+=10
                    #    x_change=0
                  if event.key==pygame.K_UP:
                        if jump<100:
                              y_change=-10 #   x_change=0
                        if jump>100:
                              y_change=10
            if event.type==pygame.KEYUP:
                  if event.key==pygame.K_LEFT:
                        x_change=0
                        speed_bg=0
                  if event.key==pygame.K_RIGHT:
                        x_change=0
                        speed_bg=0
                  if event.key==pygame.K_DOWN:
                        y_change=0
                  if event.key==pygame.K_UP:
                        y_change=+10
      jump=jump+(y_change)*-1
      if y>=425:
            y=425
      x=x_change*-1
      #y=y_change*-1
      (x,y,x_change,y_change)=boundry_check(x,y,x_change,y_change)
      if jump<100:
            y=y+y_change
      if jump>100:
            y=y+y_change
      x_bg=x_bg+speed_bg
      bg0(x_bg,y_bg)
      enemy(x,y)
      #enemy1(400+x_bg,400+y_bg)
      hero(x,y)
      
      
            
      
      pygame.display.update()
      clock.tick(30)
pygame.quit()
quit()
