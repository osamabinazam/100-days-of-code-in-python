


######### Black Jack Rules ##########

# 1. The deck is unlimited
# 2. There are no jokers
# 4. The Jack/Queen/King  all count as 10
# 5. The Ace count as 11 or 1
# 6. Below list is representing deck of cards
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# 7. Cards are not removed from the deck as they are drawn
# 8. Equal probability of drawn

import random
import  os


def logo():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    print(logo)
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

# Calculate function that take list of cards as input and return the score
def calculate_score (cards):
    # if 11 in cards and 10 in cards and len(cards)==2:
    # check for a black jack (a hand with only two cards: Ace+(Jack/Queen/King)) and return 0 instead of actual score
    if sum(cards) ==21 and len(cards) ==2:
        return 0

    # checking for an ace and selecting its value according to condition or score
    # if score is already over 21 then remove 11 and replace it with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# Assign card to dealer and computer. 2 card each using deal_card()

# Compare score and return appropriate result
def compare_score(user_score , computer_score):
   if user_score == computer_score:
       return "It's a tie"
   elif computer_score==0:
       return "You lose, opponent has BlackJack"
   elif user_score==0:
       return "You win with a BlackJack"
   elif user_score >21:
       return  "You lose, went beyond 21"
   elif computer_score >21:
       return "You win,opponent went beyond 21"
   elif user_score > computer_score:
       return "You win"
   elif user_score < computer_score:
       return "You lose"

def BlackJack():
    # lists represent user and computer cards
    user_cards = []
    computer_cards = []
    is_game_end = False

    # Drawing cards from the deck of 52 cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # keep track of game state untill game end
    while not is_game_end:
        # Calling calculate score. if computer or a user has blackjack or score is over 21
        user_score = int (calculate_score(user_cards))
        computer_score = int (calculate_score(computer_cards))
        print(f"Your cards: {user_cards} ,Current score: {user_score}")

        if user_score ==0 or computer_score==0 and user_cards>21:
            is_game_end = True
        else :
            # Ask Users if they want to draw a new card
            card_draw = input("Do you want to get another card ? Type Y/y and Type N/n to pass : " )
            if card_draw in ["y","Y"]:
                user_cards.append(deal_card())
            else:
                is_game_end = True

    # Once user is done. it's time to let computer play
    # The computer should keep drawing card until it has score less than 17
    while computer_score ==0 or computer_score <17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n")
    print(f"Your cards are : {user_cards}")
    print(f"Your Final Score is : {user_score}")
    print(f"Computer's cards are : {computer_cards}")
    print(f"Computer's Final Score is : {computer_score}")
    print(compare_score(user_score,computer_score))

if __name__ == '__main__':
    logo()
    BlackJack()
    while True:
        print("\nDo you want to play again ? Type Y/y and Type N/n to Quit the Game")
        if input() in ['y','Y']:
            os.system('clear')
            logo()
            BlackJack()
        else:
            exit(0)


