#! /usr/bin/env python

from ..number_of_islands import count_mountains


def test_count_mountains():
    sample_map_with_count_of_mountains = (
        (
            [
                ['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
            ],
            1,
        ),
        (
            [
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1']
            ],
            3
        ),
        (
            [],
            0
        ),
        (
            [
                ['1', '1', '0', '1', '1']
            ],
            2
        )
    )

    for _map, expected_mountains in sample_map_with_count_of_mountains:
        assert count_mountains(_map) == expected_mountains
