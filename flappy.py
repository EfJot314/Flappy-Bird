import pygame
import sys
import random
from pygame.locals import *
pygame.init()
plansza = pygame.display.set_mode((600,600))
pygame.display.set_caption('Flappy bird')
zegar=pygame.time.Clock()
FPS=60
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(124,252,0)
BLUE=(135,206,250)
YELLOW=(255,255,0)

czcionka=pygame.font.SysFont("monospace",30)

przegrana=False
można=True

jump=True
v=0
y=0

tab=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
yg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
yd=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
wsk=300

vx=3

score=0
licznik=4


zaczynamy_gre=False
czy_gramy=False


while True:
    while True:
        plansza.fill(BLUE)
        napis1=czcionka.render("Flappy bird",1,BLACK)
        napis2=czcionka.render("1 - Start",1,BLACK)
        napis3=czcionka.render("2 - Wyjdź",1,BLACK)
        plansza.blit(napis1,(200,200))
        plansza.blit(napis2,(200,300))
        plansza.blit(napis3,(200,350))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_2):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_1:
                zaczynamy_gre=True

        if zaczynamy_gre==True:
            break
        pygame.display.update()
        zegar.tick(FPS)
            
    zaczynamy_gre=False
    przegrana=False
    można=True

    jump=True
    v=0
    y=0

    tab=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    yg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    yd=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    wsk=300

    vx=3

    score=0
    licznik=4


    #początek
    while True:
        plansza.fill(BLUE)
        if y>=0:
            jump=True
            licznik=licznik-1
        if jump==True:
            jump=False
            v=-8
        v=v+0.5
        y=y+v
        y=int(y)
        pygame.draw.circle(plansza, YELLOW, (100,y+300),10,0)
        if licznik<=3:
            napis=czcionka.render(str(licznik), 1, BLACK)
            if licznik<0:
                napis=czcionka.render("START", 1, BLACK)
            plansza.blit(napis,(250,250))
        pygame.display.update()
        zegar.tick(FPS)
        if licznik==-1:
            break
    


    #no i gramy
    while True:
        plansza.fill(BLUE)
    
    
        #przeszkody
        czy=random.randint(0,20)
        if czy==1 and wsk<500:
            for i in range(0,20):
                if tab[i]==0:
                    tab[i]=1
                    break
        wsk=True
        for i in range(0,19):
            if i==0 and x[0]<-30 and tab[0]==1:
                x[i]=600
                yg[i]=yg[19]+random.randint(-100,100)
                if yg[i]<0:
                    yg[i]=yg[i]+100
                yd[i]=random.randint(yg[i]+200,600)
            if tab[i]==1 and x[i]<-30:
                x[i]=600
                yg[i]=yg[i-1]+random.randint(-100,100)
                if yg[i]<0:
                    yg[i]=yg[i]+100
                yd[i]=random.randint(yg[i]+100,600)
            x[i]=x[i]-vx
            if x[i]>wsk:
                wsk=x[i]
            if x[i]<-30:
                tab[i]=0

            if tab[i]==1:
                pygame.draw.rect(plansza, GREEN, (x[i],0,27,yg[i]))
                pygame.draw.rect(plansza, GREEN, (x[i],yd[i],27,600-yd[i]))
    

        #skakanko
        if jump==True:
            jump=False
            v=-8
        v=v+0.5
        y=y+v
        y=int(y)

        pygame.draw.circle(plansza, YELLOW, (100,y+300),10,0)

         #kontrola
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                jump=True

        #przegrane i score
        for i in range(0,19):
            if x[i] <=100 and x[i]>=70:
                score=score+1
                if yg[i]>y+300:
                    przegrana=True
                    break
                if yd[i]<y+300:
                    przegrana=True
                    break
        if y>=330:
            break
        if przegrana==True:
            break

        #score
        napis=czcionka.render(str(int(score/10)), 1, BLACK)
        plansza.blit(napis,(400,50))

    
        pygame.display.update()
        zegar.tick(FPS)


    #koniec
    koniec=czcionka.render("PRZEGRAŁEŚ", 3, BLACK)
    kontynuacja=czcionka.render("wciśnij dowolny klawisz",1,BLACK)
    plansza.blit(koniec,(200,250))
    plansza.blit(napis,(400,50))
    plansza.blit(kontynuacja,(100,350))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                czy_gramy=True
        if czy_gramy==True:
            break
            
    
    







    
