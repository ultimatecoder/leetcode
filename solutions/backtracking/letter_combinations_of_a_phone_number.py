#! /usr/bin/env python
"""
Problem

    Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent.

    A mapping of digit letters (just like on the telephone buttons) is given
    below. Note that 1 does not map to any letters.

    1 ()     2 (abc) 3 (def)
    4 (ghi)  5 (jkl) 6 (mno)
    7 (pqrs) 8 (tuv) 9 (wxyz)

Example

    Input

        "23"

    Output

        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Notes

    Although the above answer is in lexicographical order, your answer could be
    in any order you want.
"""

from typing import List


def _combinations(choices_of_alphabets: List[List[str]]) -> List[str]:
    if len(choices_of_alphabets) == 0:
        return []
    elif len(choices_of_alphabets) == 1:
        return choices_of_alphabets.pop()
    left_alphabet_combination = choices_of_alphabets.pop(0)
    right_alphabet_combination = _combinations(choices_of_alphabets)
    alphabet_combinations = []
    for left_alphabet in left_alphabet_combination:
        for right_alphabet in right_alphabet_combination:
            alphabet_combinations.append(left_alphabet + right_alphabet)
    return alphabet_combinations


def combinations(digits: str) -> List[str]:
    """Computes all combinations of letters from digits

    First this method will convert each letter to a set of alphabets where each
    digit represent a unique set of 3 to 4 sequence of alphabets. Then this
    method computes all combinations of given alphabets.

    Table of digit to alphabet

        2 = abc
        3 = def
        4 = ghi
        5 = jkl
        6 = mno
        7 = pqrs,
        8 = tuv,
        9 = wxyz

    Example
        >>>combinations("23") == [
            "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
        ]
    """
    alphabets = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    choices_of_alphabets = []
    for digit in digits:
        choices_of_alphabets.append(alphabets[digit])
    return _combinations(choices_of_alphabets)
