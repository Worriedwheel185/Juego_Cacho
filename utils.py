import random

def roll_dice(num_dice, dice_to_reroll=None, current_dice=None):
    if dice_to_reroll is None:
        return [random.randint(1, 6) for _ in range(num_dice)]
    else:
        new_dice = current_dice[:]
        for index in dice_to_reroll:
            new_dice[index - 1] = random.randint(1, 6)
        return new_dice

def evaluate_throw(dice, free_slots):
    dice_counts = {i: dice.count(i) for i in range(1, 7)}
    if "grande" in free_slots and 5 in dice_counts.values():
        return "grande", 50
    if "póker" in free_slots and 4 in dice_counts.values():
        return "póker", 40
    if "full" in free_slots and 3 in dice_counts.values() and 2 in dice_counts.values():
        return "full", 30
    if "escalera" in free_slots and (sorted(dice) == [1, 2, 3, 4, 5] or sorted(dice) == [2, 3, 4, 5, 6]):
        return "escalera", 20

    # Anotar en casillas numéricas
    for num, count in dice_counts.items():
        if count > 0:
            category = ["balas", "tontos", "trenes", "cuadras", "quinas", "senas"][num - 1]
            if category in free_slots:
                return category, num * count
    return "balas", 0  # Fallback por defecto, no debería suceder en esta lógica simplificada
