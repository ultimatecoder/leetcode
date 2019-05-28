#! /usr/bin/env python
"""
Problem

    Given a n-ary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

    For example, given a 3-ary tree:

            1

        3   2   4

      5  6

    We should return its max depth, which is 3.

Note

    1. The depth of the tree is at most 1000.
    2. The total number of nodes is at most 5000.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def find_max_depth(root: Node) -> int:
    """Calculates the maximum depth of a given Tree

    Example

            1

        0   2   4

              3 5 8

                   9

    The longest branch for a given tree is 1 -> 4 -> 8 -> 9 thus the maximum
    depth for a given tree is 4.
    """
    if not root:
        return 0

    max_child_depth = 0
    for child in root.children:
        child_depth = find_max_depth(child)
        if child_depth > max_child_depth:
            max_child_depth = child_depth
    return max_child_depth + 1
