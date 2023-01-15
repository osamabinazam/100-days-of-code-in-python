


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
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

# Assign card to dealer and computer. 2 card each using deal_card()
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


# Calculate function that take list of cards as input and return the score
def create_score (cards):
    return sum(cards)



