#! /usr/bin/env python

from ..combination_sum_ii import combinations


def test_combinations():
    sample_inputs = (
        ([10, 1, 2, 7, 6, 1, 5], 8, [[2, 6], [1, 1, 6], [1, 2, 5], [1, 7]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ([18, 1, 9, 2, 1], 4, [[1, 1, 2]]),
        ([10, 1, 1], 3, []),
        ([], 5, []),
        ([1, 1, 1, 1, 1], 4, [[1, 1, 1, 1]]),
    )
    for numbers, expected_sum, expected_answer in sample_inputs:
        assert combinations(numbers, expected_sum) == expected_answer
