#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..unique_paths import count_unique_paths_from_top_left_to_bottom_right


def test_count_unique_paths_from_top_left_to_bottom_right():
    sample_inputs = (
        (0, 0, 0),
        (1, 1, 1),
        (3, 2, 3),
        (7, 3, 28),
    )
    for total_rows, total_columns, expected_paths in sample_inputs:
        assert count_unique_paths_from_top_left_to_bottom_right(
            total_rows, total_columns
        ) == expected_paths
