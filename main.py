import pygame

pygame.init()

# Variables
icon = pygame.image.load("icon.png")
width, height = 1300, 800
Running = True

# Colors
Black = (0,0,0)
White = (255, 255, 255)

Screen = pygame.display.set_mode((width, height))
Screen.fill(White)
pygame.display.set_caption("DrawScreen")    
pygame.display.set_icon(icon)

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
                
    pygame.display.flip()

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(Screen, Black, mouse_position, 1)

    pygame.display.update()

pygame.quit()