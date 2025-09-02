import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    start = input("Press Enter to pick a card or Q plus Enter to quit.: ")
    if start == "":
        card = random.choice(diamonds)
        diamonds.remove(card)
        hand.append(card)
        print("Card selected ", card)
        print("This is card in hand ", hand)
        print("Cards remaining on table ", diamonds)
    else:
        start == "q" and ""
        print("Goodbye!")
        break
    if not diamonds:
        print("THere are no more carsd to pick")