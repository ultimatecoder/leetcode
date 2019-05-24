#! /usr/bin/env python
"""
Problem

    Given an array of integers A sorted in non-decreasing order, return an
    array of the squares of each number, also in sorted non-decreasing order.

Example 1

    Input

        [-4, -1, 0, 3, 10]

    Output

        [0, 1, 9, 16, 100]

Example 2

    Input

        [-7, -3, 2, 3, 11]

    Output

        [4, 9, 9, 49, 121]

Notes

    * 1 <= A.length <= 10000
    * -10000 <= A[i] <= 10000
    * A is sorted in non-decreasing order.

Link


"""
from typing import List


def square_sequence(elements: List[int]) -> List[int]:
    """Calculates squares of given elements and sort them

    Arguments:
        * elements : Combination of negative and positive integers sorted.

    Returns:
        Sequence of integers prepared after making a square of each of them and
        then sort them in ascending order.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    left_index = 0
    right_index = len(elements) - 1
    squared_sequences: List[int] = []
    while (left_index <= right_index):
        left = elements[left_index] ** 2
        right = elements[right_index] ** 2
        if left > right:
            squared_sequences.insert(0, left)
            left_index += 1
        else:
            squared_sequences.insert(0, right)
            right_index -= 1
    return squared_sequences
