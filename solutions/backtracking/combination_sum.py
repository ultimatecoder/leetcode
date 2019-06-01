#! /usr/bin/env python
"""
Problem

    Given a set of candidate numbers (candidates) (without duplicates) and a
    target number (target), fund all unique combinations in candidates where
    the candidate numbers sums to target.

    the same repeated number may be chosen from candidates unlimited number of
    times.

Note

    * All numbers(including target) will be positive integers.
    * The solution set must not contain duplicate combinations.

Example 1

    Input

        candidates = [2, 3, 6, 7], target = 7

    Output

        [
            [7],
            [2, 2, 3]
        ]

Example 2

    Input

        candidates = [2, 3, 5], target = 8

    Output

        [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ]
"""
from typing import List, Set


Vector = List[int]
Numbers = List[int]
Combinations = List[List[int]]


def _compute_combinations(
    combinations_vector: Vector, index: int, expected_sum: int,
    numbers: Numbers
):
    if expected_sum == 0:
        return [combinations_vector[: index + 1]]
    elif expected_sum < 0:
        return []
    index += 1
    combinations: List = []
    for number in range(len(numbers)):
        try:
            combinations_vector[index] = numbers[number]
        except IndexError:
            combinations_vector.append(numbers[number])
        expected_sum -= numbers[number]
        past_combinations = _compute_combinations(
            combinations_vector,
            index,
            expected_sum,
            numbers=numbers[number:]
        )
        expected_sum += numbers[number]
        if past_combinations:
            combinations.extend(past_combinations)
    return combinations


def combinations(numbers: Numbers, expected_sum: int) -> Combinations:
    """Computes combinations whose sum is equal to expected sum

    First this method prepares all possible combinations from a set of given
    numbers. Then this method collects combination of given pair which is equal
    to a expected sum, once all combinations are checked this method returns
    all collected pairs as a result.

    This method can choose any element from a given set of numbers more than
    one time.
    """
    combinations_vector: List = []
    index = -1
    return _compute_combinations(
        combinations_vector,
        index,
        expected_sum,
        numbers,
    )
