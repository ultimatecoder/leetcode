#! /usr/bin/env python

from .. import squares_of_a_sorted_array


def test_square_sequences():
    sample_inputs = (
        [-3, 0, 2],
        [-4, -3, 0, 1, 3, 10],
        [-7, -3, 2, 3, 11],
        [1, 2, 3, 4, 5],
        [-6, -3, -2, -1],
        []
    )
    for elements in sample_inputs:
        expected_result = sorted([e**2 for e in elements])
        assert squares_of_a_sorted_array.square_sequence(
            elements) == expected_result
