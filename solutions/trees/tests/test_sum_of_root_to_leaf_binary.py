#! /usr/bin/env python

from ..sum_of_root_to_leaf_binary_numbers import (
    sum_of_root_to_leaf_nodes, Node
)


def test_sum_of_root_to_leaf_nodes_for_balanced_tree():
    root = Node(1)

    root.left = Node(0)
    root.right = Node(1)

    root.left.left = Node(0)
    root.left.right = Node(1)

    root.right.left = Node(0)
    root.right.right = Node(1)

    assert sum_of_root_to_leaf_nodes(root) == 22


def test_sum_of_root_to_leaf_nodes_for_unbalanced_tree():
    root = Node(1)

    root.left = Node(1)

    assert sum_of_root_to_leaf_nodes(root) == 3
