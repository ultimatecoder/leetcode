#! /usr/bin/env python

from ..maximum_depth_of_n_ary_tree import find_max_depth, Node


def test_find_max_depth():
    root = Node(1)

    for level_1_child in [3, 2, 4]:
        child_node = Node(level_1_child)
        root.children.append(child_node)

    level_1_child = root.children[0]
    for level_2_child in [5, 6]:
        child_node = Node(level_2_child)
        level_1_child.children.append(child_node)
    assert find_max_depth(root) == 3
