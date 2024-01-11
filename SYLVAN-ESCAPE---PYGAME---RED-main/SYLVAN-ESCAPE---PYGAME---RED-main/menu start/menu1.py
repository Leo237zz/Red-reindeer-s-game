import pygame


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Trong_suot = (255, 255, 255, 128)

width, height = 1080, 608
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sylvan Escape")

background = pygame.image.load(r"background\PREVIEW.png")
floor = pygame.image.load("background/floor.png")

font = pygame.font.SysFont("SVN-Retron 2000.otf", 40)
font_title = pygame.font.SysFont("SVN-Retron 2000.otf", 80)
title = font_title.render("Sylvan Escape", True, WHITE)

button =  pygame.image.load(r"menu start\grey_button00.png")
guide = pygame.image.load(r"menu start\sachhd.png")

def draw_button(x, y, width, height, text, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, Trong_suot, (x, y, width, height))
        if click[0] == 1:
            if action == "start":
                print("Start game!")
            elif action == "setting":
                print("Open settings!")
            elif action == "leaderboard":
                print("View leaderboard!")
            elif action == guide:
                print("Guide!")
    else:
        pygame.draw.rect(screen, BLACK, (x, y, width, height))

    text_surface = font.render(text, True, Trong_suot)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)
    screen.blit(title, (350, 150, 900, 50))
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background, (0, 0))
    screen.blit(floor, (-5, 75))
    
    draw_button(200, 250, 700, 50, "Start", "start")
    draw_button(200, 350, 700, 50, "Setting", "setting")
    draw_button(200, 450, 700, 50, "Leaderboard", "leaderboard")
    draw_button(20, 20, 40, 40, "?", guide)
    
    # Cập nhật màn hình
    pygame.display.flip()
