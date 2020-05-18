from typing import List


def dfs(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]
    else:
        collected_permutations = []
        for i, num in enumerate(nums):
            permutations_wo_this = dfs(nums[:i] + nums[i + 1:])
            this_permutations = [[num] + x for x in permutations_wo_this]
            collected_permutations.extend(this_permutations)
        return collected_permutations


def permute(nums: List[int]) -> List[List[int]]:
    permutations = dfs(nums)
    return permutations
