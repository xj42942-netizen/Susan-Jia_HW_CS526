class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def sum_three_middle(head):

    # Use fast and slow pointers to find the middle node
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Return sum of previous, current and next nodes
    return slow.prev.value + slow.value + slow.next.value

# Create test list: 2->4->8->10->15->29->41
def create_list(values):
    head = Node(values[0])
    current = head
    
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    return head

# Test
values = [2, 4, 8, 10, 15, 29, 41]
head = create_list(values)
result = sum_three_middle(head)
print(result)
