import json




def save_game(self, filename="savegame.json"):
        game_state = {
            "player_name": self.player_name,
            "player_location": self.player_location,
            "inventory": self.inventory,
            "health": self.health
        }
        with open(filename, "w") as f:
            json.dump(game_state, f, indent=4)
        print("Game saved successfully!")

def load_game(self, filename="savegame.json"):
        try:
            with open(filename, "r") as f:
                game_state = json.load(f)
            self.player_name = game_state["player_name"]
            self.player_location = game_state["player_location"]
            self.inventory = game_state["inventory"]
            self.health = game_state["health"]
            print("Game loaded successfully!")
        except FileNotFoundError:
            print("No saved game found. Starting a new game.")
            self.__init__() # Reset to initial state for new game
