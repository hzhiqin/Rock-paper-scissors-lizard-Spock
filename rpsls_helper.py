"""
    Helper module of Rock-paper-scissors-lizard-Spock
"""
import random


def rpsls(player_choice):
    """
    takes a string as input, which is one of rock ,paper,scissor, lizard or Spock.
    The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by
    generating its own random choice from these alternatives and then determining
    the winner using a simple rule
    :param player_choice: the player choice
    :return: a boolean indicates winner
    """
    choice_num = name_to_number(player_choice)
    if choice_num == _ErrorCode.WRONG_INPUT:
        print("invalid input")
    choice_computer = computer_guess()
    choice_computer_num = choice_computer[0]
    choice_computer_name = choice_computer[1]
    print("computer guess "+choice_computer_name)
    return winner(choice_num, choice_computer_num)


def winner(player, computer):
    """
    go through the rule to check who won
    :param player: playe choice
    :param computer: computer choice
    :return: a int indicates winner
    +1: player wins
    -1: computer wins
    0: a tie
    """
    diff = player - computer
    if diff < 0:
        diff = diff + 5
    if diff == 1 or diff == 2:
        return 1
    elif diff == 3 or diff == 4:
        return -1
    elif diff == 0:
        return 0


def name_to_number(name):
    """
    that converts the string  into a number between 0 and 4.
    0 — rock
    1 — Spock
    2 — paper
    3 — lizard
    4 — scissors
    :param name: the name of player choice
    :return: a number
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return _ErrorCode.WRONG_INPUT


def number_to_name(num):
    """
    translate the number back to name
    :param num:
    0 — rock
    1 — Spock
    2 — paper
    3 — lizard
    4 — scissors
    :return: the name of choice
    """
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"


def computer_guess():
    """
    generate computer guess
    :return: [num 0-4, name]
    """
    rand_num = random.randrange(5)
    return [rand_num, number_to_name(rand_num)]


class _ErrorCode:
    """
    Error code for rpsls.py
    """
    WRONG_INPUT = 11
