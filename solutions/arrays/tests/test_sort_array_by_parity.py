#! /usr/bin/env python

from .. import sort_array_by_parity


def test_parity_sort():
    assert sort_array_by_parity.parity_sort([3, 1, 2, 4]) == [4, 2, 1, 3]


def test_is_odd():
    sample_numbers_and_expected_answers = (
        (1, True),
        (2, False),
        (10000, False),
        (17, True)
    )
    for number, expected_answer in sample_numbers_and_expected_answers:
        assert sort_array_by_parity.is_odd(number) == expected_answer
