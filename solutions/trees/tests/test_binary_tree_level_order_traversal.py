#! /usr/bin/env python

from ..binary_tree_level_order_traversal import level_order, Node


def test_level_order_for_example_1():
    root = Node(12)
    root.left = Node(8)
    root.right = Node(13)
    root.left.left = Node(1)
    root.left.right = Node(2)

    assert level_order(root) == [[12], [8, 13], [1, 2]]


def test_level_order_for_example_2():
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_level_order_for_empty_tree():
    assert level_order() == []


def test_level_order_for_one_node_tree():
    root = Node(13)

    assert level_order(root) == [[13]]
