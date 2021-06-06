# Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes
# along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_tree(root):
    return get_depth(root, 0)


def get_depth(node, max_depth):
    if node is None:
        return max_depth

    else:
        return max(get_depth(node.left, max_depth + 1), get_depth(node.right, max_depth + 1))
