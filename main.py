from game import Game
from player import Player
import random

def run():
    print("Let's play a game")
    game = Game()
    p1 = Player("Peyton", 1)
    (roll1, roll2) = roll_dice()
    print(f"Player rolled {roll1} and {roll2}.  Move {roll1 + roll2}")
    move_player(p1, game, roll1 + roll2)
    # game.print_avail_properties()


def move_player(player, game, spaces):
    player.space = player.space + spaces
    prop = game.get_property(player.space)
    print(f"Player landed on {prop.name}")
    if prop.owner == 0:
        print(f"{prop.name} is unowned, would you like to buy it for ${prop.cost}?")
        game.purchase_property(prop, player)
        print(player)



def roll_dice():
    return (random.randint(1,6), random.randint(1,6))

if __name__ == "__main__":
    run()