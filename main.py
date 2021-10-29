import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
still_playing = True


from art import logo 

print(logo)


def deal_card():
  card = random.choice(cards)
  return card

first_player_cards = user_cards.append(deal_card())
second_player_card = user_cards.append(deal_card())

first_computer_card = computer_cards.append(deal_card())
second_computer_card = computer_cards.append(deal_card())

print(f" User cards: {user_cards}")
print(f" Computer cards: {computer_cards}")

def compare(cards_comp, cards_player):
  score_comp = sum(cards_comp)
  score_player = sum(cards_player)
  if score_comp == score_player:
    return "It's a draw"
  elif score_comp == 0:
    return "Computer has blackjack, bad luck!"
  elif score_player == 0:
    return "User has blackjack you win!"
  elif score_player > 21:
    return "You lose"
  elif score_comp > 21:
    return "You win"
  elif score_comp > score_player:
    return "The computer won"
  elif score_player > score_comp:
    return "User won"
  else:
    return "error"

def computer_play():
  while sum(computer_cards) < 17:
    computer_cards.append(deal_card())

computer_play()

def calculate_score():
  if sum(user_cards) == 21:
    return 0
  if 11 in user_cards and sum(user_cards) > 21:
    user_cards.remove(11)
    user_cards.append(1)
  if sum(user_cards) == 0 or sum(user_cards) > 21:
    return "Game over!!!"
  while still_playing:
    another_card = input(f"Do you want to draw another card? please type yes or no: ")
    if another_card == "yes":
      user_cards.append(deal_card())
      print(f" User cards: {user_cards}")
      if sum(user_cards) == 21 or sum(user_cards) > 21:
        print(f"Game over!")
        still_playing = False
    else:
      compare(computer_cards, user_cards)
      still_playing = False


calculate_score()



