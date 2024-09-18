import pytest
import os
import json
from player import Player  # Assuming your Player class is in a file named player.py

# Test if saving the game creates a file and contains the correct data
def test_save_game():
    # Create a player object
    player = Player(name="TestPlayer", health=75, game_state="test_state")
    player.add_item("sword", 1)
    savefile = "test_savefile.json"
    
    # Save the game
    player.save_game(savefile)

    # Check if the file was created
    assert os.path.exists(savefile), "Save file was not created!"

    # Load the saved data to ensure correctness
    with open(savefile, 'r') as file:
        data = json.load(file)
        assert data["name"] == "TestPlayer", "Player name mismatch in save file!"
        assert data["health"] == 75, "Player health mismatch in save file!"
        assert data["game_state"] == "test_state", "Game state mismatch in save file!"
        assert data["inventory"]["sword"] == 1, "Inventory item mismatch in save file!"

    # Clean up after the test
    os.remove(savefile)

# Test if loading a saved game correctly restores the player's state
def test_load_game():
    # Simulate a save file
    savefile = "test_savefile.json"
    data = {
        'name': 'TestPlayer',
        'health': 75,
        'inventory': {'sword': 1},
        'game_state': 'test_state'
    }
    
    # Write the test data to the save file
    with open(savefile, 'w') as file:
        json.dump(data, file)

    # Load the game and verify that the player's state is correctly restored
    player = Player.load_game(savefile)
    assert player.name == "TestPlayer", "Player name mismatch after loading game!"
    assert player.health == 75, "Player health mismatch after loading game!"
    assert player.inventory["sword"] == 1, "Inventory item mismatch after loading game!"
    assert player.game_state == "test_state", "Game state mismatch after loading game!"

    # Clean up after the test
    os.remove(savefile)
