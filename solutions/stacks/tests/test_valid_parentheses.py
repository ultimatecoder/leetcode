#! /usr/bin/env python

from ..valid_parentheses import is_valid


def test_is_valid_with_various_combinations():
    sample_braces_and_expected_answer = (
        ("()[]{}", True),
        ("{[]}", True),
        ("(", False),
        ("((", False),
        ("([", False),
        ("}}}", False),
        ("({})]", False)
    )

    for braces, expected_answer in sample_braces_and_expected_answer:
        assert is_valid(braces) == expected_answer
