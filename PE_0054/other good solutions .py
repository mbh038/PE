# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:29:51 2016
@author: mbh
"""
#from Safassthin
hands = [line.split() for line in open("p054_poker.txt")]
def euler54():
    """
    Medley of Kutta, eske and Paul Crowley's code.
    KW. Diederich added a few corrections for 'real world' poker
    (but unrequired in the problem, it seems):
        - Straight (3,1,2) and Flush (3,1,3) have to be ranked :
                - above three of a kind (3,1,1)
                - below full house (3,2)
        - Ace,2,3,4,5 is also straight according to the rules.
    """
    values = {c: v for v, c in enumerate('23456789TJQKA', start=2)}
    def rank(hand):
        """
        Reduce the hand to a compact form that can be directly compared to another.
        The score (or ranking) of a hand is essentially the count of same cards, in
        descending order - for example three of a kind scores (3,1,1), a double pair
        scores (2,2,1). Full House will score (3,2).
        We attribute (3,1,3) to a Flush, and (3,1,2) to a Straight.
        The next ranking value are the cards values themselves.
        """
        cards, colors = zip(*hand)
        cards = [values[c] for c in cards]
        score, cards = zip(*sorted([(cards.count(c), c) for c in set(cards)], reverse=True))

        # Handle some special cases (flush, straight...)
        if len(cards) == 5:
            flush = (len(set(colors)) == 1)
            if cards == (14,5,4,3,2):  # this is the 'Ace' type of straight
                straight = 1; cards = (5,4,3,2,1)
            else:
                straight = (cards[0]-cards[4] == 4)
            score = (((1,), (3,1,3)), ((3,1,2), (5,)))[straight][flush]
        return (score, cards)

    player1, player2 = slice(0, 5), slice(5, 10)
    return sum((rank(hand[player1]) > rank(hand[player2])) for hand in hands)

#from marcus.obi
import itertools
from collections import Counter
from operator import itemgetter

def rank(cards):
    sorted_cards = sorted(card.value for card in cards)
    histogram = Counter(sorted_cards)
    highcards = list(map(itemgetter(1), sorted(((v, k) for k, v in histogram.items()), reverse=True)))
    is_flush = len(set(card.color for card in cards)) == 1
    is_straight = list(histogram.values()).count(1) == 5 and sorted_cards[-1] - sorted_cards[0] == 4
    n_pairs = sum(1 for k, v in histogram.items() if v == 2)
    return (-[
        is_straight and is_flush,
        4 in histogram.values(),
        3 in histogram.values() and n_pairs == 1,
        is_flush,
        is_straight,
        3 in histogram.values(),
        n_pairs == 2,
        n_pairs == 1,
        True
    ].index(True),) + tuple(highcards)

lookup = list(map(str, range(10))) + list("TJQKA")
class Card(object):
    def __init__(self, s):
        self.value = lookup.index(s[0])
        self.color = s[1] # one char of "CDHS"

def solve():
    filename = "p054_poker.txt"
    hands = []
    with open(filename) as f:
        for line in f.readlines():
            cards = [Card(s) for s in line.split()]
            hands.append([cards[:5], cards[5:]])
    print(sum(rank(player1_hand) > rank(player2_hand) for player1_hand, player2_hand in hands))

def main():
    import time
    start = time.time()
    solve()
    end = time.time()
    elapsed = end - start
    print("elapsed: {:.1f} ms".format(elapsed * 1000))

