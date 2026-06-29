class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my solution (bad come back after learning some)
# Binary tree traversals (preorder, inorder, postorder, level-order BFS)
# Recursive DFS patterns on trees (return-based recursion)
# Tree symmetry and mirror structure problems
# Difference between tree structure vs traversal output
# BFS vs DFS on trees (queue vs recursion/stack)
# Backtracking on trees (path exploration + undo state)
# Tree comparison problems (same tree, subtree check, serialization basics)

def inorderTraversal(root: TreeNode) -> list:
    r = True

    def mirror(right, left):
        nonlocal r
        if left is None and right is None:
            # print("val is none for both")
            return
        if left is None and right is not None or left is not None and right is None:
            r = False
            return
        if right.val == left.val and right != None:
            # print("all the way left == all the way right", right.val, left.val)
            mirror(right.right, left.left)
            mirror(right.left, left.right)

        else: 
            r = False
    
    mirror(root.right, root.left)
    return r

class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

test2 = TreeNode(1)

test2.left = TreeNode(2)
test2.right = TreeNode(2)

test2.left.right = TreeNode(3)
test2.right.right = TreeNode(3)

test3 = TreeNode(1)

test3.left = TreeNode(2)
test3.right = TreeNode(2)

test3.left.left = TreeNode(3)
test3.left.left.right = TreeNode(4)

test3.right.right = TreeNode(3)
test3.right.right.left = TreeNode(4)

test4 = TreeNode(1)

test4.left = TreeNode(2)
test4.right = TreeNode(2)

test4.left.left = TreeNode(3)
test4.left.left.left = TreeNode(4)

test4.right.right = TreeNode(3)


root2 = TreeNode(1)

root2.left = TreeNode(2)
root2.right = TreeNode(2)

root2.left.left = TreeNode(2)
root2.right.left = TreeNode(2)

print(inorderTraversal(root2))
print(inorderTraversal(test2))
print(inorderTraversal(test3))
print(inorderTraversal(test4))
print(inorderTraversal(root))