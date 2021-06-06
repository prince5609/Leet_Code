# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Means if left is made right and right is made to be left then it should be it's mirror image

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):

    def to_check(tree1, tree2):
        if not tree1 and not tree2:
            return True

        elif tree1 and tree2:
            return tree1.val == tree2.val and to_check(tree1.left, tree2.right) and to_check(tree1.right, tree2.left)

        else:
            return False

    return to_check(root.left, root.right)
