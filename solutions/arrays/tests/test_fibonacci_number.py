#! /usr/bin/env python

from .. import fibonacci_number


def test_fibonacci():
    sample_inputs_and_expected_answers = (
        (0, 0),
        (1, 1),
        (3, 2),
        (4, 3)
    )

    for number, expected_answer in sample_inputs_and_expected_answers:
        assert fibonacci_number.fibonacci(number) == expected_answer
