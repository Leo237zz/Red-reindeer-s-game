import pygame
from src.obstacles import SpriteAnimation
from src.player import Animation
import random
import sys


def load_random_obstacle(melon_filename, pumpkin_filename):
    obstacle_type = random.choice(["melon", "pumpkin"])
    x = 1080

    if obstacle_type == "melon":
        animation = SpriteAnimation(melon_filename)
    else:
        animation = SpriteAnimation(pumpkin_filename)

    return animation, obstacle_type, x

def handle_collision(player, obstacle):
    print("Game Over!")
    player.reset_position()
    obstacle.reset_position()

def draw_game_over(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over!", True, (255, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()

def main():
    pygame.init()
    clock = pygame.time.Clock()

    global width, height  # Thêm dòng này để width và height có thể sử dụng trong hàm draw_game_over
    width, height = 1080, 608
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load(r'background\PREVIEW.png')
    floor = pygame.image.load('background/floor.png')
    pygame.display.set_caption('SYLVAN ESCAPE')
    bg_music = pygame.mixer.Sound('sound\BGM_03_mp3.mp3')
    bg_music.play(loops=-1)
    melon_filename = 'asset/melon/animation_melon.png' 
    pumpkin_filename = 'asset/pumkin/animation_pumkin.png'

    player = Animation("player/run/Run.png", initial_position=(100, 300))
    animation, obstacle_type, x = load_random_obstacle(melon_filename, pumpkin_filename)

    game_over = False  # Thêm biến để kiểm tra trạng thái của trò chơi

    while True:
 
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.jump()
                        


            if player.is_collision(animation):
                handle_collision(player, animation)
                game_over = True  # Đặt trạng thái trò chơi thành đã kết thúc
        
            screen.blit(background, (0, 0))
            screen.blit(floor, (-5, 75))

            animation.update()
            animation.draw(screen)

            if x <= -2:
                animation, obstacle_type, x = load_random_obstacle(melon_filename, pumpkin_filename)
            x -= 5

            player.update()
            player.draw(screen)
            player.clock_tick()

            pygame.display.flip()
            clock.tick(30)
        
        else:
            draw_game_over(screen)
            pygame.time.delay(2000)  # Delay để người chơi có thể nhìn thấy thông báo "Game Over"
            pygame.quit()
            sys.exit()
  

if __name__ == "__main__":
    main()
