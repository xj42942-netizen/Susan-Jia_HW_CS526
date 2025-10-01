class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def doIt(node):
    if node is None:
        return
    doIt(node.next)
    print(node.value)

# Create linked list: 12 -> 3 -> 5 -> 2
head = Node(12)
head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(2)

doIt(head)
