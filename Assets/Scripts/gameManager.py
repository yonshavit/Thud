from enum import Enum
from board import Board
import player


class GameManager:
    """GameManager class to hold the game objects and logic loop."""
    def __init__(self):
        name = raw_input("Enter the first player's name: ")
        self.players[0] = player.Player(name, Race["Dwarf"])
        name = raw_input("Enter the second player's name: ")
        self.players[1] = player.Player(name, Race["Troll"])
        self.current_turn = "Dwarf"
        self.game_board = Board()


class Race(Enum):
    Dwarf = 1
    Troll = 2
