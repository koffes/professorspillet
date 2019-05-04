import cards
import copy
from tkinter import Tk
from tkinter import Canvas

TRNG_N = [50, 50, 0, 0, 100, 0, 50, 50]
TRNG_E = [50, 50, 100, 0, 100, 100, 50, 50]
TRNG_S = [50, 50, 100, 100, 0, 100, 50, 50]
TRNG_W = [50, 50, 0, 100, 0, 0, 50, 50]


class Draw:
    def deck(deck):
        root = Tk()
        canvas = Canvas(width=800, height=800, bg='white')
        canvas.pack()
        canvas.create_polygon(TRNG_N, fill='red')
        canvas.create_polygon(TRNG_E, fill='blue')
        canvas.create_polygon(TRNG_S, fill='green')
        canvas.create_polygon(TRNG_W, fill='yellow')
        root.mainloop()

        i = 0
        for card in deck.cards:
            for side in card.sides:
                print('side {}'.format(i))
                i = i + 1


class Side:
    def __init__(self, color, bdyprt):
        self.color = color
        self.bdyprt = bdyprt


class Card:
    def __init__(self, sides):
        if len(sides) != cards.SIDE_NUM:
            raise ValueError('The number of card sides is incorrect')

        self.sides = copy.deepcopy(sides)
        for side in self.sides:
            print('{}'.format(side.color))

    def get_side(self, i):
        return self.sides[i]


class Deck:
    def __init__(self, init_deck):
        if len(init_deck) != cards.CARDS_NUM:
            raise ValueError('The number of card in deck is incorrect')

        self.cards = []
        for card in range(len(init_deck)):
            print(card)
            sides = []
            for side in range(len(init_deck[0])):
                sides.append(Side(init_deck[card][side][0],
                                  init_deck[card][side][1]))
            self.cards.append(Card(sides))

    def get_card(self, i):
        return self.cards[i]


print('running prog')
deck = Deck(cards.DECK)
Draw.deck(deck)
