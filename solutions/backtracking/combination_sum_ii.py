#! /usr/bin/env python
"""
Problem

    Given a collection of candidate numbers (candidates) and a target number
    (target), find all unique combinations in candidates where the candidate
    numbers sums to target.

    Each number in candidates may only be used once in the combination.

Note

    * All numbers (including target) will be positive integers.
    * The solution set must not contain duplicate combinations.

Example 1

    Input

        candidates = [10, 1, 2, 7, 6, 1, 5], target = 8

    Output

        [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ]

Example 2

    Input

        candidates = [2, 5, 2, 1, 2], target = 5

    Output

        [
            [1, 2, 2],
            [5]
        ]
"""
from typing import List, Union

Numbers = List[int]
Combinations = List[Numbers]


def _merge(
    elements: Numbers, start_index:int, middle_index:int, end_index:int
) -> None:
    left_elements = elements[start_index:middle_index + 1]
    right_elements = elements[middle_index + 1:end_index + 1]
    left_index = 0
    right_index = 0
    index = start_index

    while index <= end_index:
        try:
            left = left_elements[left_index]
        except IndexError:
            elements[index] = right_elements[right_index]
            right_index += 1
            index += 1
            continue
        try:
            right = right_elements[right_index]
        except IndexError:
            elements[index] = left_elements[left_index]
            left_index += 1
            index += 1
            continue
        if left < right:
            elements[index] = left
            left_index += 1
        else:
            elements[index] = right
            right_index += 1
        index += 1


def _sort(elements: Numbers, start_index: int, end_index: int) -> None:
    middle_index = (start_index + end_index) // 2
    if start_index < end_index:
        _sort(elements, start_index=start_index, end_index=middle_index)
        _sort(elements, start_index=middle_index+1, end_index=end_index)
        _merge(elements, start_index, middle_index, end_index)


def _merge_sort(elements: List[int]) -> None:
    _sort(elements, start_index=0, end_index=len(elements) - 1)


def _combinations(
    numbers: Numbers, expected_sum: int, actual_sum:int=0,
    combinations_vector: Numbers=[], index:int =-1):
        combinations = set()
        if actual_sum == expected_sum:
            combination = tuple(combinations_vector)
            combinations.add(combination)
            return combinations
        elif actual_sum > expected_sum:
            return combinations
        index += 1
        for index_of_number, number in enumerate(numbers):
            try:
                combinations_vector[index] = number
            except IndexError:
                combinations_vector.append(number)
            actual_sum += number
            further_combinations = _combinations(
                numbers[index_of_number + 1:],
                expected_sum,
                actual_sum,
                combinations_vector[:index + 1],
                index,
            )
            if further_combinations:
                combinations = combinations.union(further_combinations)
            actual_sum -= number
        return combinations


def combinations(numbers: Numbers, expected_sum: int) -> Combinations:
    """Calculates pairs where sum of pair is equal to expected Sum

    This method will prepare all combinations of elements from Numbers where
    Sum of the pair is equal to a expected Sum value and pair is constructed
    from distinct elements of Numbers. Numbers can have

    Arguments:
        * numbers : Set of numbers where numbers can be duplicated. Given set
                    of numbers can be in any order.

        * expected_sum : Expected value of Sum. Sum of pair prepared from given
                         numbers will equal to this value.
    Example

        >>>combinations([18, 1, 9, 2, 1], expected_sum=4) == [[1, 1, 2]]
    """
    _merge_sort(numbers)
    combinations = _combinations(numbers, expected_sum)
    return [list(combination) for combination in combinations]
