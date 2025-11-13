from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

def breadth_first(root):
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


# ===== Tree 1 =====
#          A
#        / | \
#       B  C  D
#      / \    |
#     E   F   G
#    / \
#   H   I

A1 = Node("A")
B1 = Node("B")
C1 = Node("C")
D1 = Node("D")
E1 = Node("E")
F1 = Node("F")
G1 = Node("G")
H1 = Node("H")
I1 = Node("I")

A1.left = B1
B1.right = C1
C1.right = D1
B1.left = E1
E1.right = F1
D1.left = G1
E1.left = H1
H1.right = I1

print("===== Tree 1 (Slide 1: Pink) =====")
print("Preorder traversal:")
preorder(A1)
print("\nPostorder traversal:")
postorder(A1)
print("\nBreadth-first traversal:")
breadth_first(A1)


# ===== Tree 2 =====
#          A
#        /   \
#       B     C
#      / \   /
#     D  E  F
#    /     / \
#   G     H   I

A2 = Node("A")
B2 = Node("B")
C2 = Node("C")
D2 = Node("D")
E2 = Node("E")
F2 = Node("F")
G2 = Node("G")
H2 = Node("H")
I2 = Node("I")

A2.left = B2
A2.right = C2
B2.left = D2
B2.right = E2
D2.left = G2
C2.left = F2
F2.left = H2
F2.right = I2

print("\n\n===== Tree 2 (Slide 2: Blue) =====")
print("Inorder traversal:")
inorder(A2)
print()
