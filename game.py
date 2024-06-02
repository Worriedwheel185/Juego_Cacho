import utils
from scoreboard import Scoreboard

def play_game(players):
    scoreboard = Scoreboard(players)
    game_over = False

    while not game_over:
        for player in players:
            print(f"\nTurno de {player.name}")
            turn(player, scoreboard)
            game_over = scoreboard.check_game_over()
            if game_over:
                break

    scoreboard.display_final_scores()

def turn(player, scoreboard):
    while True:
        print("\n1. Lanzar dados")
        print("2. Ver tablero de anotaciones")
        print("3. Consultar jugadas libres")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            first_throw = utils.roll_dice(5)
            print(f"Primer lanzamiento: {first_throw}")
            if process_throw(player, scoreboard, first_throw):
                break
            dice_to_reroll = input("Ingrese los dados a relanzar (separados por comas, del 1 al 5): ")
            if dice_to_reroll:
                dice_to_reroll = [int(d) for d in dice_to_reroll.split(',')]
                second_throw = utils.roll_dice(5, dice_to_reroll, first_throw)
                print(f"Segundo lanzamiento: {second_throw}")
                process_throw(player, scoreboard, second_throw)
            break  # El turno termina después de lanzar los dados y anotar
        elif choice == '2':
            scoreboard.display()
        elif choice == '3':
            scoreboard.show_free_slots(player)
        else:
            print("Opción no válida. Intente nuevamente.")

def process_throw(player, scoreboard, dice):
    category, score = utils.evaluate_throw(dice, player.get_free_slots())
    print(f"Posibles anotaciones: {category} con {score} puntos.")
    choice = input("¿Desea anotar esta jugada? (s/n): ")

    if choice.lower() == 's':
        scoreboard.update(player, category, score)
        scoreboard.display()
        return True
    return False
