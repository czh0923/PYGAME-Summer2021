import pygame

from red_spaceship import *
from bullet import *
from constants import *
from aliens import *


def draw_window(score, health):
    WIN.blit(SPACE, (0, 0))

    score_txt = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_txt, (10, 10))

    health_txt = HEALTH_FONT.render("Health: " + str(health), 1, WHITE)
    WIN.blit(health_txt, (WIDTH - health_txt.get_width() - 10, 10))

    draw_red_spaceship()

    draw_bullets()

    draw_alien()

    pygame.display.update()

def draw_end(score):

    draw_text = WINNER_FONT.render("Your score is: " + str(score), 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)



def main():
    run = True
    score = 0
    health = 100
    clock1 = pygame.time.Clock()

    while run:

        clock1.tick(FPS)

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
            
            if event.type == YELLOW_ALIEN_DIED:
                score += YELLOW_ALIEN_SCORE
                ALIEN_DIE_SOUND.play()
                print(score)
            
            if event.type == SPACESHIP_DAMAGE:
                health -= 1
                SPACESHIP_DAMAGE_SOUND.play()
        
        red_spaceship_move()

        # use to create long bullets
        #handle_bullets() # long bullet

        bullet_move()

        if pygame.time.get_ticks() % red_alien_refresh == 0:
            red_alien_appear()
        if pygame.time.get_ticks() % yellow_alien_refresh == 0:
            yellow_alien_appear()

        red_alien_move()
        yellow_alien_move()

        handle_alien_spaceship()

        draw_window(score, health)
        
        if health <= 0:
            draw_end(score)
            break
    
    pygame.quit()


if __name__ == "__main__":
    main()
