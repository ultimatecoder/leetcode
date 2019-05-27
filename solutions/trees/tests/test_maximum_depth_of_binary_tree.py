#! /usr/bin/env python

from ..maximum_depth_of_binary_tree import Node, maximum_depth


def test_maximum_depth_for_small_tree():
    # Root

    root_node = Node(3)
    # Level - 1

    root_node.right = Node(9)
    root_node.left = Node(20)

    # Level - 2
    root_node.left.right = Node(15)
    root_node.left.left = Node(7)

    assert maximum_depth(root_node) == 3


def test_maximum_depth_for_big_tree():
    # Root

    root_node = Node(4)

    # Level - 1

    root_node.right = Node(3)
    root_node.left = Node(4)

    # Level - 2

    root_node.right.left = Node(3)
    root_node.right.right = Node(23)

    root_node.left.left = Node(4)
    root_node.left.right = Node(2)

    # Level - 3

    root_node.right.left.right = Node(32)
    root_node.right.left.left = Node(23)

    root_node.right.right.right = Node(22)
    root_node.right.right.left = Node(21)

    root_node.left.left.right = Node(221)
    root_node.left.left.left = Node(13)

    root_node.left.right.right = Node(13)
    root_node.left.right.left = Node(21)

    # Level - 4

    root_node.right.left.right.right = Node(32)
    root_node.right.left.right.left = Node(32)

    root_node.right.left.left.left = Node(23)
    root_node.right.left.left.right = Node(23)

    root_node.right.right.right.right = Node(22)
    root_node.right.right.right.left = Node(22)

    root_node.right.right.left.right = Node(21)
    root_node.right.right.left.left = Node(21)

    root_node.left.left.right.left = Node(221)
    root_node.left.left.right.right = Node(221)

    root_node.left.left.left.right = Node(13)
    root_node.left.left.left.left = Node(13)

    root_node.left.right.right.right = Node(13)
    root_node.left.right.right.left = Node(13)

    root_node.left.right.left.right = Node(21)
    root_node.left.right.left.left = Node(21)

    assert maximum_depth(root_node) == 5
