# Define the Node class
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Traverse and print the linked list
def traverseList(head):
    current = head
    while current is not None:
        print(current.data, end="")
        if current.next is not None:
            print(" -> ", end="")
        current = current.next
    print(" -> null")


# Create the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Traverse the list
traverseList(head)


