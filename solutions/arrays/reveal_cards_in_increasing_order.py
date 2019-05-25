#! /usr/bin/env python
"""
Problem

    In a deck of cards, every card has a unique integer. You can order the deck
    in any order you want.

    Initially, all the cards start face down (unrevealed) in one deck.

    Now, you do the following steps repeatedly, unitl all cards are revealed:
        1. Take the top card of the deck, reveal it, and take it out of the
           deck.
        2. If there are still cards in the deck, put the next top card of the
           deck at the bottom of the deck.
        3. If there are still unrevealed cards, go back to step 1. Otherwise,
           stop.

    Return an ordering of the deck that would reveal the cards in increasing
    order.

    The first entry in the answer is considered to be the top of the deck.

Example 1

    Input

        [17, 13, 11, 2, 3, 5, 7]

    Output

        [2, 13, 3, 11, 5, 17, 7]

    Explanation

        We get the deck in the order [17, 13, 11, 2, 3, 5, 7] (this order
        doesn't matter) and reorder it.

        After reordering, the deck starts as [2, 13, 3, 11, 5, 17, 7], where 2
        is the top of the deck.

        We reveal 2, and move 13 to the bottom. The deck is now
        [3, 11, 5, 17, 7, 13].

        We reveal 3, and move 11 to the bottom. The deck is now
        [5, 17, 7, 13, 11].

        We reveal 5, and move 17 to the bottom. The deck is now
        [7, 13, 11, 17].

        We reveal 7, and move 13 to the bottom. The deck is now [11, 17, 13].

        We reveal 11, and move 17 to the bottom. The deck is now [13, 17].

        We reveal 13, and move 17 to the bottom. The deck is now [17].

        Since all the cards revealed are in increasing order, the answer is
        correct.

Note

    1. 1 <= A.length <= 1000
    2. 1 <= A[i] <= 10^6
    3. A[i] != A[j] for all i != j

Link

    https://leetcode.com/problems/reveal-cards-in-increasing-order/
"""
from typing import List


def _merge_sort(elements: List, start_index: int, end_index: int) -> List:
    middle_index = (start_index + end_index) // 2
    if (start_index != end_index):
        _merge_sort(
            elements, start_index=start_index, end_index=middle_index
        )
        _merge_sort(
            elements, start_index=middle_index + 1, end_index=end_index
        )
    return _merge(elements, start_index, end_index)


def _merge(elements: List, start_index: int, end_index: int) -> List:
    middle_index = (start_index + end_index) // 2
    left = elements[start_index:middle_index+1]
    right = elements[middle_index+1:end_index+1]
    left_index = 0
    right_index = 0
    for index in range(start_index, end_index+1):
        if (
            (right_index >= len(right)) or
            (left_index < len(left)) and (left[left_index] < right[right_index])
        ):
            elements[index] = left[left_index]
            left_index += 1
        else:
            elements[index] = right[right_index]
            right_index += 1
    return elements


def arrange_deck(deck: List[int]) -> List[int]:
    """Arranges the given deck in special order

    This method will arrange a given deck in a special order. If top number is
    revealed and next card is put on the bottom of the deck then all cards will
    reveal in increasing order.

    Assume a deck arranged as 3, 4, 1, 5 will be sorted as 1, 4, 3, 5 to follow
    below steps yet the cards reveals in a sorted order.

    1. Take the top card of the deck, reveal it, and take it out of the
        deck.
    2. If there are still cards in the deck, put the next top card of the
        deck at the bottom of the deck.
    3. If there are still unrevealed cards, go back to step 1. Otherwise,
        stop.

    Example
        >>>arrange_deck([3, 4, 1, 5]) == [1, 4, 3, 5]

    Time complexity: O(n * log n)
    Space complexity: O(n)
    """
    deck = _merge_sort(deck, 0, len(deck) - 1)
    sorted_deck = [0] * len(deck)
    sequence_indexes = list(range(len(deck)))
    for card in deck:
        index = sequence_indexes.pop(0)
        sorted_deck[index] = card
        try:
            next_card_index = sequence_indexes.pop(0)
            sequence_indexes.append(next_card_index)
        except IndexError:
            return sorted_deck
    return sorted_deck
