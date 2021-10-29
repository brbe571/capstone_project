import random
from art import logo 

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if computer_score == user_score:
    return "It's a draw"
  elif computer_score == 0:
    return "Computer has blackjack, bad luck!"
  elif user_score == 0:
    return "User has blackjack you win!"
  elif user_score > 21:
    return "You went over 21 lose"
  elif computer_score > 21:
    return "Opponent went over, you win"
  elif computer_score > user_score:
    return "The computer won"
  elif user_score > computer_score:
    return "User won"
  else:
    return "error"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      another_card = input(f"Do you want to draw another card? please type y or n: ")
      if another_card == "y":
        user_cards.append(deal_card())
        print(f" User cards: {user_cards}")
      else:
        is_game_over = True


  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()



