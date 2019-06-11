#! /usr/bin/env python

from ..network_delay_time import find_network_delay_time


def test_network_delay_time():
    sample_inputs = (
        (
            [(2, 1, 1), (2, 3, 1), (3, 4, 1)],
            4,
            2,
            2
        ),
        (
            [(1, 1, 0)],
            1,
            1,
            None
        ),
        (
            [(2, 1, 0), (1, 2, 1)],
            3,
            1,
            None
        )
    )
    for metric, number_of_nodes, source, expected_answer in sample_inputs:
        assert find_network_delay_time(
            metric, number_of_nodes, source
        ) == expected_answer
