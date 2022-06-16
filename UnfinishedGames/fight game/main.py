import pygame
import time
# screen setup
screen_width = 1800
screen_height = 1013
background = pygame.image.load('background_right.jpg')

field = [(325,819),(1475,819)]

bodywidth = 75
bodyheight = 400

class Player:
    def __init__(self, playername,x, y, dir, health):
        self.playername = playername
        self.x = x
        self.y = y
        self.dir = dir
        self.health = health

def jump(player, playerlist, win):
    a = 1
    v = 1
    height = 30
    for y in range(100):
        v *= a
        print(v)
        player.y += v
        a -= 0.01
        draw_function(win,playerlist)
    time.sleep(1)
    for y in range(100):
        v *= a
        player.y -= v
        a += 0.01
        draw_function(win,playerlist)

def move_player(playerlist):
    for player in playerlist:
        if player.dir == 'left':
            player.x -= 1
        if player.dir  == 'right':
            player.x += 1
        if player.dir == 'down' and not(player.x+bodywidth > 325 and player.x < 1475 and player.y+bodyheight<=819): #cant go trough the field
            player.y += 1
        if player.dir == 'stand':
            return

def draw_function(win,playerlist):
    # background
    win.blit(background,(0,0))
    pygame.draw.rect(win, (255,255,255),(325,819,1150,2))

    for i,player in enumerate(playerlist):
        colors = [(255,0,0),[0,0,255]]
        #body:
        pygame.draw.rect(win, (232, 190, 172), (player.x, player.y, bodywidth, bodyheight))
        #color strap
        pygame.draw.rect(win, colors[i], (player.x, player.y+(2*bodyheight)/3,bodywidth,bodyheight/10))

    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    refresh_time = 0

    player1 = Player('Jef', 325+bodywidth, 819-bodyheight, 'stand', 100)
    player2 = Player('Tom', 1475-bodywidth*2, 819-bodyheight, 'stand', 100)
    playerlist = [player1,player2]

    run = True
    while run:
        refresh_time += clock.get_rawtime()
        clock.tick(60)

        move_player(playerlist)
        draw_function(win,playerlist)

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                #jump player 1
                if event.key == pygame.K_SPACE:
                    jump(player1, playerlist, win)
                #jump player 2
                if event.key == pygame.K_SPACE:
                    jump(player2, playerlist, win)

        key = pygame.key.get_pressed()  # checking pressed keys
        #player 1
        if key[pygame.K_a]:
            player1.dir = 'left'
        elif key[pygame.K_s]:
            player1.dir = 'down'
        elif key[pygame.K_d]:
            player1.dir = 'right'
        else:
            player1.dir = 'stand'
        #player2
        if key[pygame.K_j]:
            player2.dir = 'left'
        elif key[pygame.K_k]:
            player2.dir = 'down'
        elif key[pygame.K_l]:
            player2.dir = 'right'
        else:
            player2.dir = 'stand'

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman')
main(win)
