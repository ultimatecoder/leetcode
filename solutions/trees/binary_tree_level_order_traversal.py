#! /usr/bin/env python
"""
Problem

    Given a binary tree, return the level order traversal of its nodes' values.
    (ie, from left to right level by level).

    For example

        Given binary tree [3, 9, 20, null, null, 15, 7]

        3

    9       20

          15   7

    returns its level order traversal as:
        [

            [3],
            [9, 20],
            [15, 7]
        ]
"""
from typing import List

Paths = List[List[int]]


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _traverse(nodes: List[Node]) -> Paths:
        if not nodes:
            return []

        sequences = []
        sequence = []
        next_nodes = []
        for node in nodes:
            sequence.append(node.value)
            for next_node in [node.left, node.right]:
                if next_node:
                    next_nodes.append(next_node)
        sequences.append(sequence)
        child_sequences = _traverse(next_nodes)
        sequences.extend(child_sequences)
        return sequences


def level_order(root: Node=None) -> Paths:
    """Computes the level order traversal path for given tree

    Example

            12

        8        13

      1  2

    Level order traversal path for given Binary Tree will be below

    Level 1: 12
    Level 2: 8, 13
    Level 3: 1, 2
    """
    sequences: Paths = []
    if root:
        nodes = [root]
        sequences = _traverse(nodes)
    return sequences
