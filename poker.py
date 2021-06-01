#Jalen Tacsiat
#Project
#Implementation of a Poker effective hand stregth algorithm
#Playing Texas Hold Em poker
import math
import numpy as np
import random
import itertools


def create_deck():
    values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ["spade", "clubs", "diamonds", "hearts"]
    playing_deck = []
    for value in values:
        for suit in suits:
            playing_deck.append((value, suit))
    return playing_deck

def create_river(playing_deck):
    river = []
    for playing_card in range (0, 3):
        river.append(playing_deck.pop())
    return river

def create_hand(playing_deck):
    hand = []
    for card_hand in range (0, 2):
        hand.append(playing_deck.pop())
    return hand

#creates all 2 card hand combinations from a remaining deck
def create_2_card_hand_combinations(playing_deck):
    len(playing_deck)
    hands = []
    hands.extend(itertools.combinations(playing_deck, 2))
    hands = [list(x) for x in hands]
    return hands
