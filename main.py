import random
import time
player1_value = 0
player2_value = 0

for y in range(50):


    for i in range(1):
         input("Player 1's turn. Press enter player 1")
         current_dice_value_p1 = random.randint(1, 6)
         print(f"Player 1 rolled: {current_dice_value_p1}")
         player1_value = player1_value + current_dice_value_p1
         print(f"Player 1 is on: {player1_value}")

         # if player1_value < 50:
         #     input("Player 2's turn. Press enter player 2")

    if player1_value >= 50:
        print(f"Player 1 wins. Score: {player1_value}")
        time.sleep(1)
        print("Game Over")
        break

    for j in range(1):
         input("Player 2's turn. Press enter player 2")
         current_dice_value_p2 = random.randint(1, 6)
         print(f"Player 2 rolled: {current_dice_value_p2}")
         player2_value = player2_value + current_dice_value_p2
         print(f"Player 2 is on: {player2_value}")

         # if player2_value < 50:
         #     input("Player 1's turn. Press enter player 1")

    if player2_value >= 50:
        print(f"Player 2 wins. Score: {player2_value}")
        time.sleep(1)
        print("Game Over")
        break