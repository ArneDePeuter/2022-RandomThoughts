import pygame
import random
from math import sin, cos,pi

# screen setup
screen_width = 1000
screen_height = 1000
play_width = 960
play_height = 960
x0 = 20
y0 = 20

class Speler:
    def __init__(self, kleur, punten, bouw_dict, voorwerp_dict, machtdict):
        self.kleur = kleur
        self.punten = punten
        self.bouw_dict = bouw_dict
        self.voorwerp_dict = voorwerp_dict
        self.macht_dict = machtdict

def get_spelerlijst(aantalspelers):
    #init dictionaries
    empty_bouwdict = {'straten':[], 'dorpen':[], 'steden':[]}
    empty_voorwerpendict = {'hout':0, 'steen':0, 'graan':0, 'klei':0}
    empty_machtdict = {'riddermacht': False, 'langste_straat': False}

    #create spelers
    speler1=Speler('rood',0,empty_bouwdict, empty_voorwerpendict, empty_machtdict)
    speler2=Speler('wit',0,empty_bouwdict, empty_voorwerpendict, empty_machtdict)
    speler3=Speler('blauw',0,empty_bouwdict, empty_voorwerpendict, empty_machtdict)
    speler4=Speler('zwart',0,empty_bouwdict, empty_voorwerpendict, empty_machtdict)
    return [speler1, speler2, speler3, speler4]

def create_spelbord():
    bord = [
        [('soort','getal'),('soort','getal'),('soort','getal')],
        [('soort','getal'),('soort','getal'),('soort','getal'),('soort','getal')],
        [('soort','getal'),('soort','getal'),('soort','getal'),('soort','getal'),('soort','getal')],
        [('soort','getal'),('soort','getal'),('soort','getal'),('soort','getal')],
        [('soort', 'getal'), ('soort', 'getal'), ('soort', 'getal')]
    ]
    materiaallijst = [  'rover',
                        'klei','klei','klei',
                        'schaap', 'schaap', 'schaap', 'schaap',
                        'hout', 'hout', 'hout', 'hout',
                        'graan', 'graan', 'graan', 'graan',
                        'steen', 'steen', 'steen'
                      ]
    getallijst = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    for i,rij in enumerate(bord):
        for j,blok in enumerate(rij):
            soort, getal = blok
            soort = random.choice(materiaallijst)
            materiaallijst.remove(soort)
            if soort != 'rover':
                getal = random.choice(getallijst)
                getallijst.remove(getal)
            bord[i][j] = (soort, getal)
    return bord

def draw_board(Surface, color, radius, position):
    pi2 = 2 * pi
    n=6

    return pygame.draw.lines( Surface,
                              color,
                              True,
                             [(cos(+ i / n * pi2) * radius + position[0],
                               sin(+ i / n * pi2) * radius + position[1]) for i in range(1, n + 1)],4)

def draw_tile(Surface, color, radius, position):
    pi2 = 2 * pi
    n = 6

    return pygame.draw.lines(Surface,
                             color,
                             True,
                             [(cos((pi / 6) + i / n * pi2) * radius + position[0],
                               sin((pi / 6) + i / n * pi2) * radius + position[1]) for i in range(1, n + 1)])
def draw_function(win,bord):
    # background
    win.fill((0, 0, 0))

    draw_board(win, (255,255,255), 400, (screen_width/2,screen_height/2))
    for

    pygame.display.update()


def main(win):
    clock = pygame.time.Clock()
    refresh_time = 0
    run = True

    #create spelers
    aantalspelers = 4
    spelerlijst = get_spelerlijst(aantalspelers)

    #bord
    bord = create_spelbord()

    while run:
        refresh_time += clock.get_rawtime()
        clock.tick()

        # writing on screen
        if refresh_time > 1:
            draw_function(win,bord)
            refresh_time = 0

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pass

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman')
main(win)