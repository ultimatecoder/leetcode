#! /usr/bin/env python

from ..letter_combinations_of_a_phone_number import combinations


def test_combinations():
    sample_input = (
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
        ("786",  [
            'ptm', 'ptn', 'pto', 'pum', 'pun', 'puo', 'pvm', 'pvn', 'pvo',
            'qtm', 'qtn', 'qto', 'qum', 'qun', 'quo', 'qvm', 'qvn', 'qvo',
            'rtm', 'rtn', 'rto', 'rum', 'run', 'ruo', 'rvm', 'rvn', 'rvo',
            'stm', 'stn', 'sto', 'sum', 'sun', 'suo', 'svm', 'svn', 'svo'
        ])
    )
    for digits, expected_answer in sample_input:
        assert combinations(digits) == expected_answer
