from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """

    :param s: `str` to be segmented
    :param word_dict: `List[str]` with dictionary of words
                      we can use for segmentation

    :return: `bool` can / can not be segmented
    """

    # We are going to use `in` statement with word_dict,
    # so it's better to have set instead of list
    word_dict = set(word_dict)

    # This list shows if it's possible to segment s[:i] prefix
    # Also plays memory role
    is_valid_prefix = [True]

    # We iterate trough string s with pointer `i`
    for i in range(1, len(s) + 1):
        # And for each `j` < `i` we check two things:
        # 1. If we have s[:j] as valid prefix?
        # 2. If the rest part s[j:i] is in word dictionary?
        # If yes, we store `True` in our memory: that means s[:i] now is valid prefix.
        # If no, then s[:i] now is valid prefix, store `False` in memory
        for j in range(i):
            if (is_valid_prefix[j]) and (s[j:i] in word_dict):
                is_valid_prefix += [True]
                break
            elif j == i - 1:
                is_valid_prefix += [False]

    return is_valid_prefix[-1]
