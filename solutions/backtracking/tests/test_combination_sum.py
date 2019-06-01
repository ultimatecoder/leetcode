#! /usr/bin/env python

from ..combination_sum import combinations


def test_combinations():
    sample_inputs = (
        ((2, 3, 6, 7), 7, [[2, 2, 3], [7]]),
        ((2, 3, 5), 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ((4, 5, 1), 0, [[]]),
        ((1, 2), 1, [[1]]),
        ((), 3, [])
    )
    for numbers, expected_sum, expected_answer in sample_inputs:
        assert combinations(numbers, expected_sum) == expected_answer
