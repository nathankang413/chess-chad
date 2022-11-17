# Import and initialize the pygame library
import pygame
from config import *
from game import Game
from user_interface import UserInterface

class PygameGUI(UserInterface):
    """
    A UserInterface implemented with PyGame
    """

    def __init__(self, game: Game = None, players: tuple = None) -> None:
        super().__init__(game, players)

    def set_game(self, game: Game) -> None:
        super().set_game(game)

    def set_players(self, *players) -> None:
        super().set_players(*players)

    def run_loop(self) -> None:
        super().run_loop()

        # init display and screen
        screen = pygame.display.set_mode(size=[BOARD_SIZE, BOARD_SIZE], flags=pygame.SCALED)
        pygame.display.set_icon()
        pygame.display.set_caption()

        # game loop
        running = True
        while running:

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # checker board
            for x in range(8):
                for y in range(8):
                    if (x + y) % 2 == 0:
                        color = (0, 144, 0)
                    else:
                        color = (144, 0, 0)
                    pygame.draw.rect(screen, color, 
                        (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            pygame.display.flip()
        
        pygame.display.quit()