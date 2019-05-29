#! /usr/bin/env python
"""
Problem

    Given an array with 'n' objects colored red, white or blue, sort them
    in-place so that objects of the same color are adjacent, with the colors in
    the order red, white and blue so that objects of the same color are
    adjacent, with the colors in the order red, white and blue.

    Here, we will use the integers 0, 1 and 2 to represent the color red, white
    and blue respectively.

    Note: You are not suppose to use the library's sort function for this
    problem.

Example

    Input

        [2, 0, 2, 1, 1, 0]

    Output

        [0, 0, 1, 1, 2, 2]

Follow up

    * A rathre straight forward solution is a two-pass algorithm using counting
      sort.

      First, iterate the array counting numbers of 0's, 1's and 2's then
      overwrite array with total number of 0's, then 1's and followed by 2's.

    * Could you come up iwth a one-pass algorithm using only constant spaces?

Link

    https://leetcode.com/problems/sort-colors/
"""
from typing import List

RED = 0
BLUE = 2


def sort(colors: List[int]) -> None:
    """Sorts given colors.

    Value or colors can be 0, 1 or 2 where 0 represents the color red, 1
    represents the color white and 2 representes the color blue. This method
    will arrage the given sequence of colors where all red colors are first
    followed by white colors and in the last blue colors.

    Similar problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    """
    pointer_to_red_colors = -1
    pointer_to_blue_colors = len(colors)
    index = pointer_to_red_colors + 1

    while index < pointer_to_blue_colors:
        if colors[index] == RED:
            pointer_to_red_colors += 1
            colors[index], colors[pointer_to_red_colors] = (
                colors[pointer_to_red_colors], colors[index]
            )
            index = pointer_to_red_colors + 1
        elif colors[index] == BLUE:
            pointer_to_blue_colors -= 1
            colors[index], colors[pointer_to_blue_colors] = (
                colors[pointer_to_blue_colors], colors[index]
            )
        else:
            index += 1
