from typing import List, Set


def concatenated_words_graph_descent(word: str, words: Set[str], memory: Set[str]) -> bool:
    """

    :param memory:
    :param word:
    :param words:
    :return:
    """
    # Separate word by i-pointer starting with 1
    # because having i=0 we get right == word
    word_len = len(word)
    for i in range(1, word_len):
        left = word[:i]
        right = word[i:]
        # Check if two parts are ok -> True
        if (left in words) and (right in words):
            return True
        # Check if left is in words and we can get right by concatenation
        elif left in words:
            if right in memory:
                return True
            else:
                dfs_result = concatenated_words_graph_descent(right, words, memory)
                if dfs_result:
                    # We update memory inplace
                    memory.add(right)
                    return True
        # Same logic for opposite case
        elif right in words:
            if left in memory:
                return True
            else:
                dfs_result = concatenated_words_graph_descent(left, words, memory)
                if dfs_result:
                    memory.add(left)
                    return True

    return False


def find_all_concatenated_words(words: List[str]) -> List[str]:
    """

    :param words: `List[str]` with given words
    :return: `List[str]` of words which can be built with concatenation of other words
    """
    words = set(words)
    memory = set()
    result = [w for w in words if concatenated_words_graph_descent(w, words, memory)]
    return result
