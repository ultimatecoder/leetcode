#! /usr/bin/env python
"""
Problem

    Given 2d grid map of '1's (land) and '0' s (water), count the number of
    islands. An island is surrounded by water and is formed by connecting
    adjacent lands horizontally or vertically. You may assume all four edges of
    the grid are all surrounded by water.

Example 1

    Input

        11110
        11010
        11000
        00000

    Output

        1

Example 2

    Input

        11000
        11000
        00100
        00011

    Output

        3
"""
import collections
from typing import Deque, List, Set, Tuple


Grid = List[List[str]]
RowIndex = int
ColumnIndex = int
Chunk = Tuple[RowIndex, ColumnIndex]


ROW = 0
COLUMN = 1


def _traverse_entire_mountain(_map: Grid, chunk_of_mountain: Chunk):
    mountain_chunks: Deque = collections.deque()
    mountain_chunks.appendleft(chunk_of_mountain)
    while len(mountain_chunks) != 0:
        mountain_chunk = mountain_chunks.pop()
        _convert_to_water(_map, mountain_chunk)

        right = (mountain_chunk[ROW], mountain_chunk[COLUMN] + 1)
        left = (mountain_chunk[ROW], mountain_chunk[COLUMN] - 1)
        up = (mountain_chunk[ROW] - 1, mountain_chunk[COLUMN])
        down = (mountain_chunk[ROW] + 1, mountain_chunk[COLUMN])

        for future_chunk in (right, left, up, down):
            if (
                (_is_valid(_map, future_chunk)) and
                (_is_land(_map, future_chunk))
            ):
                mountain_chunks.appendleft(future_chunk)
                _convert_to_water(_map, future_chunk)

def _is_valid(_map: Grid, chunk: Chunk) -> bool:
    return (
        (chunk[ROW] >= 0 and chunk[ROW] < len(_map)) and
        (chunk[COLUMN] >= 0 and chunk[COLUMN] < len(_map[0]))
    )


def _convert_to_water(_map: Grid, chunk: Chunk) -> None:
    _map[chunk[ROW]][chunk[COLUMN]] = '0'


def _is_land(_map: Grid, chunk: Chunk) -> bool:
    return _map[chunk[ROW]][chunk[COLUMN]] == '1'


def count_mountains(_map: Grid) -> int:
    """Counts number of mountains on given Map

    This method counts mounts present on a given earth. To avoid re-counting
    given mountain, it converts counted mounts to a water.

    Arguments:

        * Map : A instance of 2 dimensional Matrix where each cell is either
                water or land. If give cell of a Map is '1' then it should be
                considered that there is land on that cell. If given cell of a
                Map is '0' then it should be considered that there is water
                filled in that cell of map.

    Terminologies

        * Island: An Island is a collection of all adjacent lands surrounded by
                  water.
    """
    discovered_lands = 0
    visited_chunks: Set = set()
    for row_index in range(len(_map)):
        for column_index in range(len(_map[0])):
            chunk = (row_index, column_index)
            if _is_land(_map, chunk):
                discovered_lands += 1
                _traverse_entire_mountain(_map, chunk)
    return discovered_lands
