#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem

    On a staircase, the 'i'-th step has some non-negative cost 'cost[i]'
    assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps. You need to
    find minimum cost to reach the top of the floor, and you can either start
    from the step with index 0, or the step with index 1.

Example 1

    Input

        cost = [10, 15, 20]

    Output

        15

    Explanation

        Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:

    Input

        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    Output

        6

    Explanation

        Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note

    1. 'coost' will have a length in the range [2, 1000].
    2. Every 'cost[i]' will be an integer in the range [0, 999].
"""

from typing import Dict, List, Union


def _find_chepeast_cost(
    step_index: int, cost_of_each_steps: List[int], cache=Dict
):
    try:
        return cache[step_index]
    except KeyError:
        if step_index == len(cost_of_each_steps):
            return 0
        if step_index == (len(cost_of_each_steps) - 1):
            return cost_of_each_steps[step_index]
        cost_with_one_steps = _find_chepeast_cost(
            step_index + 1, cost_of_each_steps, cache
        )
        cost_with_two_steps = _find_chepeast_cost(
            step_index + 2, cost_of_each_steps, cache
        )
        result = cost_of_each_steps[step_index] + min(
            cost_with_one_steps, cost_with_two_steps
        )
        cache[step_index] = result
        return result


def find_minimum_cost_to_climb_stairs(cost_of_each_steps: List[int]) -> int:
    """Finds minimum cost to climb stairs

    This function first calculates a cost to reach top of stair case either by
    taking one step or two steps from first step. After summing a cost of each
    climed step, this function finds a minimum total cost to reach at top of
    stair case. This function do not remember a combination of steps taken to
    reach at top of a stair case.

    This function starts calulation process from 0th step and 1st step. It is
    assumed that given stair case is two steps long.
    """
    cache:Dict = {}
    return min(
        _find_chepeast_cost(
            step_index=0, cost_of_each_steps=cost_of_each_steps, cache=cache
        ),
        _find_chepeast_cost(
            step_index=1, cost_of_each_steps=cost_of_each_steps, cache=cache
        )
    )
