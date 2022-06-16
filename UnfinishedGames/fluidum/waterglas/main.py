import pygame
import math
# screen setup
screen_width = 1000
screen_height = 1000

#glas
class Glass():
    def __init__(self, glas_breedte, glas_hoogte, glas_dikte):
        self.glas_breedte = glas_breedte
        self.glas_hoogte = glas_hoogte
        self.glas_dikte = glas_dikte
        self.bottomleft = [screen_width/2-self.glas_breedte/2,screen_height]
        self.topleft = [screen_width/2-self.glas_breedte/2,screen_height-self.glas_hoogte]
        self.bottomright = [screen_width/2+self.glas_breedte/2,screen_height]
        self.topright = [screen_width/2+self.glas_breedte/2,screen_height-self.glas_hoogte]

    def draw_glas(self,win):
        pygame.draw.line(win, (200,200,200), self.bottomleft, self.topleft ,self.glas_dikte)
        pygame.draw.line(win, (200,200,200), self.bottomright, self.topright,self.glas_dikte)
        pygame.draw.line(win, (200,200,200), self.bottomleft, self.bottomright,self.glas_dikte)

    def rotate_point(self, angle, point, aroundpoint):
        s = math.sin(angle)
        c = math.cos(angle)
        point[0] = (point[0]-aroundpoint[0]) * c - (point[1]-aroundpoint[1]) * s
        point[1] = (point[0]-aroundpoint[0]) * s - (point[1]-aroundpoint[1]) * c
        return point

    def rotate_glass(self,angle):
        middlepoint = ((self.bottomleft[0]+self.bottomright[0])/2,(self.bottomleft[1]+self.bottomright[1])/2)
        self.rotate_point(angle, self.bottomleft, middlepoint)
        self.rotate_point(angle, self.bottomright, middlepoint)
        self.rotate_point(angle, self.topleft, middlepoint)
        self.rotate_point(angle, self.topright, middlepoint)

class Water():
    def __init__(self, glas_hoogte, topleft, topright, bottomleft, bottomright):
        self.topleft = topleft
        self.topright = topright
        self.bottomleft = bottomleft
        self.bottomright = bottomright
        self.glas_hoogte = glas_hoogte

    def draw_water(self, win):
        pygame.draw.polygon(win, (0,0,255), ((self.topleft[0],self.topleft[1]+self.glas_hoogte/10),(self.topright[0], self.topright[1]+self.glas_hoogte/10),self.bottomright,self.bottomleft), 0)

def draw_function(win,glass,water):
    # background
    win.fill((0, 0, 0))
    water.draw_water(win)
    glass.draw_glas(win)

    pygame.display.update()


def main(win):
    glass = Glass(100, 200, 10)
    clock = pygame.time.Clock()

    angle = 0

    run = True
    while run:
        water = Water(glass.glas_hoogte, (screen_width/2-glass.glas_breedte/2,screen_height-glass.glas_hoogte),(screen_width/2+glass.glas_breedte/2,screen_height-glass.glas_hoogte),(screen_width/2-glass.glas_breedte/2,screen_height), (screen_width/2+glass.glas_breedte/2,screen_height) )
        clock.tick(60)

        draw_function(win,glass,water)

        # using physical inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle += 30
                if event.key == pygame.K_RIGHT:
                    angle -= 30
                glass.rotate_glass(angle)


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman')
main(win)
