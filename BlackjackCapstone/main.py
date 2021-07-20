#function that uses the List below to *return* a random card
import random
from art import logo
#import clear function
import os
clear = lambda: os.system('cls')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#function that takes a list of cards as input and returns the score.
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
#check for a blackjack and return 0 instead of the actual score. 0 will represent a blackjack in my game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
#check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#function passed in the user_score and computer_score
#if the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses
#if the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
#if the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
#if you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

#the score will need to be rechecked with every new card drawn 
    while not is_game_over:
    #if the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
      #if the game has not ended, ask the user if they want to draw another card
      #if yes, then use the deal_card() function to add another card to the user_cards list. If no, then the game has ended
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

  #once the user is done, it's time to let the computer play. The computer will keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

