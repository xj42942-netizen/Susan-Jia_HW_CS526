from collections import deque

# Define a simple binary tree node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ===== Traversal Functions =====

def preorder(root):
    """Preorder: Root → Left → Right"""
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    """Inorder: Left → Root → Right"""
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    """Postorder: Left → Right → Root"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

def breadth_first(root):
    """Breadth-First (Level Order Traversal)"""
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# ===== Example Tree =====
# Suppose your tree is:
#          A
#        /   \
#       B     C
#      / \   / \
#     D  E  F  G

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

# ===== Output Section =====
print("Preorder traversal:")
preorder(A)
print("\nInorder traversal:")
inorder(A)
print("\nPostorder traversal:")
postorder(A)
print("\nBreadth-first traversal:")
breadth_first(A)
