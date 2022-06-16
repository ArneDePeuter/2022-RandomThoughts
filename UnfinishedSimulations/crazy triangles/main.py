import pygame
import math

screen_width = 1000
screen_height = 1000

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

def draw_function(win,triangles, middles):
    # background
    win.fill((125, 125, 125))
    for i, triangle in enumerate(triangles):
        pygame.draw.polygon(win, (55*i,0,20*i), (triangle.p1, triangle.p2, triangle.p3))
    pygame.draw.polygon(win, (255,255,255), middles)
    for middle in middles:
        pygame.draw.circle(win, (0,0,255), middle, 10)
    pygame.display.update()

def calc_p3(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    # express coordinates of the point (x2, y2) with respect to point (x1, y1)
    dx = x2 - x1
    dy = y2 - y1

    alpha = 60 / 180 * math.pi
    # rotate the displacement vector and add the result back to the original point
    xp = x1 + (math.cos(alpha) * dx + math.sin(alpha) * dy)
    yp = y1 + (math.sin(-alpha) * dx + math.cos(alpha) * dy)

    return (xp, yp)

def get_triangles(triangle):
    triangle1 = Triangle(triangle.p1, triangle.p2, calc_p3(triangle.p1, triangle.p2))
    triangle2 = Triangle(triangle.p1, triangle.p3, calc_p3(triangle.p1, triangle.p3))
    triangle3 = Triangle(triangle.p3, triangle.p2, calc_p3(triangle.p3, triangle.p2))

    return [triangle, triangle1, triangle2, triangle3]

def middle(triangle):
    x = (triangle.p1[0] + triangle.p2[0]+ triangle.p3[0])/3
    y = (triangle.p1[1] + triangle.p2[1]+ triangle.p3[1])/3
    return (x,y)

def get_get_middles(triangles):
    middles = []
    for triangle in triangles:
        if triangle != triangles[0]:
            middles.append(middle(triangle))
    return middles

def main(win):
    clock = pygame.time.Clock()
    triangle = Triangle((200,300), (500,600), (100,700))
    triangles = get_triangles(triangle)

    run = True
    while run:
        clock.tick(60)

        triangles = get_triangles(triangle)
        middles = get_get_middles(triangles)

        draw_function(win,triangles, middles)

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    triangle.p1 = pygame.mouse.get_pos()
                if event.key == pygame.K_2:
                    triangle.p2 = pygame.mouse.get_pos()
                if event.key == pygame.K_3:
                    triangle.p3 = pygame.mouse.get_pos()


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman')
main(win)
