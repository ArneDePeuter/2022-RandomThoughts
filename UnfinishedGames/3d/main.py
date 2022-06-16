import pygame as pg
pg.init()

offset = 10
width = 40
height = 200
amount = 10

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

#screen
screenwidht = 500
screenheight = 500
win = pg.display.set_mode((screenwidht,screenheight))

def get_lines():
    amount = screenwidht//(width+offset)
    print(amount)
    lines = []
    for line in range(amount):
        lines.append([[line*(width+offset),screenwidht/2,width, height/2],[line*(width+offset),screenwidht/2-height/2,width, height/2]])
    return lines

def show_line(line):
    for box in line:
        pg.draw.rect(win, white, box)

def draw_screen(lines):
    win.fill(black)
    for line in lines:
        show_line(line)
    pg.display.update()

def get_input():
    run = True
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        if event.type == pg.KEYDOWN:
            pass
    return run

def main():
    pg.display.set_caption("Pygame Default")

    lines = get_lines()

    run = True
    while run:

        draw_screen(lines)
        run = get_input()

    quit()

if __name__ == '__main__':
    main()