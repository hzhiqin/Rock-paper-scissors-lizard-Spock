"""
    play Rock-paper-scissors-lizard-Spock
"""

import rpsls_helper

print("rock\nSpock\npaper\nlizard\nscissors")
print("type in one above\n")
choice_of_player = input("make your choice\n")
result = rpsls_helper.rpsls(choice_of_player)
if result == 1:
    print("player wins")
elif result == -1:
    print("computer wins")
elif result == 0:
    print("it is a tie")
