import random

# toss = ["heads", "tails"]

# result = random.choice(toss)

# print(result)

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

result_suit = random.choice(suits)
result_card = random.choice(ranks)

print(f"The card assigned to you is {result_card} of {result_suit}")