import pygame

swidth = 1000
sheight = 1000

def check_action(drawpos,action,size):
    (x, y) = drawpos
    uitvoer = 'Select'
    if y >= sheight-50:
        if x <=50:
            action = 'Draw_selected'
        elif x <=100:
            action = 'Erase_selected'
        elif x <=150:
            action = 'Fill_selected'
        elif x <= 250:
            action = 'Size_selected'
            size = round((x-150)/10)
        else:
            action = 'Draw_selected'
            uitvoer = 'Draw'
    else:
        uitvoer = 'Draw'
    return action, size, uitvoer

def draw_screen(win,action,drawpos,size, uitvoer):
    x,y = drawpos
    win.fill((255,255,255))
    drawsize = int(size)//2
    drewlist = []

    pygame.draw.rect(win,(0,0,0), (0,sheight-50,50,50))
    pygame.draw.rect(win,(125,125,125), (50,sheight-50,50,50))
    pygame.draw.rect(win,(0,0,0), (100,sheight-50,50,50))
    pygame.draw.rect(win,(125,125,125), (150,sheight-50,100,50))

    if action == 'Draw_selected' and uitvoer == 'Draw':
        drewlist.append((drawpos,size))
        for pixel in drewlist:
            (px,py), drewsize = pixel
            pygame.draw.rect(win,(0,0,255), (px-drewsize//2,py-drewsize//2,drewsize,drewsize))
    if action == 'Erase_selected' and uitvoer == 'Draw':
        for pixel in drewlist:
            (px,py), drewsize = pixel
            if x >= px and x <= px+drewsize and y >= py and y <= py+drewsize:
                drewlist.remove(pixel)

    if action == 'Fill_selected':
        pass
    if action == 'Size_selected' and y >= sheight-50 and x <= 250:
        pygame.draw.rect(win, (255,0,0), (x-2, sheight-50, 5, 50))

    pygame.display.update()

def main(win):
    run = True
    clock = pygame.time.Clock()
    drawpos = tuple
    action = str
    updatetime = 0
    size = 5

    while run:
        updatetime += clock.get_rawtime()
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawpos = pygame.mouse.get_pos()
                action, size, uitvoer = check_action(drawpos,action,size)
                print('action=', action, '\nsize = ' + str(size))

                while updatetime>1:
                    draw_screen(win, action, drawpos, size, uitvoer)
                    updatetime = 0

win = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('Paint')
main(win)