#! /usr/bin/env python

from ..evaluate_reverse_polish_notation import evaluate

def test_evaluate():
    sample_inputs = (
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (
            [
                "10", "6", "9", "3", "+", "-11", "*",
                "/", "*", "17", "+", "5", "+"
            ],
            22
        ),
        ([], 0),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "5", "+"], 5)
    )
    for expression, expected_answer in sample_inputs:
        assert evaluate(expression) == expected_answer
