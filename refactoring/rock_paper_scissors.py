
from typing import Tuple

# Original code:
# while True:
# 	player1 = ""
# 	while player1 not in ["rock", "paper", "scissors"]:
# 		player1 = input("player1 make your move (rock, paper, scissors): ")
# 	player2 = ""
# 	while player2 not in ["rock", "paper", "scissors"]:
# 		player2 = input("player2 make your move (rock, paper, scissors): ")
# 	winner_message = ""
# 	if player1 == player2:
# 		winner_message = "The outcome is a tie"
# 	elif player1 == "rock" and player2 == "scissors":
# 		winner_message = "player1 is the winner"
# 	elif player1 == "paper" and player2 == "rock":
# 		winner_message = "player1 is the winner"
# 	elif player1 == "scissors" and player2 == "paper":
# 		winner_message = "player1 is the winner"
# 	elif player2 == "rock" and player1 == "scissors":
# 		winner_message = "player2 is the winner"
# 	elif player2 == "paper" and player1 == "rock":
# 		winner_message = "player2 is the winner"
# 	elif player2 == "scissors" and player1 == "paper":
# 		winner_message = "player2 is the winner"
# 	print(winner_message)
# 	again = ""
# 	while again not in ["y", "n"]:
# 		again = input("Do you want to play again? (y/n): ")
# 	if again == "n":
# 		break
# Source: https://www.practicepython.org/exercise/2022/02/20/37-functions-refactor.html

# Refactored code

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
OPTION_DONT_PLAY_AGAIN = "n"
OPTION_PLAY_AGAIN = "y"

PLAYER_1_NAME = "player1"
PLAYER_2_NAME = "player2"

OUTCOME_TIE = "tie"
game_input_options = [ROCK,PAPER,SCISSORS]
end_game_options = [OPTION_PLAY_AGAIN,OPTION_DONT_PLAY_AGAIN]
outcome_dict = {(ROCK,PAPER):PAPER, (ROCK,SCISSORS):ROCK, (PAPER,SCISSORS):SCISSORS}

def input_for_next_move(player_name: str) -> str:
    return "{} make your move ({})".format(player_name, ",".join(game_input_options))

def form_winner_string(player_name: str) -> str:
    return "{} is the winner!".format(player_name)

def get_player_inputs() -> Tuple[str,str]:
    player1 = ""
    player2 = ""
    while player1 not in game_input_options:
        player1 = input(input_for_next_move(PLAYER_1_NAME))
    while player2 not in game_input_options:
        player2 = input(input_for_next_move(PLAYER_2_NAME))
    return (player1, player2)

def decide_outcome(choice1: str, choice2: str) -> str:
    if choice1 == choice2:
        return OUTCOME_TIE
    if (choice1, choice2) in outcome_dict:
        return outcome_dict[(choice1,choice2)]
    return outcome_dict[(choice2,choice1)]

def form_outcome_string(outcome: str, is_player1_winner: bool) -> str:
    if outcome == OUTCOME_TIE:
        return "the outcome is a {}".format(OUTCOME_TIE)
    if is_player1_winner:
        return form_winner_string(PLAYER_1_NAME)
    return form_winner_string(PLAYER_2_NAME)

def form_play_again_message() -> str:
    return "Do you want to play again? ({}/{}): ".format(OPTION_PLAY_AGAIN, OPTION_DONT_PLAY_AGAIN)

def should_we_play_again(play_again: str) -> bool:
    if play_again == OPTION_PLAY_AGAIN:
        return True
    return False
    

def play():
 
    while True:
        player1, player2 = get_player_inputs()
        outcome = decide_outcome(player1, player2)
        print(form_outcome_string(outcome, player1==outcome))
        again = ""
        while again not in end_game_options:
            again = input(form_play_again_message())
        if not should_we_play_again(again):
            break

if __name__ == "__main__":
    play()



