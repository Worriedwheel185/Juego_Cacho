class Scoreboard:
    def __init__(self, players):
        self.players = players

    def update(self, player, category, score):
        player.update_score(category, score)

    def check_game_over(self):
        for player in self.players:
            if any(value is None for value in player.scoreboard.values()):
                return False
        return True

    def display(self):
        for player in self.players:
            print(f"\nTablero de {player.name}")
            for category, score in player.scoreboard.items():
                if score is None:
                    score = 0  # Mostrar 0 en lugar de None
                print(f"{category}: {score}")

    def display_final_scores(self):
        print("\nPuntajes finales:")
        for player in self.players:
            total_score = sum(score for score in player.scoreboard.values() if score is not None)
            print(f"{player.name}: {total_score} puntos")

    def show_free_slots(self, player):
        free_slots = player.get_free_slots()
        print(f"Casillas libres para {player.name}: {list(free_slots.keys())}")
