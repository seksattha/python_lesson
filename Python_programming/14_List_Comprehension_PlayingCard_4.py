def playingCard():
    #Ordinary foor loop.
    rank = list("A23456789") + ["10"] + list("JQK")
    suit = ("\u2660","\u2665","\u2666","\u2663" )
    deck = []
    for i in rank:
        for j in suit:
            deck.append(i+j)
    print(deck)

def playingCardComp():
    # List comprehension.
    rank = list("A23456789") + ["10"] + list("JQK")
    suit = ("\u2660", "\u2665", "\u2666", "\u2663")
    deck = [ i+ j for i in rank for j in suit]
    # Be Able to store the value in tuple as well.
    deck2 = [(i,j) for i in rank for j in suit]
    print(deck)
    print(deck2)

if __name__ == '__main__':
    playingCardComp()