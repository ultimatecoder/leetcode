#! /usr/bin/env python
"""
Problem

    Given two integers 'n' and 'k', return all possible combinations of 'k'
    numbers out of 1 .. n.

Example

    Input

        n = 4, k = 2

    Output

        [
            [2, 4],
            [3, 4],
            [2, 3]
            [1, 2],
            [1, 3],
            [1, 4]
        ]
"""
from typing import List, Union

Combinations = List[List[int]]
Vector = List[bool]


def _process_solutions(
    combinations_vector: Vector,
    maximum_number_of_set: int,
    length_of_combination: int
) -> Combinations:
    combination = []
    for index in range(1, maximum_number_of_set + 1):
        if combinations_vector[index]:
            combination.append(index)
    if len(combination) == length_of_combination:
        return [combination]
    else:
        return []


def _backtrack(
    combinations_vector: Vector,
    maximum_number_of_set: int,
    length_of_combination: int,
    index: int
) -> Combinations:
    if index == maximum_number_of_set:
        return _process_solutions(
            combinations_vector, maximum_number_of_set, length_of_combination
        )

    combinations = []
    index += 1
    for state in [True, False]:
        try:
            combinations_vector[index] = state
        except IndexError:
            combinations_vector.append(state)
        combinations_of_past = _backtrack(
            combinations_vector,
            maximum_number_of_set,
            length_of_combination, index
        )
        if combinations_of_past:
            combinations.extend(combinations_of_past)
    return combinations


def construct_combinations(
    maximum_number_of_set: int, length_of_combination: int
) -> Combinations:
    """Computes all combinations from 1 to given Maxiumum number of set

    Arguments:
        * maximum_number_of_set : Maximum number of a given set. This method
                                  will compute combination of subsets from 1 to
                                  this number.

        * length_of_combination : Lenth of each combination of subset.

    Example
        If we want to generate all 2 digits long subsets of set 1, 2, 3, 4 then
        this method will compute them and return [[1, 2], [1, 3], [1, 4], [2,
        3], [2, 4], [3, 4]] as a result.
    """
    polly_fill = False
    combinations_vector = [polly_fill]
    return _backtrack(
        combinations_vector=combinations_vector,
        maximum_number_of_set=maximum_number_of_set,
        length_of_combination=length_of_combination,
        index=0
    )
