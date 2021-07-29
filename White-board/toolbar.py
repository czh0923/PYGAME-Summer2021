import pygame

def draw_toolbar(WIN, COLOR, WIDTH, TOOLBAR_HEIGHT):
    pygame.draw.rect(WIN, COLOR, (0, WIDTH + 1, WIDTH, TOOLBAR_HEIGHT))

    #pygame.display.update()


def draw_color_button(WIN, COLOR, PosX, PosY, size):
    return pygame.draw.rect(WIN, COLOR, (PosX, PosY, size, size))

def draw_text_button(WIN, COLOR, PosX, PosY, size):
    return pygame.draw.rect(WIN, COLOR, (PosX, PosY, size, size), 2)
    
def draw_buttons(WIN, WIDTH, HEIGHT, TOOLBAR_HEIGHT, BUTTON_SIZE, COLORS, BUTTON_NUM, TEXT_FONT, COLOR_BUTTON):
    
    PosY = HEIGHT - TOOLBAR_HEIGHT / 2 - BUTTON_SIZE / 2
    for i in range(len(COLORS) - 1): # don't draw a white button
        rect = draw_color_button(WIN, COLORS[i], 10 + i * (WIDTH / BUTTON_NUM), PosY, BUTTON_SIZE)
        COLOR_BUTTON[i] = rect

    BLACK = COLORS[0]
    WHITE = COLORS[4]

    text = ['ERASE', 'CLEAR', 'SAVE']
    for i in range(3): 
        j = i + 4    # j = 4, 5, 6 
        rect = draw_text_button(WIN, BLACK, 10 + j * (WIDTH / BUTTON_NUM), PosY, BUTTON_SIZE)
        COLOR_BUTTON[j] = rect
            
        text_surface = TEXT_FONT.render(text[i], 1, BLACK)
        WIN.blit(text_surface, (10 + j * (WIDTH / BUTTON_NUM) + BUTTON_SIZE / 2 - text_surface.get_width() / 2,
                                PosY + BUTTON_SIZE / 2 - text_surface.get_height() / 2))



def handle_button(x, y, COLOR_BUTTON, WHITE, COLORS):
    for i in COLOR_BUTTON.keys():
        if COLOR_BUTTON[i].collidepoint(x, y):
            if i == 5: # CLEAR
                return 1
            elif i == 6: # SAVE
                return 2
            else:
                return COLORS[i]