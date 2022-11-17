# Import and initialize the pygame library
import pygame
from config import *

# Set up the drawing window
# flags = pygame.RESIZABLE
flags = pygame.SCALED
screen = pygame.display.set_mode(size=[BOARD_SIZE, BOARD_SIZE], flags=flags, display=0, vsync=0)

# pygame.display.set_icon()
# pygame.display.set_caption()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for x in range(8):
        for y in range(8):
            if (x + y) % 2 == 0:
                color = (0, 144, 0)
            else:
                color = (144, 0, 0)
            pygame.draw.rect(screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.display.quit()