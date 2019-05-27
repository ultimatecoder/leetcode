#! /usr/bin/env python
"""
Problem

    Given a binary tree, return all root-to-leaf paths.

    Note: A leaf is a node with no children.

Example

    Input

        1

    2       3

      5

    Output

        ["1->2->5", "1->3"]

    Explanation

        All root-to-leaf paths are: 1->2->5, 1->3
"""

from typing import List


class Node:
    """Call this class to create a Node of a binary tree"""

    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f"<Node {self.value}>"


def binary_tree_paths(root: Node=None) -> List[str]:
    """Finds all paths from root to a leaf nodes

    Example:

        For below tree instance, this method will return two paths. One is 1 ->
        2 -> 5 and another one is 1 -> 3.

            1

        2       3

          5
    """
    paths = []

    if root.left is None and root.right is None:
        return [str(root.value)]

    for child_paths in (
        binary_tree_paths(root.left) + binary_tree_paths(root.right)
    ):
        path = f"{root.value}->{child_paths}"
        paths.append(path)
    return paths
