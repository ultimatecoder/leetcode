#! /usr/bin/env python

from .. import sort_array_by_parity_ii


def test_even():
    sample_inputs_and_expected_answers = (
        (12, True),
        (13, False),
        (1, False),
        (0, True)
    )

    for number, expected_answer in sample_inputs_and_expected_answers:
        assert sort_array_by_parity_ii.is_even(number) == expected_answer


def test_sort_by_parity():
    sample_inputs_and_expected_outputs = (
        ([4, 2, 5, 7], [4, 5, 2, 7]),
        ([3, 4], [4, 3]),
        ([888, 505, 627, 486], [888, 505, 486, 627]),
        ([5, 7, 9, 2, 4, 6], [2, 5, 4, 7, 6, 9])
    )
    for elements, expected_output in sample_inputs_and_expected_outputs:
        assert sort_array_by_parity_ii.sort_by_parity(elements) == (
            expected_output
        )
