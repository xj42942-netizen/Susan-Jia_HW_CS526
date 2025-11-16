import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def findNode(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def deleteNode(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete(node.right, min_node.value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def printTree(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)

if __name__ == "__main__":
    bst = BST()
    arr = random.sample(range(1, 1001), random.randint(5, 50))
    print("Input set:", arr)

    # Build tree
    for val in arr:
        bst.addNode(val)
    print("\nInitial tree (inorder):")
    bst.printTree()

    # Delete a random node
    delete_val = random.choice(arr)
    print(f"\nDeleting node {delete_val}")
    bst.deleteNode(delete_val)
    bst.printTree()

    # Add a new random node
    new_val = random.randint(1, 1000)
    print(f"\nAdding new node {new_val}")
    bst.addNode(new_val)
    bst.printTree()

    # FindNode test: one positive, one negative
    existing_val = random.choice(arr)
    missing_val = 2000
    print(f"\nFinding {existing_val}: {'Found' if bst.findNode(existing_val) else 'Not Found'}")
    print(f"Finding {missing_val}: {'Found' if bst.findNode(missing_val) else 'Not Found'}")
