"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card == "A":
        return 1
    elif card in ["J", "Q", "K"]:
        return 10
    else:
        return int(card)


def higher_card(card_one, card_two):
    A = value_of_card(card_one)
    B = value_of_card(card_two)
    if (A > B):
        return card_one
    elif (B > A):
        return card_two
    else:
        return card_one,card_two
    
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """


def value_of_ace(card_one, card_two):
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    if (card_one == "A"):
        one = 11
    elif (card_two == "A"):
        two = 11
    total = one + two
    if (total <= 10):
        return 11
    else:
        return 1
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """


def is_blackjack(card_one, card_two):
    if (card_one == "A" and card_two in ["10","K","Q","J"]):
        return True
    elif (card_one in ["10","K","Q","J"] and card_two == "A"):
        return True
    else:
        return False

 
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """


def can_split_pairs(card_one, card_two):
    ten_cards = ["10", "K", "Q", "J"]
    return (card_one == card_two) or (card_one in ten_cards and card_two in ten_cards)

    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

def can_double_down(card_one, card_two):
    A = value_of_card(card_one)
    B = value_of_card(card_two)
    Total = A + B
    if (Total in [9,10,11]):
        return True
    else:
        return False
    
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
