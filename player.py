class Player:
    def __init__(self, name):
        self.name = name
        self.scoreboard = {
            "balas": None,
            "tontos": None,
            "trenes": None,
            "cuadras": None,
            "quinas": None,
            "senas": None,
            "escalera": None,
            "full": None,
            "póker": None,
            "grande": None
        }

    def update_score(self, category, score):
        if self.scoreboard[category] is None:
            self.scoreboard[category] = score
        else:
            print(f"La categoría {category} ya está anotada.")

    def get_free_slots(self):
        return {k: v for k, v in self.scoreboard.items() if v is None}
