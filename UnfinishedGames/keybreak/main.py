import copy
import pygame
import copy
import random
import string
# screen setup
screen_width = 1000
screen_height = 500

#keys
keys_qwerty = {'rij1':['q','w','e','r','t','y','u','i','o','p'],
        'rij2':['a','s','d','f','g','h','j','k','l'],
        'rij3':['z','x','c','v','b','n','m'],
        'rij4':['space']}

pygame.font.init()
font = pygame.font.SysFont('comicsans', 20, bold=True)

def determine_points(keys):
    aantal_replace = 10
    for replace in range(aantal_replace):
        rij = random.choice(list(keys.keys()))
        index = random.randint(0, len(keys[rij]))
        for i,key in enumerate(keys[rij]):
            if i == index:
                keys[rij][i] = key.upper()
    return keys

def cleanse_key(keys, key):
    for value in keys:
        for x,keytje in enumerate(keys[value]):
            if keytje == key.upper():
                keys[value][x] = key.lower()
    return keys

def draw_function(win,keys):
    # background
    win.fill((0, 0, 0))
    for i,rij in enumerate(keys):
        for j,key in enumerate(keys[rij]):
            if key != key.upper():
                key = font.render('{}'.format(key), 1, (0,0,0))
            else:
                key = font.render('{}'.format(key), 1, (255,0,0))
            if rij != 'rij4':
                pygame.draw.rect(win, (255,255,255), (100+j*((screen_width-100)/len(keys[rij])),100+i*((screen_height-100)/4),40,40))
                rect = key.get_rect(center=(140+j*((screen_width-100)/len(keys[rij]))-20, 100+i*((screen_height-100)/4)+40-20))
                win.blit(key, rect)
            else:
                rect = pygame.draw.rect(win, (255,255,255), (250+j*((screen_width-100)/len(keys[rij])),100+i*((screen_height-100)/4),500,40))
                rect = key.get_rect(center=(250+j*((screen_width-100)/len(keys[rij]))+500-250, 100+i*((screen_height-100)/4)+40-20))
                win.blit(key, rect)
    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()
    refresh_time = 0

    punten = 0
    levens = 3

    keys = copy.deepcopy(keys_qwerty)

    run = True
    while run:
        refresh_time += clock.get_rawtime()
        clock.tick()

        # writing on screen
        if refresh_time > 1:
            draw_function(win,keys)
            refresh_time = 0

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    keys = determine_points(keys)
                else:
                    key = pygame.key.name(event.key)
                    ervoor = keys
                    keys = cleanse_key(keys, key)
                    erna = keys
                    if ervoor.values() != erna.values():
                        punten += 100
                    elif ervoor.values() == erna.values():
                        levens -= 1
                    print(ervoor.values(), '\n', erna.values())
                    print(punten , levens)


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman')
main(win)
