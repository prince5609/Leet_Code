# CHECK IS TREE BALANCED OR NOT
# A balanced tree is one whose height of every node differ by not more than 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    if root is None:
        return True

    # Make a utility func to check if node is a leaf

    def is_leaf(node):
        if not node.left and not node.right:
            return True
        return False

    # Calculate if certain node is balanced
    # 1) Check the height of left and right children
    # 2) If unbalanced, return -1 else return height

    def get_height(node):
        # If node is a leaf then height is 1
        if is_leaf(node):
            return 1

        left = node.left
        right = node.right

        # If node has a left child
        if left is not None:
            h_left = get_height(left)

            if h_left == -1:
                return -1

        # If node doesn't have a left child
        else:
            h_left = 0

        # Now same for right
        if right is not None:
            h_right = get_height(right)

            if h_right == -1:
                return -1

        else:
            h_right = 0

        # If left & right height differs by more than 1 points
        if abs(h_left - h_right) > 1:
            return -1

        # If everything is ok
        return max(h_left, h_right) + 1

    result = get_height(root)
    if result == -1:
        return False
    return True
