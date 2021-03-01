import random

while True:
    user_action = input("elige una opcion (piedra, papel, tijera): ")
    possible_actions = ["piedra", "papel", "tijera"]
    computer_action = random.choice(possible_actions)
    print(f"\nelegistes {user_action}, rival elige {computer_action}.\n")

    if user_action == computer_action:
        print(f"ambos jugadores eligieron {user_action}. Empate")
    elif user_action == "piedra":
        if computer_action == "tijera":
            print("piedra destruye tijera! has ganado!")
        else:
            print("papel cubre piedra! has perdido.")
    elif user_action == "papel":
        if computer_action == "roca":
            print("papel cubre piedra! has ganado!")
        else:
            print("tijeras cortan papel! has perdido.")
    elif user_action == "tijera":
        if computer_action == "papel":
            print("tijera cortan papel! has ganado!")
        else:
            print("piedra destruye tijera! has perdido.")

    otra_vez = input("deseas jugar de nuevo? (y/n): ")
    if otra_vez.lower() != "y":
        break
