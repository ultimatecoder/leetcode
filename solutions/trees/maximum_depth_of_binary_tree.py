#! /usr/bin/env python
"""
Problem

    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

    Note: A leaf is a node with no children.

Example:

    Given binary tree [3, 9, 20, null, null, 15, 7]

        3

    9       20

        15      7

    returns its depth = 3.

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

class Node:
    """Represents a node object of a tree"""

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def maximum_depth(root_node: Node=None) -> int:
    """Calculates the maximum depth of a given Node"""
    if root_node is None:
        return 0

    return 1 + max(
        maximum_depth(root_node=root_node.left),
        maximum_depth(root_node=root_node.right)
    )
