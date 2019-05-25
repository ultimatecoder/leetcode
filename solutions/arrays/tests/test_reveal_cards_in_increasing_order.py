#! /usr/bin/env python

from .. import reveal_cards_in_increasing_order


def test_arrange_deck():
    assert reveal_cards_in_increasing_order.arrange_deck(
        [17, 13, 11, 2, 3, 5, 7]
    ) == [2, 13, 3, 11, 5, 17, 7]
