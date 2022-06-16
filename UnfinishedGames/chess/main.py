import pygame
pygame.init()

# screen setup
screen_width = 1000
screen_height = 1000
board_width = 800
board_height = 800

#images
black_pawn = pygame.image.load("images/black_pawn.png")
black_king = pygame.image.load("images/black_king.png")
black_queen = pygame.image.load("images/black_queen.png")
black_rook = pygame.image.load("images/black_rook.png")
black_castle = pygame.image.load("images/black_castle.png")
black_knight = pygame.image.load("images/black_knight.png")
white_pawn = pygame.image.load("images/white_pawn.png")
white_king = pygame.image.load("images/white_king.png")
white_queen = pygame.image.load("images/white_queen.png")
white_rook = pygame.image.load("images/white_rook.png")
white_castle = pygame.image.load("images/white_castle.png")
white_knight = pygame.image.load("images/white_knight.png")


class Player:
    def __init__(self, x, y, godmode):
        self.x = x
        self.y = y
        self.godmode = godmode


def draw_function(win):
    # background
    win.fill((255, 255, 255))
    #drawboard
    for y in range(8):
        for x in range(8):
            if y%2 ==0:
                if x%2 ==0:
                    pygame.draw.rect(win, (0, 0, 0), (100 + x * 100, 100 + y * 100, 100, 100))
                else:
                    pygame.draw.rect(win, (125, 125, 125), (100 + x * 100, 100 + y * 100, 100, 100))
            else:
                if x%2==0:
                    pygame.draw.rect(win, (125, 125, 125), (100 + x * 100, 100 + y * 100, 100, 100))
                else:
                    pygame.draw.rect(win, (0, 0, 0), (100 + x * 100, 100 + y * 100, 100, 100))

    pygame.display.update()


def main(win):
    clock = pygame.time.Clock()
    refresh_time = 0

    run = True
    while run:
        refresh_time += clock.get_rawtime()
        clock.tick()

        # writing on screen
        if refresh_time > 1:
            draw_function(win)
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
