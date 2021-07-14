import pygame

from red_spaceship import *
from bullet import *
from constants import *
from aliens import *


def draw_window(score):
    WIN.blit(SPACE, (0, 0))

    score_txt = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_txt, (10, 10))

    draw_red_spaceship()

    draw_bullets()

    draw_alien()

    pygame.display.update()


def main():
    run = True
    score = 0

    while run:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == key_fire:
                    one_bullet()
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_ALIEN_DIED:
                score += RED_ALIEN_SCORE
                ALIEN_DIE_SOUND.play()
                print(score)
        
        red_move()

        # use to create long bullets
        #handle_bullets() # long bullet

        bullet_move()

        if pygame.time.get_ticks() % red_alien_refresh == 0:
            red_alien_appear()

        red_alien_move()
        
        draw_window(score)
    
    pygame.quit()


if __name__ == "__main__":
    main()
