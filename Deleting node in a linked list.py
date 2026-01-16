#initialize a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_by_value(head, value):
    # An Empty list
    if not head:
        return head

    # Delete the  node head
    if head.data == value:
        return head.next

    # Traverse and find the node
    current = head
    while current.next and current.next.data != value:
        current = current.next
     # Delete value if it was found.
    if current.next:
        current.next = curren

    return head


def print_list(head):
    current = head
    while current:
        print(current.data, end=" → ")
        current = current.next
    print("None")


