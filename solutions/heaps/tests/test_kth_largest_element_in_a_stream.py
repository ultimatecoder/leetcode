#! /usr/bin/env python

from ..kth_largest_element_in_a_stream import KthLargest


def test_kth_largest_element_with_sample_scenarios():
    sample_inputs = (
        (
            3, [4, 5, 8, 2], ((3, 4), (5, 5), (10, 5), (9, 8), (4, 8))
        ),
        (
            5, [4, 2, 4], ((2, 2), (4, 2), (5, 2), (1, 2))
        ),
        (
            1, [], ((4, 4), (2, 4), (1, 4), (4, 4), (5, 5))
        )
    )

    for k, numbers, sequence in sample_inputs:
        kth_largest = KthLargest(k, numbers)
        for number_to_add, expected_kth_largest_number in sequence:
            kth_largest_number = kth_largest.add(number_to_add)
            assert kth_largest_number == expected_kth_largest_number

