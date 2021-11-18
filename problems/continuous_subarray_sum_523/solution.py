from typing import List


def check_subarray_sum(nums: List[int], k: int) -> bool:
    accum = 0
    memory = {0: -1}
    for i, number in enumerate(nums):
        accum += nums[i]
        if k != 0:
            accum = accum % k
        if accum in memory:
            if i - memory[accum] >= 2:
                return True
        else:
            memory[accum] = i
    return False


if __name__ == '__main__':

    nums = [23, 2, 4, 6, 7]
    k = 6
    assert check_subarray_sum(nums, k)

    nums = [23,2,6,4,7]
    k = 6
    assert check_subarray_sum(nums, k)

    nums = [23,2,6,4,7]
    k = 13
    assert not check_subarray_sum(nums, k)