from collections import deque


# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if root is None:
        return 0
    curr_level = deque([(root, 1)])
    while curr_level:
        node, depth = curr_level.popleft()
        if node.left is None and node.right is None:
            return depth
        if node.left:
            curr_level.append((node.left, depth + 1))
        if node.right:
            curr_level.append((node.right, depth + 1))
