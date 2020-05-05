from typing import List


def h_index(citations: List[int]) -> int:

    len_citations = len(citations) + 1
    if len_citations == 0:
        return 0
    elif len_citations == 1:
        if citations[0] > 0:
            return 1
        else:
            return 0

    memory = [0] * (len_citations + 1)
    for paper in citations:
        idx_to_increment = min(paper, len_citations)
        memory[idx_to_increment] += 1

    cum_sum = 0
    for i in reversed(range(len_citations + 1)):
        cum_sum += memory[i]
        if cum_sum >= i:
            return i

