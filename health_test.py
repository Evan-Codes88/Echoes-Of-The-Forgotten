import pytest
from player import Player
from typewrite import typewrite

def test_take_damage():
    # Create a player with default health of 100
    player = Player(name="Hero", health=100)

    # The player should start with 100 health
    assert player.health == 100

    # The player takes 20 damage
    player.take_damage(20)

    # Assert that the player's health is now 80
    assert player.health == 80