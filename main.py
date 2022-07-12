# Problem 54:
#     Poker Hands
#
# Description:
#     In the card game poker, a hand consists of five cards and are ranked,
#       from lowest to highest, in the following way:
#         * High Card:          Highest value card.
#         * One Pair:           Two cards of the same value.
#         * Two Pairs:          Two different pairs.
#         * Three of a Kind:    Three cards of the same value.
#         * Straight:           All cards are consecutive values.
#         * Flush:              All cards of the same suit.
#         * Full House:         Three of a kind and a pair.
#         * Four of a Kind:     Four cards of the same value.
#         * Straight Flush:     All cards are consecutive values of same suit.
#         * Royal Flush:        Ten, Jack, Queen, King, Ace, in same suit.
#
#     The cards are valued in the order:
#         2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
#     If two players have the same ranked hands then the rank made up of the highest value wins;
#       for example, a pair of eights beats a pair of fives (see example 1 below).
#     But if two ranks tie, for example, both players have a pair of queens,
#       then highest cards in each hand are compared (see example 4 below);
#       if the highest cards tie then the next highest cards are compared, and so on.
#
#     Consider the following five hands dealt to two players:
#
#         |======|===================|=====================|==========|
#         | Hand |     Player 1      |      Player 2       |  Winner  |
#         |======|===================|=====================|==========|
#         |  1   |  5H 5C 6S 7S KD   |   2C 3S 8S 8D TD    | Player 2 |
#         |      |   Pair of Fives   |   Pair of Eights    |          |
#         |------|-------------------|---------------------|----------|
#         |  2   |  5D 8C 9S JS AC   |   2C 5C 7D 8S QH    | Player 1 |
#         |      | Highest card Ace  | Highest card Queen  |          |
#         |------|-------------------|---------------------|----------|
#         |  3   |  2D 9C AS AH AC   |   3D 6D 7D TD QD    | Player 2 |
#         |      |    Three Aces     | Flush with Diamonds |          |
#         |------|-------------------|---------------------|----------|
#         |  4   |  4D 6S 9H QH QC   |   3D 6D 7H QD QS    | Player 1 |
#         |      |  Pair of Queens   |   Pair of Queens    |          |
#         |      | Highest card Nine | Highest card Seven  |          |
#         |------|-------------------|---------------------|----------|
#         |  5   |  2H 2D 4C 4D 4S   |   3C 3D 3S 9S 9D    | Player 1 |
#         |      |    Full House     |     Full House      |          |
#         |      | With Three Fours  |  with Three Threes  |          |
#         |======|===================|=====================|==========|
#
#     The file, poker.txt, contains one-thousand random hands dealt to two players.
#     Each line of the file contains ten cards (separated by a single space):
#       the first five are Player 1's cards and the last five are Player 2's cards.
#     You can assume that all hands are valid (no invalid characters or repeated cards),
#       each player's hand is in no specific order,
#       and in each hand there is a clear winner.
#
#     How many hands does Player 1 win?

from collections import defaultdict
from typing import List, Tuple

# Possible suits for an individual card (clover, diamond, heart, spade)
CARD_SUITS = {'C', 'D', 'H', 'S'}

# Mapping of an individual card's rank to an int which captures the ranking between cards
CARD_RANK_TO_INT = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def card_to_tuple(c: str) -> Tuple[str, int]:
    """
    Converts the string representation of a card to a tuple.

    Args:
        c (str): Length-2 string representing a playing card in poker

    Returns:
        (Tuple[str, int]):
          Tuple of:
            * (str) Card's suit as one of {'C', 'D', 'H', 'S'}
            * (int) Card's rank as an int in range [2, 14]

    Raises:
        AssertError: if incorrect args are given
        KeyError:    if card has invalid rank
    """
    assert type(c) == str and len(c) == 2

    global CARD_SUITS
    suit = c[1]
    assert suit in CARD_SUITS

    global CARD_RANK_TO_INT
    rank = CARD_RANK_TO_INT[c[0]]

    return suit, rank


def hand_freqs(hand: List[Tuple[str, int]]) -> List[int]:
    """
    Returns a list of the ordered frequencies of the card ranks in `hand`.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (List[int]): Ordered frequencies of the card ranks in `hand`
    """
    rank_to_freq = defaultdict(lambda: 0)
    for _, r in hand:
        rank_to_freq[r] += 1
    freqs = list(rank_to_freq.values())
    freqs.sort()
    return freqs


def is_four_of_a_kind(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a four-of-a-kind in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a four-of-a-kind
    """
    return hand_freqs(hand) == [1, 4]


def is_full_house(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a full house in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a full house
    """
    return hand_freqs(hand) == [2, 3]


def is_three_of_a_kind(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a three-of-a-kind in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a three-of-a-kind
    """
    return hand_freqs(hand) == [1, 1, 3]


def is_two_pair(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a two-pair in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a two-pair
    """
    return hand_freqs(hand) == [1, 2, 2]


def is_one_pair(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a one-pair in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a one-pair
    """
    return hand_freqs(hand) == [1, 1, 1, 2]


def is_straight(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a straight in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a straight
    """
    ranks = set(map(lambda c: c[1], hand))
    rank_lo = min(ranks)
    rank_hi = max(ranks)
    return (rank_hi - rank_lo) == 4 and len(ranks) == 5


def is_flush(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a flush in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is flush
    """
    suits = set(map(lambda c: c[0], hand))
    return len(suits) == 1


def is_straight_flush(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a straight flush in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a royal flush
    """
    return is_straight(hand) and is_flush(hand)


def is_royal_flush(hand: List[Tuple[str, int]]) -> bool:
    """
    Returns True iff given `hand` is a royal flush in poker.
    Assumes hand is represented properly as list of tuples.

    Args:
        hand (List[Tuple[str, int]]): List of cards represented as tuples of str/int

    Returns:
        (bool): True iff `hand` is a royal flush
    """
    return is_straight_flush(hand) and max(map(lambda c: c[1], hand)) == CARD_RANK_TO_INT['A']


def poker_hand_rank(hand: List[Tuple[str, int]]) -> List[int]:
    """
    Returns the 'rank' of the given poker hand as an int list
      with which two different hands can be compared lexicographically.

    Args:
        hand (List[Tuple[str, int]]): List of 5 cards represented as tuples of str/int

    Returns:
        (List[int]): Rank of given poker hand which can be used for lexicographic comparison

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(hand) == list and len(hand) == 5 \
           and all([type(c) == tuple and type(c[0]) == str and type(c[1]) == int for c in hand])

    # Idea:
    #     The 'major' categorization of a hand (flush, straight, full house, etc.)
    #       is first represented by the 'major_rank', which is an int.
    #     Then if ties are possible, the full hand is further ranked by considering other elements.
    #     For example, if two hands had full houses,
    #       then they would be compared based on what numbers were in the hand,
    #       so those numbers are tacked onto the overall hand's rank to be used for comparison.
    #     Do this by iteratively checking whether the given hand fits a certain rank,
    #       from best to worst rank.

    major_rank = 10

    # Royal Flush
    if is_royal_flush(hand):
        return [major_rank]
    else:
        major_rank -= 1

    # Straight Flush
    if is_straight_flush(hand):
        # Only need the highest rank for tie-breaking since card ranks are consecutive anyway
        rank_hi = max(map(lambda c: c[1], hand))
        return [major_rank, rank_hi]
    else:
        major_rank -= 1

    # Four of a Kind
    if is_four_of_a_kind(hand):
        # Possible to tie with 4-of-a-kind, but not with same rank,
        #   so use that rank for tie-breaking if needed
        ranks = list(map(lambda c: c[1], hand))
        rank_set = set(ranks)
        rank = rank_set.pop()
        rank_tiebreak = rank if ranks.count(rank) == 4 else rank_set.pop()
        return [major_rank, rank_tiebreak]
    else:
        major_rank -= 1

    # Full House
    if is_full_house(hand):
        # Possible to tie with full house,
        #   but not with same rank occurring 3 times
        #   so use that rank for tie-breaking if needed
        ranks = list(map(lambda c: c[1], hand))
        rank_set = set(ranks)
        rank = rank_set.pop()
        rank_tiebreak = rank if ranks.count(rank) == 3 else rank_set.pop()
        return [major_rank, rank_tiebreak]
    else:
        major_rank -= 1

    # Flush
    if is_flush(hand):
        # Tack on all card ranks for tie-breaking
        ranks = list(map(lambda c: c[1], hand))
        ranks.sort(reverse=True)
        return [major_rank] + ranks
    else:
        major_rank -= 1

    # Straight
    if is_straight(hand):
        # Only need the highest rank for tie-breaking since card ranks are consecutive anyway
        rank_hi = max(map(lambda c: c[1], hand))
        return [major_rank, rank_hi]
    else:
        major_rank -= 1

    # Three of a Kind
    if is_three_of_a_kind(hand):
        # Possible to tie with 3-of-a-kind,
        #   but not with same rank occurring 3 times
        #   so use that rank for tie-breaking if needed
        ranks = list(map(lambda c: c[1], hand))
        rank_set = set(ranks)
        rank_tiebreak = None
        while len(rank_set) > 0:
            rank = rank_set.pop()
            if ranks.count(rank) == 3:
                rank_tiebreak = rank
                break
            else:
                continue
        return [major_rank, rank_tiebreak]
    else:
        major_rank -= 1

    # Two Pairs
    if is_two_pair(hand):
        # Use ranks of pairs for tie-breaking,
        #   and then rank of remaining card if needed
        ranks = list(map(lambda c: c[1], hand))
        rank_set = set(ranks)
        rank_tiebreaks = []
        rank_last = None
        while len(rank_set) > 0:
            rank = rank_set.pop()
            if ranks.count(rank) == 2:
                rank_tiebreaks.append(rank)
            else:
                rank_last = rank
                continue
        rank_tiebreaks.sort(reverse=True)
        return [major_rank] + rank_tiebreaks + [rank_last]
    else:
        major_rank -= 1

    # One Pair
    if is_one_pair(hand):
        # Use rank of pair for tie-breaking,
        #   and then use ranks of remaining cards if needed
        ranks = list(map(lambda c: c[1], hand))
        rank_set = set(ranks)
        ranks_last = []
        rank_tiebreak = None
        while len(rank_set) > 0:
            rank = rank_set.pop()
            if ranks.count(rank) == 2:
                rank_tiebreak = rank
            else:
                ranks_last.append(rank)
                continue
        ranks_last.sort(reverse=True)
        return [major_rank, rank_tiebreak] + ranks_last
    else:
        major_rank -= 1

    # High Card
    # Just compare by highest cards
    ranks = list(map(lambda c: c[1], hand))
    ranks.sort(reverse=True)
    return [major_rank] + ranks


def main(filename: str) -> int:
    """
    Returns the number of poker hands won by Player 1 in the given `filename`.

    Args:
        filename (str): File name containing poker hands

    Returns:
        (int): Number of poker hands won by Player 1 in `filename`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(filename) == str

    p1_wins = 0
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            # Parse hands into representation of cards
            all_cards = line.strip().split()
            p1_hand = list(map(card_to_tuple, all_cards[:5]))
            p2_hand = list(map(card_to_tuple, all_cards[5:]))

            # Determine rank each hand
            p1_rank = poker_hand_rank(p1_hand)
            p2_rank = poker_hand_rank(p2_hand)

            # Compare ranks lexicographically
            if p1_rank > p2_rank:
                p1_wins += 1
    return p1_wins


if __name__ == '__main__':
    poker_hands_file_name = 'p054_poker.txt'
    player_1_wins = main(poker_hands_file_name)
    print('Number of poker hands won by Player 1 in file "{}":'.format(poker_hands_file_name))
    print('  {}'.format(player_1_wins))
