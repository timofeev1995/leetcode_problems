import pytest
from problems.word_break_139.solution import word_break


@pytest.mark.parametrize(
    ['s', 'word_dict', 'expected'],
    [
        ('leetcode', ['leet', 'code'], True),
        ('applepenapple', ['apple', 'pen'], True),
        ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'], False),
        ('aaaaaaa', ['aaa', 'aaaa'], True)
    ]
)
def test_word_break(s, word_dict, expected):
    result = word_break(s, word_dict)
    assert result == expected

