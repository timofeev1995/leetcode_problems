from typing import List


def h_index(citations: List[int]) -> int:
    # Actually, idea is simple:
    # to find an element which is bigger than number of elements on the right side.

    len_ = len(citations)
    left = 0
    right = len_ - 1

    while left <= right:
        m = (right + left) // 2
        if citations[m] >= len_ - m:
            right = m - 1
        else:
            left = m + 1

    return len_ - left
