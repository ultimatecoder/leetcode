#! /usr/bin/env python
"""
Problem

    Given a binary tree, each node has value '0' or '1'. Each root-to-leaf path
    represents a binary number starting with the most significant bit. For
    example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
    01101 in binary, which is 13.

    For all leaves in the tree, consider the numbers represented by the path
    from the root to that leaf.

    Return the sum of these numbers.

Example 1

            1

        0       1

      0   1    0  1


Input

    [1, 0, 1, 0, 1, 0, 1]

Output

    22

Explanation

    (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Notes

    * The number of nodes in the tree is between 1 and 1000.
    * node.val is 0 or 1.
    * The answer will not exceed 2^31 - 1
"""

from typing import List, Tuple


Paths = List[List[int]]
Sum = int
BLANK: Tuple[Paths, Sum] = ([[]], 0)


class Node:
    """Represents Binary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f"<Node {self.value}>"


def is_leaf_node(node: Node) -> bool:
    return (node.right is None) and (node.left is None)


def _calculate_leaf_nodes_and_sum(root: Node) -> Tuple[Paths, Sum]:
    if root is None:
        return ([[]], 0)

    if is_leaf_node(root):
        paths = [[root.value]]
        total = root.value
        return (paths, total)
    total = 0
    paths = []

    left_childs = _calculate_leaf_nodes_and_sum(root.left)
    right_childs = _calculate_leaf_nodes_and_sum(root.right)

    for childs in [left_childs, right_childs]:
        if childs != BLANK:
            child_paths, child_total = childs
            for path in child_paths:
                base = 2 ** len(path)
                value = base * root.value
                paths.append([value] + path)
                total += value
            total += child_total
    return (paths, total)


def sum_of_root_to_leaf_nodes(root: Node) -> Sum:
    """Calculates Sum of all the paths in a binary tree

    Example
            1

        0       1

      0   1   0   1

    Above tree has below paths
    100, 101, 110, 111

    Considering all of them as a binary tree we get below values
    (100) 4, (101) 5, (110) 6, (111) 7

    Summing these numbers we get 22 which is sum of 4, 5, 6, 7.
    This method will return 22 if given tree organized as above.
    """
    paths, total = _calculate_leaf_nodes_and_sum(root)
    return total
