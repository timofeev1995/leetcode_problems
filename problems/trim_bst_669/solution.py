# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self) -> None:

        def get_height(node):
            return 1 + max(get_height(node.left), get_height(node.right)) if node else 0

        height = get_height(self) - 1
        columns = 2 ** (height + 1) - 1
        res = [["."] * columns for _ in range(height + 1)]

        queue = deque([(self, (columns - 1) // 2)])
        r = 0

        while queue:
            for _ in range(len(queue)):
                node, c = queue.popleft()
                res[r][c] = str(node.val)
                if node.left:
                    queue.append((node.left, c - 2 ** (height - r - 1)))
                if node.right:
                    queue.append((node.right, c + 2 ** (height - r - 1)))
            r += 1

        for line in res:
            print(''.join(line))


class Solution:

    def trim_BST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return root
        elif root.val < low:
            return self.trim_BST(root.right, low, high)
        elif root.val > high:
            return self.trim_BST(root.left, low, high)
        else:
            root.left = self.trim_BST(root.left, low, high)
            root.right = self.trim_BST(root.right, low, high)

        return root


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(0, right=TreeNode(2, left=TreeNode(1))), TreeNode(4))
    print("Before:")
    tree.print()
    trimmed = Solution().trim_BST(tree, 1, 3)
    print("After:")
    trimmed.print()
