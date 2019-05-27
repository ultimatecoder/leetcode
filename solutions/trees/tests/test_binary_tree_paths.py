#! /usr/bin/env python

from ..binary_tree_paths import Node, binary_tree_paths


def test_binary_tree_paths_with_small_tree():
    # Root

    root_node = Node(3)
    # Level - 1

    root_node.right = Node(9)
    root_node.left = Node(20)

    # Level - 2
    root_node.left.right = Node(15)
    root_node.left.left = Node(7)

    assert binary_tree_paths(root_node) == ["3->20->7", "3->20->15", "3->9"]


def test_binary_tree_paths_with_large_tree():

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

    assert binary_tree_paths(root_node) == [
        '4->4->4->13->13',
        '4->4->4->13->13',
        '4->4->4->221->221',
        '4->4->4->221->221',
        '4->4->2->21->21',
        '4->4->2->21->21',
        '4->4->2->13->13',
        '4->4->2->13->13',
        '4->3->3->23->23',
        '4->3->3->23->23',
        '4->3->3->32->32',
        '4->3->3->32->32',
        '4->3->23->21->21',
        '4->3->23->21->21',
        '4->3->23->22->22',
        '4->3->23->22->22'
    ]
