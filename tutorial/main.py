import pygame 

from red_spaceship import *
from bullet import *
from constants import *


def draw_window():
    WIN.blit(SPACE, (0, 0))

    draw_red_spaceship(WIN)

    draw_bullets(WIN)

    pygame.display.update()


def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                # comment bullet_appear_one_at_a_time() out when creating long bullets
                bullet_appear_one_at_a_time(event) # 1. shot bullet
                pass
        
        red_move()

        # use to create long bullets
        #handle_bullets() # 2. long bullet

        # comment bullet_move() out and use handle_bullets to create long bullets
        bullet_move() # 1. shot bullet
        
        draw_window()
    
    pygame.quit()


if __name__ == "__main__":
    main()
