#! /usr/bin/env python
"""
Problem

    Given a string containing just the characters '(', ')', '{', '}', '[', and
    ']', determine if the input string is valid.

    An input string is valid if:

        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.

Example 1

    Input

        "()"

    Output

        True

Example 2

    Input

        "()[]{}"

    Output

        True

Example 3

    Input

        "(["

    Output

        False

Example 4

    Input

        "([)]"

    Output

        False

Example 5

    Input

        "{[]}"

    Output

        True

Link

    https://leetcode.com/problems/valid-parentheses/
"""

def is_valid(braces: str) -> bool:
    """Validates given sequence of braces

    Values of braces can be '(', ')', '{', '}', '[', ']'. A correct sequence of
    braces is a sequence in which each brace is followed by closed brace of its
    type in order it opened.

    For example a sequence "()" is a valid sequence because an open brace '('
    is followed by closing brace of it round brace type. A sequence '([}' is
    not a valid sequence because a square brace is not followed by any closing
    square bracket.
    """
    open_braces = []
    for brace in braces:
        if brace in ['[', '{', '(']:
            open_braces.append(brace)
        else:
            try:
                last_open_brace = open_braces.pop()
            except IndexError:
                return False
            if (
                (brace == ']') and (last_open_brace != '[') or
                (brace == ')') and (last_open_brace != '(') or
                (brace == '}') and (last_open_brace != '{')
            ):
                return False
    return (open_braces == [])
