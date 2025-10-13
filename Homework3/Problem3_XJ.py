# Problem 3 - Using Recursion

# Part 1: Array versio:
def reverse_stack(stack):
    if len(stack) <= 1:
        return stack

    top = stack.pop()
    reverse_stack(stack)
    stack.insert(0, top)
    return stack

# Test
stack = [1,2,3,4,5,6,7,8,9,10]
result = reverse_stack(stack.copy())
print("Array:", result)

# Part 2: Linked list version
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

head = Node(1)
cur = head
for i in range(2, 11):
    cur.next = Node(i)
    cur = cur.next
head = reverse_linked_list(head)
cur = head
print("Linked List:", end=" ")
while cur:
    print(cur.data, end=" ")
    cur = cur.next
print()


# Part 3: Doubly linked list version
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    if head is None:
        return None
    temp = head.prev
    head.prev = head.next
    head.next = temp
    if head.prev is None:
        return head
    return reverse_doubly_linked_list(head.prev)

head = DNode(1)
cur = head
for i in range(2, 11):
    node = DNode(i)
    cur.next = node
    node.prev = cur
    cur = node
head = reverse_doubly_linked_list(head)
cur = head
print("Doubly Linked List:", end=" ")
while cur:
    print(cur.data, end=" ")
    cur = cur.next
print()
