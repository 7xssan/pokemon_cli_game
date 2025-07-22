import random
import get_pokemon
import CPU_pokemon

CPU = CPU_pokemon.chosen_pokemon

player = get_pokemon.player_pokemon

turn_number = 1
flee = False

print(f"You encounter a wild {CPU["pokemon"].capitalize()} while walking in the long grass!")

start_battle = input(f"Would you like to use {player["pokemon"].capitalize()}? (y/n) ")

if start_battle.lower() == "n":
    print("You successfully flee from the battle!")
    flee = True
else:
    while player["hp"] > 0 and CPU["hp"] > 0:
        if turn_number % 2 != 0:
            attack_value = random.randint(1, 10)
            CPU["hp"] -= attack_value
            print(f"Your {player["pokemon"].capitalize()} uses {player["move_name"]}!")
            print(f"The opposing {CPU["pokemon"]} takes {attack_value} points of damage!")
            turn_number += 1
        else:
            move_number = random.randint(0, len(CPU["moves"]) - 1)
            attack_value = random.randint(1, 10)
            player["hp"] -= attack_value
            print(f"The opposing {CPU["pokemon"].capitalize()} uses {CPU["moves"][move_number]}!")
            print(f"Your {player["pokemon"]} takes {attack_value} points of damage!")
            turn_number += 1

    if player["hp"] <= 0 and not flee:
        print(f"Your {player["pokemon"]} has fainted! Teleporting you back to town...")
    else:
        print(f"The opposing {CPU["pokemon"]} has fainted. Your {player["pokemon"]} gains 100 exp!")
