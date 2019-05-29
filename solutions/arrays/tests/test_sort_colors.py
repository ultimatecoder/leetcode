#! /usr/bin/env python

from ..sort_colors import sort


def test_sort():
    sample_colors = (
        [2, 0, 2, 1, 1, 0],
        [1, 0, 1],
        [1, 2, 1],
        [0],
        [2, 0],
        []
    )

    for colors in sample_colors:
        expected_colors = colors[:]
        expected_colors.sort()
        sort(colors)
        assert colors == expected_colors
