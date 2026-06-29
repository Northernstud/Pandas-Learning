from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list:
    r = []
    def inorderTrav(root: TreeNode):
        if root is None: 
            return

        inorderTrav(root.left)
        r.append(root.val)
        if root.right is not None:
            inorderTrav(root.right)
    inorderTrav(root)
    return r

def build_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root

# Create nodes
root = build_tree([1,2,None,3,None,4])


print(inorderTraversal(root))