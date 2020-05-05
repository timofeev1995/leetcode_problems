import pytest
from problems.word_break_II_140.solution import word_break


@pytest.mark.parametrize(
    ['s', 'word_dict', 'expected'],
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cats and dog", "cat sand dog"]
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        )
    ]
)
def test_word_break_ii(s, word_dict, expected):
    result = word_break(s, word_dict)
    assert set(result) == set(expected)
