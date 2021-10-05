import pygame
from pygame.draw import *

def head (surface,head_center,hair_col,eye_col,skin_col,nose_col,mouse_col,pupil_col):
    '''
   Функция рисует голову одного человечка
    '''
    circle(surface, skin_col, (head_center, 250), 130)

    polygon(surface, mouse_col, [(head_center-70,275), (head_center+70,275),(head_center,320)])

    polygon(surface, nose_col, [(head_center-10,247), (head_center+10,247),(head_center,265)])

    polygon(surface, (0,0,0), [(head_center-70,275), (head_center+70,275),(head_center,320)],1)
    polygon(surface, (0,0,0), [(head_center-10,247), (head_center+10,247),(head_center,265)],1)

    circle(surface, eye_col ,(head_center+50, 210), 25)
    circle(surface, eye_col, (head_center-50, 210), 25)
    circle(surface, (0,0,0), (head_center+50, 210), 25,1)
    circle(surface, (0,0,0), (head_center-50, 210), 25,1)

    circle(surface, pupil_col, (head_center+50, 215), 7)
    circle(surface, pupil_col, (head_center-50, 215), 7)

    polygon(surface, hair_col, [(head_center-92,158),(head_center-71,137),(head_center-92,128)])
    polygon(surface, (0,0,0), [(head_center-92,158),(head_center-71,137),(head_center-92,128)],1)
    polygon(surface, hair_col, [(head_center-75,144),(head_center-50,127),(head_center-75,114)])
    polygon(surface, (0,0,0), [(head_center-75,144),(head_center-50,127),(head_center-75,114)],1)
    polygon(surface, hair_col, [(head_center-55,132),(head_center-28,119),(head_center-55,102)])
    polygon(surface, (0,0,0), [(head_center-55,132),(head_center-28,119),(head_center-55,102)],1)
    polygon(surface, hair_col, [(head_center-34,124),(head_center-5,116),(head_center-30,94)])
    polygon(surface, (0,0,0), [(head_center-34,124),(head_center-5,116),(head_center-30,94)],1)
    polygon(surface, hair_col, [(head_center-11,120),(head_center+19,117),(head_center,90)])
    polygon(surface, (0,0,0), [(head_center-11,120),(head_center+19,117),(head_center,90)],1)
    polygon(surface, hair_col, [(head_center+11,121),(head_center+41,124),(head_center+24,98)])
    polygon(surface, (0,0,0), [(head_center+11,121),(head_center+41,124),(head_center+24,98)],1)
    polygon(surface, hair_col, [(head_center+34,124),(head_center+63,132),(head_center+52,100)])
    polygon(surface, (0,0,0), [(head_center+34,124),(head_center+63,132),(head_center+52,100)],1)
    polygon(surface, hair_col, [(head_center+55,132),(head_center+82,145),(head_center+70,112)])
    polygon(surface, (0,0,0), [(head_center+55,132),(head_center+82,145),(head_center+70,112)],1)
    polygon(surface, hair_col, [(head_center+75,144),(head_center+100,161),(head_center+94,128)])
    polygon(surface, (0,0,0), [(head_center+75,144),(head_center+100,161),(head_center+94,128)],1)
    polygon(surface, hair_col, [(head_center+92,158),(head_center+108,179),(head_center+108,148)])
    polygon(surface, (0,0,0), [(head_center+92,158),(head_center+108,179),(head_center+108,148)],1)

def arms (surface,head_center,skin_col,body_col):
    '''
    Функция рисует руки одного человечка
    '''
    polygon(surface, skin_col, [(head_center+115,360), (head_center+127,369),(head_center+230,40),
                               (head_center+218,31)])
    polygon(surface, skin_col, [(head_center-115,360), (head_center-127,369),(head_center-230,40),
                               (head_center-218,31)])

    circle(surface, skin_col, (head_center+215,40), 25)
    circle(surface, skin_col, (head_center-215,40), 25)
    polygon(surface, body_col, [(head_center+80,360), (head_center+110,320),(head_center+150,335),
                               (head_center+150,385),(head_center+110,400)])
    polygon(surface, body_col, [(head_center-80,360), (head_center-110,320),(head_center-150,335),
                               (head_center-150,385),(head_center-110,400)])
    polygon(surface, (0,0,0), [(head_center+80,360), (head_center+110,320),(head_center+150,335),
                              (head_center+150,385),(head_center+110,400)],1)
    polygon(surface, (0,0,0), [(head_center-80,360), (head_center-110,320),(head_center-150,335),
                              (head_center-150,385),(head_center-110,400)],1)

 def body (surface,head_center,body_col):
    '''
    Функция рисует тело одного человечка
    x,y - координаты центра головы
    size - размер головы
    '''
    circle(surface, body_col, (head_center, 480), 150)

    circle(surface, body_col, (x,y), size)

def person (surface,head_center,hair_col,eye_col,skin_col,nose_col,mouse_col,pupil_col):
    '''
    Функция рисует человечка
    '''
    head(surface,head_center,hair_col,eye_col,skin_col,nose_col,mouse_col,pupil_col)
    arms(surface,head_center,skin_col,body_col)
    body(surface,head_center,body_col)


head_center=290#координата центра головы,head_center
body_col=(255, 117, 34)#цвет тела ,b
hair_col=(180, 0, 227)#цвет волос,h
eye_col=(1, 215, 232)#цвет глаз,e
skin_col=(255, 220, 185)#цвет кожи,s
nose_col=(87, 0, 2)#цвет носа,n
mouse_col=(255, 0, 0)#цвет рта,m
pupil_col=(0, 0, 0)#цвет зрачков,z


pygame.init()
FPS = 30
screen = pygame.display.set_mode((1010, 450))
screen.fill((255,255,255))
surface = pygame.Surface()

person(surface, 290,(1, 100, 1),(226, 226, 0),(205, 230, 212),skin_col,nose_col,mouse_col,pupil_col)
person(surface,720,body_col,hair_col,eye_col,skin_col,nose_col,mouse_col,pupil_col)

rect(screen, (0, 254, 0), (40, 0, 930, 45))
rect(screen, (0, 0, 0), (40, 0, 930, 45),1)
f1 = pygame.font.Font(None, 80)
text1 = f1.render('PYTHON is REALLY AMAZING!', True,
                  (0, 0, 0))
screen.blit(text1,(80,0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
