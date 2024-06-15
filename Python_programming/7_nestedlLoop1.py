def playing_card():
    suit = ("\u2660","\u2665","\u2666","\u2663")
    rank = list("123456789") +["10"] + list("JQK")

    deck = []
    for i in suit:
        for j in rank:
            deck.append(i + j)

    return deck

if __name__ == '__main__':
    print(playing_card())