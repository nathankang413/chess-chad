from src.config import *
# import a UserInterface class
from src.game import Game
# import a Bot class

ui = UserInterface()  # place holder, should be a subclass
game = Game()
bot = Bot()  # place holder, should be a subclass

ui.set_game(game)
ui.set_players(HUMAN_PLAYER, bot)

ui.run_loop()