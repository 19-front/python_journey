import random
# random integer
pips = random.randint(1, 6)
print('You roll the die... it lands with', pips, 'pips showing.')
# random choice
prizes = ['a car', '$1000', 'a pony', '$30']

prize_won = random.choice(prizes)
print('You turn the wheel of fortune.... its lands on a prize of', prize_won, '!!')

# random shuffle
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print('The cards are now in this order: ')
print(cards)