#! /usr/bin/env python
"""
Problem

    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
    Fibonacci sequence, such that each number is the sum of the two preceding
    ones, starting from 0 and 1. That is,

        F(0) = 0, F(1) = 1
        F(N) = F(N - 1) + F(N - 2), for N > 1.

    Given N, calculate F(N).

Example 1

    Input

        2

    Output

        1

    Explanation

        F(2) = F(1) + F(0) = 1 + 0

Example 2

    Input

        3

    Output

        2

    Explanation

        F(3) = F(2) + F(1) = 1 + 1 = 2

Example 3

    Input

        4

    Output

        3

    Explanation

        F(4) = F(3) + F(2) = 2 + 1 = 3

Note

    * 0 <= N <= 30
"""
from typing import Dict


def _fibonacci_sub(position: int, cache: Dict) -> int:
    try:
        return cache[position]
    except KeyError:
        return (
            _fibonacci_sub(position-1, cache) +
            _fibonacci_sub(position - 2, cache)
        )


def fibonacci(position: int) -> int:
    """Calculates a fibonacci position for given position

    Arguments:
        * position : Position of fibonacci sequence. A value of 3 will return a
                     fibonacci position for 3rd position.
    Example

        >>>fibonacci(2) == 1
    """
    cache = {0: 0, 1: 1}
    for index in range(2, position+1):
        cache[index] = _fibonacci_sub(index, cache)
    return cache[position]
