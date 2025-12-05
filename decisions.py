#Decision making
import random
#kyles codeeee
# Define possible moves
# The order goes rock > paper > scissors, so you will see paper_scissors but never scissors_paper

def We_Play_RS(opponent_move):
    """
    Our team chooses rock + scissors.
    Decide which hand to play based on opponent's move.
    """

    # Opponent plays rock + rock → we play rock
    if opponent_move == "rock_rock":
        return  "rock"

    # Opponent plays paper + paper → we play scissors
    elif opponent_move == "paper_paper":
        return "scissors"

    # Opponent plays scissors + scissors → we play rock
    elif opponent_move == "scissors_scissors":
        return "rock"

    # Opponent plays rock + scissors → we play rock
    elif opponent_move == "rock_scissors":
        return "rock"

    # Opponent plays rock + paper → 25 scissors, 75% rock
    elif opponent_move == "rock_paper":
        if random.random() <= 0.75:
            return "rock"
        else:
            return "scissors"

    # Opponent plays scissors + paper → we play scissors
    elif opponent_move == "paper_scissors":
        if random.random() <= 0.65:
            return "scissors"
        else:
            return "rock"
    # Default fallback (if unexpected input)

def rock_paper_chosen(opponent_moves):

    if opponent_moves == "rock_rock":
        return "paper"

    elif opponent_moves == "paper_paper":
        return "paper"

    elif opponent_moves == "scissors_scissors":
        return "rock"

    elif opponent_moves == "rock_paper":
        return "paper"

    elif opponent_moves == "rock_scissors":
        if random.random() <= 0.65:
            return "rock"
        else:
            return "paper"

    elif opponent_moves == "paper_scissors":
        if random.random() <= 0.75:
            return "paper"
        else:
            return "rock"

# Lynns code
def we_play_scissors_paper(opponent_move):
  if opponent_move == "rock_scissors":
      if random.random() <= 0.75:
          return "scissors"
      else:
          return "paper"

  elif opponent_move== "paper_scissors":
      return "scissors"

  elif opponent_move=="rock_paper":
      if random.random() <=0.65:
          return "paper"
      else:
          return "scissors"

  elif opponent_move== "paper_paper":
      return "scissors"

  elif opponent_move =="rock_rock":
      return "paper"

  elif opponent_move == "scissors_scissors":
      return "scissors"

if __name__ == "__main__":
    play = We_Play_RS("paper_scissors")
    print(play)