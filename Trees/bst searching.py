#Searching in binary search
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            return self.left.search(data) if self.left else False
        else:
            return self.right.search(data) if self.right else False


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    key = 5
    print(root.search(key))


