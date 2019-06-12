#! /usr/bin/env python
"""
Problem

    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are '+', '-', '*', '/'. Each operand may be an integer or
    another expression.

Note:

    * Division between two integers should truncate toward zero.

    * The given RPN expression is always valid. That means the expression would
      always evaluate to a result and there won't be any division by zero
      operation.

Example 1

    Input

        ["2", "1", "+", "3", "*"]

    Output

        9

    Explanation

        ((2 + 1) * 3) = 9

Example 2

    Input ["4", "13", "5", "/", "+"]

    Output

        6

    Explanation

        (4 + (13 / 5)) = 6

Example 3

    Input

        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    Output

        22

    Explanation

        = ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22
"""
from typing import List

ReversePolishNotationExpression = List[str]


def evaluate(expression: ReversePolishNotationExpression) -> int:
    """Evaluates given Reverse Polish Notation Expression"""
    numbers: List[int] = []
    for character in expression:
        if character == '+':
            number_1 = numbers.pop()
            number_2 = numbers.pop()
            numbers.append(number_1 + number_2)
        elif character == '/':
            number_1 = numbers.pop()
            number_2 = numbers.pop()
            # Note: Because requirement specifically insist to prefer a
            # round-down conversion, using 'int' which always converts to
            # round-down.
            numbers.append(int(number_2 / number_1))
        elif character == '*':
            number_1 = numbers.pop()
            number_2 = numbers.pop()
            numbers.append(number_1 * number_2)
        elif character == '-':
            number_1 = numbers.pop()
            number_2 = numbers.pop()
            numbers.append(number_2 - number_1)
        else:
            numbers.append(int(character))
    return numbers[0] if numbers else 0
