import game
import player

def main_menu():
    print("Bienvenido al juego de Cacho Alalay")
    print("1. Iniciar nuevo juego")
    print("2. Salir")
    choice = input("Seleccione una opción: ")
    return choice

def main():
    players = []
    while True:
        choice = main_menu()
        if choice == '1':
            num_players = int(input("Ingrese el número de jugadores: "))
            for i in range(num_players):
                name = input(f"Nombre del jugador {i + 1}: ")
                players.append(player.Player(name))
            game.play_game(players)
        elif choice == '2':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
