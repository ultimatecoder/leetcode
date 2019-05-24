#! /usr/bin/env python
"""
Problem

    Given an array A of non-negative integers, half of the integers in A are
    odd, and half of the integers are even.

    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
    even, i is even.

    You may return any answer array that satisfies this condition.

Example 1

    Input

        [4, 2, 5, 7]

    Output

        [4, 5, 2, 7]

    Explanation

        [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5] would also have been accepted.


Note

    * 2 <= A.length <= 20000
    * A.length % 2 == 0
    * 0 <= A[i] <= 1000

Link

    https://leetcode.com/problems/sort-array-by-parity-ii/
"""

from typing import List


def is_even(number: int) -> bool:
    """Checks that the given number is even"""
    return number % 2 == 0


def sort_by_parity(elements: List[int]) -> List[int]:
    """Puts all even and odd at even and odd position

    This method place all even elements at even position of a sequence and all
    odd elements at odd positions.

    Argument
        * elements : A special sequence of positive integers where half of
                     elements are even and half are odd. Length of this
                     elements should be even.

    Returns
        Sequence of given elements where all even elements are at even position
        and odd elements are at odd position.

    Example

        >>>sort_by_parity([4, 2, 5, 7]) == [4, 5, 2, 7]
    """
    sorted_sequence: List[int] = []
    even_index = 0
    odd_index = 1
    for element in elements:
        if is_even(element):
            sorted_sequence.insert(even_index, element)
            even_index += 2
        else:
            sorted_sequence.insert(odd_index, element)
            odd_index += 2
    return sorted_sequence
