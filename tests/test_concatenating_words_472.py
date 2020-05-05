import pytest
from problems.concatenating_words_472.solution import find_all_concatenated_words


@pytest.mark.parametrize(
    ["words", "expected"],
    [
        (
            ["cats", "cat", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
            ["catsdogcats","dogcatsdog","ratcatdogcat"]
        ),
    ]
)
def test_concatenating_words(words, expected):
    result = find_all_concatenated_words(words)
    assert set(result) == set(expected)

