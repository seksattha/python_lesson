def playing_card():
    suits = ("\u2660", "\u2665", "\u2666", "\u2663")
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(suit + rank)

    return deck

if __name__ == '__main__':
    print(playing_card())
