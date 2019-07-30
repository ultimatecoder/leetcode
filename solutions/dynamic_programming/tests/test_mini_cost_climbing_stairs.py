#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..mini_cost_climbing_stairs import find_minimum_cost_to_climb_stairs


def test_find_minimum_cost_to_climb_stairs():
    sample_cost_and_expected_answers = (
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 0], 0)
    )

    for cost_of_steps, expected_cost in sample_cost_and_expected_answers:
        assert find_minimum_cost_to_climb_stairs(
            cost_of_steps
        ) == expected_cost
