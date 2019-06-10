#! /usr/bin/env python

from ..flood_fill import replace


def test_replace():
    sample_inputs = (
        (
            [
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 1]
            ],
            (1, 1),
            2,
            [
                [2, 2, 2],
                [2, 2, 0],
                [2, 0, 1]
            ]
        ),
        (
            [
                [1]
            ],
            (0, 0),
            550,
            [
                [550]
            ]
        ),
        (
            [
                [0, 67000, 67000],
                [540, 0, 67000],
            ],
            (1, 1),
            67000,
            [
                [0, 67000, 67000],
                [540, 67000, 67000],
            ]
        ),
        (
            [
                [0, 0, 9],
                [540, 0, 67000],
                [0, 0, 9],
                [540, 0, 67000],
            ],
            (0, 1),
            0,
            [
                [0, 0, 9],
                [540, 0, 67000],
                [0, 0, 9],
                [540, 0, 67000],
            ]
        )
    )
    for image, pixel, color, expected_image in sample_inputs:
        assert replace(image, pixel, color) == expected_image
