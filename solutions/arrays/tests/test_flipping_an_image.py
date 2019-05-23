#! /usr/bin/env python

from .. import flipping_an_image


def test_flip_and_invert_image():
    sample_inputs_and_expected_answers = (
        (
            [[1, 1, 0], [1, 0, 1], [0, 0, 0]],
            [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        ),
        (
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        )
    )
    for image, expected in sample_inputs_and_expected_answers:
        assert flipping_an_image.flip_and_invert_image(image) == expected
