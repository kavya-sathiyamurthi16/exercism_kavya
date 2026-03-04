"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number,number+1,number+2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2

def list_contains_round(rounds, number):
    for i in rounds:
        if i==number:
           return True
    return False
def card_average(hand):
    return float((sum(hand))/len(hand))


def approx_average_is_average(hand):
    avg_num=(hand[0]+hand[-1])/2
    mid=len(hand)//2
    act=(sum(hand))/len(hand)
    if avg_num==act or hand[mid]==act :
        return True
    return False


def average_even_is_average_odd(hand):
    odd=hand[1::2]
    even=hand[0::2]
    even_avg=sum(even)/len(even)
    odd_avg=sum(odd)/len(odd)
    if even_avg==odd_avg:
        return True
    return False


def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]=11*2
        return hand
    return hand