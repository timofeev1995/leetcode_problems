from typing import List


class Solution:
    # TODO: passes the test but too slow.
    def dfs(self, stones, start_stone, visited, accum):
        if visited[start_stone]:
            return accum
        else:
            visited[start_stone] = True
            accum += 1
        start_stone = stones[start_stone]
        allowed_neighbors = [
            i for i, s in enumerate(stones)
            if ((s[0] == start_stone[0]) or (s[1] == start_stone[1])) and not visited[i]
        ]
        if len(allowed_neighbors):
            for an in allowed_neighbors:
                accum = self.dfs(stones, an, visited, accum)
        return accum

    def find_unvisited(self, visited: List[int]):
        for i, status in enumerate(visited):
            if not status:
                return i
        return -1

    def find_component_sizes(self, stones: List[List[int]]) -> List[int]:
        visited = [False] * len(stones)
        component_sizes = []
        candidate = 0
        while candidate != -1:
            component_sizes.append(self.dfs(stones, candidate, visited, 0))
            candidate = self.find_unvisited(visited)
        return component_sizes

    def removeStones(self, stones: List[List[int]]) -> int:
        component_sizes = self.find_component_sizes(stones)
        return sum([component - 1 for component in component_sizes])


if __name__ == '__main__':
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(Solution().removeStones(stones))
