#! /usr/bin/env python
"""
Problem

    Given an array 'A' of non-negative integers, return an array consisting of
    all the even elements of A, followed by all the odd elements of 'A'.

    You may return any answer array that satisfies this condition.

Example 1

    Input

        [3, 1, 2, 4]

    Output

        [2, 4, 3, 1]

    The outputs [4, 2, 3, 1], [2, 4, 1, 3] and [4, 2, 1, 3] would also be
    accepted.

Note

    1. 1 <= A.length <= 5000
    2. 0 <= A[i] <= 5000

Link

    https://leetcode.com/problems/sort-array-by-parity/

Tag

    Easy
"""
from typing import List


def is_odd(number: int) -> bool:
    """Checks a given number is Odd or not"""
    return number % 2 == 1


def is_even(number: int) -> bool:
    """Checks a given number is Even or not"""
    return not is_odd(number)


def parity_sort(numbers: List[int]) -> List[int]:
    """Sorts given numbers

    This utility will sort the given numbers by placing all the even numbers at
    the beginning and odd numbers at the end.

    Example:
        >>>parity_sort([3, 1, 2, 4]) == [2, 4, 3, 1]

    Time complexity: O(n)
    Space complexity: O(1)

    Notes: Other approaches will increase the time complexity by placing all the
    elements to a new storage. Which will increase the space complexity. This
    approach will not store any elements to new storage, but rather than sort
    them in place.
    """
    left = 0
    right = len(numbers) - 1
    while left <= right:
        if is_odd(numbers[left]) and is_even(numbers[right]):
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
        elif is_even(numbers[left]):
            left += 1
        elif is_odd(numbers[right]):
            right -= 1
    return numbers
