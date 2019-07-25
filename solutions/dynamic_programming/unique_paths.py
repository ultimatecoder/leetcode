#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem
    A robot is located at the top-left corner of a 'M x N' grid (Marked 'Start'
    in the diagram below).

    The robot can only move either down or right at any point in time. The
    robot is trying to reach the bottom-right corner of the grid (Marked
    'Finish' in the diagram below).

    How many possible unique paths are there?

    Diagram

        _____________________________
        | R |   |   |   |   |   |   |
        _____________________________
        |   |   |   |   |   |   |   |
        _____________________________
        |   |   |   |   |   |   |   |
        -----------------------------
                                  ^
                               'Finish'

    Above is a 7 x 3 gridd. How many possible unique paths are there?

    Note: M and N will be at most 100.

Example 1

    Input

        M = 3, N = 2

    Output

        3

    Explanation

        From the top-left corner, there are a total of 3 ways to reach the
        bottom-right corner:
            1. Right -> Right -> Down
            2. Right -> Down -> Right
            3. Down -> Right -> Right

Example 2

    Input

        M = 7, N = 3

    Output

        28
"""
from typing import Tuple, Dict, Union

Row_index = int
Column_index = int
Cell = Tuple[Row_index, Column_index]
VisitedPaths = Union[Dict[Cell, int], None]
NumberOfPaths = int


ROW = 0
COLUMN = 1


def _count_paths(
    total_rows: int, total_columns: int,
    start: Cell, destination: Cell,
    visited: VisitedPaths=None
) -> NumberOfPaths:
    if visited is None:
        visited = {}
    try:
        return visited[start]
    except KeyError:
        if (start[COLUMN] >= total_columns) or (start[ROW] >= total_rows):
            return 0
        if start == destination:
            return 1
        right_cell: Cell = (start[ROW], start[COLUMN] + 1)
        down_cell: Cell = (start[ROW] + 1, start[COLUMN])
        right_paths = _count_paths(
            total_rows, total_columns, right_cell, destination, visited
        )
        down_paths = _count_paths(
            total_rows, total_columns, down_cell, destination, visited
        )
        result = right_paths + down_paths
        visited[start] = result
        return result


def count_unique_paths_from_top_left_to_bottom_right(
    total_rows: int, total_columns: int
) -> NumberOfPaths:
    """Counts number of unique paths

    This method calculates number of unique paths to reach from top-left start
    to bottom-right cell at matrix of given rows and columns.
    """
    return _count_paths(
        total_rows=total_rows,
        total_columns=total_columns,
        start=(0, 0),
        destination=(total_rows - 1, total_columns - 1),
    )
