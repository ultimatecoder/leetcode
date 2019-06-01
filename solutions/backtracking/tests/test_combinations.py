#! /usr/bin/env python

from itertools import combinations

from ..combinations import construct_combinations


def test_construct_combinations():
    sample_inputs = (
        (4, 2),
        (0, 0),
        (4, 0),
        (5, 2),
        (1, 1),
        (1, 2),
        (5, 3),
        (5, 2),
    )
    for maximum_number_of_set, length_of_combinations in sample_inputs:
        _expected_combinations = combinations(
            range(1, maximum_number_of_set + 1),
            length_of_combinations
        )
        computed_combinations = construct_combinations(
            maximum_number_of_set,
            length_of_combinations
        )
        expected_combinations = []
        for index, expected_combination in enumerate(_expected_combinations):
            expected_combinations.append(list(expected_combination))
        assert expected_combinations == computed_combinations
