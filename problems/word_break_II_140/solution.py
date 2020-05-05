from typing import List, Mapping, Tuple


def word_break_graph_descent(
        s: str, word_dict: List, memory: Mapping[str, List[str]]
) -> Tuple[List[List[str]], Mapping[str, List[str]]]:
    """
    Walk the tree from top to bottom looking for possible ways to segment s.
    :param s: `str` to be segmented
    :param word_dict: `list` of words we can use
    :param memory: `Mapping` from string to sequences we can build using word_dict
    :return:
        accumulator: `List[List]` with possible ways to segment s and memory for time complexity reducing
    """
    if s in memory:
        return memory[s], memory

    accumulator = []
    for word in word_dict:
        if word == s:
            accumulator.append([word])
        elif s.startswith(word):
            inner_accum, memory = word_break_graph_descent(s[len(word):], word_dict, memory)
            if inner_accum:
                accumulator += [[word] + x for x in inner_accum]

    memory[s] = accumulator
    return accumulator, memory


def word_break(s: str, word_dict: List[str]) -> List[str]:
    """

    :param s: `str` to be segmented
    :param word_dict: `list` of words we can use
    :return: `List[str]` with all possible ways to segment s.
    """
    initial_memory = {}
    ways_to_break, _ = word_break_graph_descent(s, word_dict, initial_memory)
    ways_to_break_str = [' '.join(x) for x in ways_to_break]
    return ways_to_break_str



